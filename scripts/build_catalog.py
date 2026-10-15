#!/usr/bin/env python3
"""Build the manufacturer index and preview galleries from model READMEs."""

from dataclasses import dataclass
from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
TABLE = re.compile(r"^\|[^\n]+\n\|[-:| ]+\n(?:\|[^\n]+\n)+", re.MULTILINE)
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


@dataclass
class Model:
    directory: Path
    title: str
    entries: list[tuple[str, str, str]]

    @property
    def formats(self) -> list[str]:
        return list(dict.fromkeys(fmt for _, fmt, _ in self.entries))


def cells(row: str) -> list[str]:
    return [cell.strip() for cell in row.strip().strip("|").split("|")]


def read_model(path: Path) -> Model:
    text = path.read_text()
    section = text.split("## Model entries\n", 1)[1].split("\n## ", 1)[0]
    table = TABLE.search(section)
    entries = []
    for row in table.group().splitlines()[2:]:
        purpose, fmt, link, _ = cells(row)
        target = LINK.search(link).group(1)
        if not (path.parent / target).is_file():
            raise ValueError(f"Missing model entry: {path.parent / target}")
        entries.append((purpose, fmt, target))
    return Model(path.parent, text.splitlines()[0].removeprefix("# "), entries)


def entry_links(model: Model) -> str:
    links = []
    for fmt in model.formats:
        entries = [entry for entry in model.entries if entry[1] == fmt]
        primary = next(
            (entry for entry in entries if "demonstration" not in entry[0].lower()),
            entries[0],
        )
        links.append(f"[{fmt}]({model.directory.name}/{primary[2]})")
    if len(model.entries) > len(model.formats):
        links.append(f"[All {len(model.entries)} entries]({model.directory.name}/README.md#model-entries)")
    return "<br>".join(links)


def add_model_preview(model: Model) -> None:
    path = model.directory / "README.md"
    text = path.read_text()
    if 'src="preview.png"' in text:
        return
    title, content = text.split("\n", 1)
    navigation = "[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)"
    preview = f'<img src="preview.png" width="480" alt="{escape(model.title, quote=True)} model preview">'
    caption = "MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)"
    path.write_text(f"{title}\n\n{navigation}\n\n{preview}\n\n{caption}\n{content}")


def update_brand(path: Path, models: list[Model]) -> None:
    text = path.read_text()
    table = TABLE.search(text)
    old_rows = table.group().splitlines()
    headers = cells(old_rows[0])
    replaced = {
        "Preview", "Model", "Model / assembly", "Format", "Included formats",
        "Entry", "Native entries", "Documentation", "Format notes", "Model documentation",
    }
    extra_columns = [i for i, name in enumerate(headers) if name not in replaced]
    extra_values = {}
    for row in old_rows[2:]:
        values = cells(row)
        model_link = re.search(r"\]\(([^/()]+)/README\.md\)", row)
        if model_link:
            extra_values[model_link.group(1)] = [values[i] for i in extra_columns]

    extra_headers = [headers[i] for i in extra_columns]
    if any("MJCF" in model.formats and "URDF" in model.formats for model in models):
        extra_headers = ["URDF " + name.lower() if name in {"Upstream", "Source status", "Source"} else name for name in extra_headers]
    new_headers = ["Preview", "Model / assembly", "Native entries"] + extra_headers
    rows = ["| " + " | ".join(new_headers) + " |", "|" + "---|" * len(new_headers)]
    for model in models:
        slug = model.directory.name
        title = model.title.replace("|", "\\|")
        image = f'<img src="{slug}/preview.png" width="240" alt="{escape(model.title, quote=True)} model preview">'
        values = [f"[{image}]({slug}/README.md)", f"[{title}]({slug}/README.md)", entry_links(model)]
        values.extend(extra_values.get(slug, [""] * len(extra_columns)))
        rows.append("| " + " | ".join(values) + " |")
    text = text[:table.start()] + "\n".join(rows) + "\n" + text[table.end():]
    navigation = "[All manufacturers](../../README.md#models) · [Chinese index](../../README_CN.md#模型目录)"
    if navigation not in text:
        title, content = text.split("\n", 1)
        text = f"{title}\n\n{navigation}\n{content}"
    caption = "Previews are rendered with MuJoCo. See the [rendering method](../../docs/PREVIEWS.md); each model page links its exact entry and rendering record."
    if caption not in text:
        text = text.replace(navigation, navigation + "\n\n" + caption, 1)
    path.write_text(text)


def update_root(brands: dict[str, list[Model]], names: dict[str, str]) -> None:
    headers = {
        "README.md": "| Brand | Models | Formats |\n|---|---:|---|",
        "README_CN.md": "| 品牌 | 模型数 | 格式 |\n|---|---:|---|",
    }
    rows = []
    for brand, models in brands.items():
        formats = sorted({fmt for model in models for fmt in model.formats}, reverse=True)
        rows.append(f"| [{names[brand]}](models/{brand}/README.md) | {len(models)} | {', '.join(formats)} |")
    start_marker = "<!-- MODEL_CATALOG:START -->"
    end_marker = "<!-- MODEL_CATALOG:END -->"
    for filename, header in headers.items():
        path = ROOT / filename
        text = path.read_text()
        before, rest = text.split(start_marker, 1)
        _, after = rest.split(end_marker, 1)
        path.write_text(f"{before}{start_marker}\n\n{header}\n" + "\n".join(rows) + f"\n\n{end_marker}{after}")


def main() -> None:
    names = {brand: name for name, brand in re.findall(
        r"^\| \[([^\]]+)\]\(models/([^/]+)/README\.md\)",
        (ROOT / "README.md").read_text(), re.MULTILINE,
    )}
    brands = {}
    for brand in sorted((ROOT / "models").iterdir()):
        models = [read_model(path) for path in sorted(brand.glob("*/README.md"))]
        if not models:
            continue
        brands[brand.name] = models
        names.setdefault(brand.name, (brand / "README.md").read_text().splitlines()[0].removeprefix("# ").removesuffix(" models"))
        update_brand(brand / "README.md", models)
        for model in models:
            add_model_preview(model)
    update_root(brands, names)
    print(f"Updated {len(brands)} manufacturer galleries and {sum(map(len, brands.values()))} model previews.")


if __name__ == "__main__":
    main()
