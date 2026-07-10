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
INDEXNOW_KEY = "723a4fbfcdbb892bf323d26e59688a25"
CASE_PAGES = {
    "cases/index.html": {
        "url": f"{CANONICAL}cases/",
        "types": {"CollectionPage", "ItemList"},
    },
    "cases/boss-insert-request.html": {
        "url": f"{CANONICAL}cases/boss-insert-request.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/dau-decline.html": {
        "url": f"{CANONICAL}cases/dau-decline.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/ab-test-clicks-no-orders.html": {
        "url": f"{CANONICAL}cases/ab-test-clicks-no-orders.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/project-delay.html": {
        "url": f"{CANONICAL}cases/project-delay.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/requirement-prioritization.html": {
        "url": f"{CANONICAL}cases/requirement-prioritization.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/growth-stagnation.html": {
        "url": f"{CANONICAL}cases/growth-stagnation.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/retention-drop-after-release.html": {
        "url": f"{CANONICAL}cases/retention-drop-after-release.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/community-cold-start.html": {
        "url": f"{CANONICAL}cases/community-cold-start.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/content-supply-shortage.html": {
        "url": f"{CANONICAL}cases/content-supply-shortage.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/campaign-low-participation.html": {
        "url": f"{CANONICAL}cases/campaign-low-participation.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/data-definition-conflict.html": {
        "url": f"{CANONICAL}cases/data-definition-conflict.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
    "cases/conflicting-user-feedback.html": {
        "url": f"{CANONICAL}cases/conflicting-user-feedback.html",
        "types": {"Article", "BreadcrumbList", "FAQPage"},
    },
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.in_title = False
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.anchors: list[str] = []
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
        elif tag == "a" and values.get("href"):
            self.anchors.append(values["href"])
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


def validate_case_pages() -> None:
    docs_root = DOCS.resolve()
    titles: set[str] = set()
    descriptions: set[str] = set()
    article_urls = {
        expected["url"]
        for relative_path, expected in CASE_PAGES.items()
        if relative_path != "cases/index.html"
    }
    require(len(article_urls) == 12, "The public case library must contain twelve case articles")

    for relative_path, expected in CASE_PAGES.items():
        path = DOCS / relative_path
        require(path.exists(), f"Missing case page: {relative_path}")
        source = path.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(source)

        title = "".join(parser.title_parts).strip()
        description = meta_content(parser, name="description")
        require(len(title) >= 18, f"Case title is too short: {relative_path}")
        require(len(description) >= 60, f"Case description is too short: {relative_path}")
        require(title not in titles, f"Duplicate case title: {title}")
        require(description not in descriptions, f"Duplicate case description: {relative_path}")
        titles.add(title)
        descriptions.add(description)

        canonical = next((item.get("href") for item in parser.links if item.get("rel") == "canonical"), None)
        require(canonical == expected["url"], f"Case canonical URL is incorrect: {relative_path}")
        require(meta_content(parser, prop="og:image").startswith(CANONICAL), f"Case Open Graph image is invalid: {relative_path}")

        require(len(parser.json_ld) == 1, f"Expected one case JSON-LD graph: {relative_path}")
        graph = json.loads(parser.json_ld[0]).get("@graph", [])
        types = {item.get("@type") for item in graph}
        require(expected["types"] <= types, f"Case JSON-LD graph is incomplete: {relative_path}")

        if relative_path == "cases/index.html":
            item_list = next(item for item in graph if item.get("@type") == "ItemList")
            items = item_list.get("itemListElement", [])
            require(item_list.get("numberOfItems") == len(article_urls), "Case index count is incorrect")
            require({item.get("url") for item in items} == article_urls, "Case index JSON-LD URLs are incomplete")
        else:
            article = next(item for item in graph if item.get("@type") == "Article")
            faq = next(item for item in graph if item.get("@type") == "FAQPage")
            require(article.get("url") == expected["url"], f"Case Article URL is incorrect: {relative_path}")
            require(len(article.get("headline", "")) >= 12, f"Case Article headline is too short: {relative_path}")
            require(len(faq.get("mainEntity", [])) >= 2, f"Case FAQ needs at least two questions: {relative_path}")
            for section_id in ("question", "judgment", "why", "actions", "decision"):
                require(f'id="{section_id}"' in source, f"Case section is missing ({section_id}): {relative_path}")
            require("case-stop" in source, f"Case stop list is missing: {relative_path}")
            require("case-related" in source, f"Case related links are missing: {relative_path}")

        for asset in parser.assets:
            parsed = urlparse(asset)
            if parsed.scheme or asset.startswith("#") or asset.startswith("/"):
                continue
            asset_path = (path.parent / parsed.path).resolve()
            require(asset_path == docs_root or docs_root in asset_path.parents, f"Case asset escapes docs: {asset}")
            require(asset_path.exists(), f"Missing case asset: {relative_path} -> {asset}")

        for href in parser.anchors:
            parsed = urlparse(href)
            if parsed.scheme or href.startswith("#") or href.startswith("/"):
                continue
            target = (path.parent / parsed.path).resolve()
            require(target == docs_root or docs_root in target.parents, f"Case link escapes docs: {relative_path} -> {href}")
            require(target.exists(), f"Broken internal case link: {relative_path} -> {href}")


def validate_discovery_files() -> None:
    sitemap = ET.parse(DOCS / "sitemap.xml")
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [node.text for node in sitemap.findall("sm:url/sm:loc", namespace)]
    require(CANONICAL in locations, "Canonical URL is missing from sitemap.xml")
    for expected in CASE_PAGES.values():
        require(expected["url"] in locations, f"Case URL is missing from sitemap.xml: {expected['url']}")

    robots = (DOCS / "robots.txt").read_text(encoding="utf-8")
    require("Allow: /" in robots, "robots.txt does not allow crawling")
    require("sitemap.xml" in robots, "robots.txt does not advertise sitemap.xml")

    llms = (DOCS / "llms.txt").read_text(encoding="utf-8")
    llms_full = (DOCS / "llms-full.txt").read_text(encoding="utf-8")
    require(CANONICAL in llms, "llms.txt is missing the canonical URL")
    require(INSTALL_COMMAND in llms, "llms.txt is missing the verified install command")
    require("Core reasoning behavior" in llms_full, "llms-full.txt is missing the reasoning description")
    require("Frequently asked questions" in llms_full, "llms-full.txt is missing FAQ content")
    require(f"{CANONICAL}cases/" in llms, "llms.txt is missing the case index")
    for relative_path in CASE_PAGES:
        if relative_path == "cases/index.html":
            continue
        filename = Path(relative_path).name
        require(filename in llms, f"llms.txt is missing searchable case: {filename}")
        require(filename in llms_full, f"llms-full.txt is missing searchable case: {filename}")

    indexnow_key = (DOCS / f"{INDEXNOW_KEY}.txt").read_text(encoding="utf-8").strip()
    require(indexnow_key == INDEXNOW_KEY, "IndexNow verification file is invalid")


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
    validate_case_pages()
    validate_discovery_files()
    validate_repository_package()
    print("Publication validation passed.")


if __name__ == "__main__":
    main()
