#!/usr/bin/env python3
"""Validate the public repository, Pages metadata, and generated brand assets."""

from __future__ import annotations

import json
import struct
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CANONICAL = "https://atdy.github.io/maoxuan-product-agent/"
INSTALL_COMMAND = (
    "npx skills add atdy/maoxuan-product-agent --skill product-decision-agent "
    "--agent codex claude-code cursor -g -y"
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.in_title = False
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.assets: list[str] = []
        self.json_ld: list[str] = []
        self._json_buffer: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            self.meta.append(values)
        elif tag == "link":
            self.links.append(values)
            if values.get("href"):
                self.assets.append(values["href"])
        elif tag in {"img", "script"} and values.get("src"):
            self.assets.append(values["src"])

        if tag == "script" and values.get("type") == "application/ld+json":
            self._json_buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self._json_buffer is not None:
            self.json_ld.append("".join(self._json_buffer))
            self._json_buffer = None

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self._json_buffer is not None:
            self._json_buffer.append(data)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    require(data[:8] == b"\x89PNG\r\n\x1a\n", f"{path} is not a PNG")
    return struct.unpack(">II", data[16:24])


def meta_content(parser: PageParser, *, name: str | None = None, prop: str | None = None) -> str:
    for item in parser.meta:
        if name and item.get("name") == name:
            return item.get("content", "")
        if prop and item.get("property") == prop:
            return item.get("content", "")
    return ""


def validate_page() -> None:
    index = DOCS / "index.html"
    parser = PageParser()
    parser.feed(index.read_text(encoding="utf-8"))

    title = "".join(parser.title_parts).strip()
    require("Maoxuan Product Agent" in title, "Page title is missing the product name")
    require("产品决策 Agent" in title, "Page title is missing the Chinese search intent")
    require(len(meta_content(parser, name="description")) >= 60, "Meta description is too short")
    require(meta_content(parser, prop="og:image").endswith("/assets/social-preview.png"), "Open Graph image is missing")
    require(meta_content(parser, name="twitter:card") == "summary_large_image", "Twitter large card is missing")

    canonical = next((item.get("href") for item in parser.links if item.get("rel") == "canonical"), None)
    require(canonical == CANONICAL, "Canonical URL is incorrect")

    for asset in parser.assets:
        parsed = urlparse(asset)
        if parsed.scheme or asset.startswith("#") or asset.startswith("/"):
            continue
        require((DOCS / parsed.path).exists(), f"Missing local page asset: {asset}")

    require(len(parser.json_ld) == 1, "Expected one JSON-LD graph")
    graph = json.loads(parser.json_ld[0]).get("@graph", [])
    types = {item.get("@type") for item in graph}
    require({"SoftwareApplication", "HowTo", "FAQPage"} <= types, "JSON-LD graph is incomplete")
    faq = next(item for item in graph if item.get("@type") == "FAQPage")
    require(len(faq.get("mainEntity", [])) >= 6, "JSON-LD FAQ needs at least six questions")


def validate_assets() -> None:
    expected = {
        DOCS / "assets/social-preview.png": (1280, 640),
        DOCS / "assets/product-output-preview.png": (1200, 780),
        DOCS / "assets/hero-decision-map.png": (1600, 900),
    }
    for path, size in expected.items():
        require(path.exists(), f"Missing generated asset: {path}")
        require(read_png_size(path) == size, f"Unexpected dimensions for {path}")


def validate_discovery_files() -> None:
    sitemap = ET.parse(DOCS / "sitemap.xml")
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [node.text for node in sitemap.findall("sm:url/sm:loc", namespace)]
    require(CANONICAL in locations, "Canonical URL is missing from sitemap.xml")

    robots = (DOCS / "robots.txt").read_text(encoding="utf-8")
    require("Allow: /" in robots, "robots.txt does not allow crawling")
    require("sitemap.xml" in robots, "robots.txt does not advertise sitemap.xml")

    llms = (DOCS / "llms.txt").read_text(encoding="utf-8")
    llms_full = (DOCS / "llms-full.txt").read_text(encoding="utf-8")
    require(CANONICAL in llms, "llms.txt is missing the canonical URL")
    require(INSTALL_COMMAND in llms, "llms.txt is missing the verified install command")
    require("Core reasoning behavior" in llms_full, "llms-full.txt is missing the reasoning description")
    require("Frequently asked questions" in llms_full, "llms-full.txt is missing FAQ content")


def validate_repository_package() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "README_EN.md",
        ROOT / "CHANGELOG.md",
        ROOT / "CITATION.cff",
        ROOT / "LICENSE",
        ROOT / "product-decision-agent/SKILL.md",
        ROOT / "docs/.nojekyll",
    ]
    for path in required:
        require(path.exists(), f"Missing public repository file: {path}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require(INSTALL_COMMAND in readme, "README is missing the verified install command")
    require("《矛盾论》《实践论》" in readme, "README does not foreground the methodology source")

    agent_metadata = (ROOT / "product-decision-agent/agents/openai.yaml").read_text(encoding="utf-8")
    require("allow_implicit_invocation: true" in agent_metadata, "Implicit invocation must stay enabled")
    require("产品" in agent_metadata and "行动" in agent_metadata, "Agent metadata lacks product-action intent")
    for source_term in ("毛选", "毛泽东", "矛盾论", "实践论"):
        require(source_term not in agent_metadata, f"Agent metadata exposes source term: {source_term}")


def main() -> None:
    validate_page()
    validate_assets()
    validate_discovery_files()
    validate_repository_package()
    print("Publication validation passed.")


if __name__ == "__main__":
    main()
