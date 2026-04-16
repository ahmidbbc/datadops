#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VALID_DEPENDENCIES = {
    "analyze_datadog_logs",
    "apm_search_spans",
    "get_datadog_metric",
    "search_datadog_events",
    "search_datadog_logs",
    "search_datadog_monitors",
    "search_datadog_services",
    "search_datadog_spans",
}


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path}: invalid JSON ({exc})")
        return None


def fail(message: str):
    ERRORS.append(message)


def extract_frontmatter(path: Path, text: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path}: missing or malformed frontmatter")
        return ""
    return match.group(1)


def check_json_files():
    plugin = load_json(ROOT / ".claude-plugin" / "plugin.json")
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    mcp = load_json(ROOT / ".mcp.json")

    if not all(isinstance(obj, dict) for obj in (plugin, marketplace, mcp)):
        return

    if plugin.get("name") != "datadops":
        fail("plugin.json: expected plugin name 'datadops'")

    marketplace_plugins = marketplace.get("plugins", [])
    datadops_entry = next((p for p in marketplace_plugins if p.get("name") == "datadops"), None)
    if not datadops_entry:
        fail("marketplace.json: missing datadops plugin entry")
    else:
        if datadops_entry.get("version") != plugin.get("version"):
            fail("marketplace.json: datadops version does not match plugin.json")

    datadog = mcp.get("mcpServers", {}).get("datadog")
    if not datadog:
        fail(".mcp.json: missing mcpServers.datadog")
    else:
        if datadog.get("type") != "http":
            fail(".mcp.json: datadog server must use type 'http'")
        if "datadoghq.com" not in datadog.get("url", ""):
            fail(".mcp.json: datadog server URL must target Datadog")


def check_templates():
    config = load_json(ROOT / "templates" / "monitoring-templates.json")
    if not isinstance(config, dict):
        return

    templates = config.get("templates", {})
    monitors = templates.get("monitors", {})
    dashboards = templates.get("dashboards", {})
    service_configurations = config.get("service_configurations", {})

    if not isinstance(monitors, dict):
        fail("templates/monitoring-templates.json: templates.monitors must be an object")
        return
    if not isinstance(dashboards, dict):
        fail("templates/monitoring-templates.json: templates.dashboards must be an object")
        return
    if not isinstance(service_configurations, dict):
        fail("templates/monitoring-templates.json: service_configurations must be an object")
        return

    for service_name, service_config in service_configurations.items():
        if not isinstance(service_config, dict):
            fail(f"templates/monitoring-templates.json: {service_name} config must be an object")
            continue

        dashboard_name = service_config.get("dashboard_template")
        if dashboard_name and dashboard_name not in dashboards:
            fail(
                "templates/monitoring-templates.json: "
                f"{service_name} references unknown dashboard '{dashboard_name}'"
            )

        for monitor_name in service_config.get("monitors", []):
            if monitor_name not in monitors:
                fail(
                    "templates/monitoring-templates.json: "
                    f"{service_name} references unknown monitor '{monitor_name}'"
                )


def check_skill_files():
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        frontmatter = extract_frontmatter(path, text)
        if not frontmatter:
            continue

        if "tools: [datadog]" not in frontmatter:
            fail(f"{path}: compatibility.tools must be [datadog]")

        if "argument-hint:" not in frontmatter:
            fail(f"{path}: missing argument-hint")

        dep_match = re.search(r"dependencies:\s*\[([^\]]*)\]", frontmatter)
        if not dep_match:
            fail(f"{path}: missing compatibility.dependencies list")
            deps = []
        else:
            deps = [item.strip() for item in dep_match.group(1).split(",") if item.strip()]
            invalid = [dep for dep in deps if dep not in VALID_DEPENDENCIES]
            if invalid:
                fail(f"{path}: unknown dependency names: {', '.join(invalid)}")

        if "claude skill " in text:
            fail(f"{path}: still contains legacy 'claude skill' examples")


def check_docs():
    for rel_path in ["README.md", "setup/installation-guide.md"]:
        path = ROOT / rel_path
        text = path.read_text(encoding="utf-8")
        if re.search(r"^\s*claude mcp add\b", text, re.MULTILINE):
            fail(f"{path}: still contains manual 'claude mcp add' installation instructions")
        if re.search(r"^\s*claude skill\b", text, re.MULTILINE):
            fail(f"{path}: still contains legacy 'claude skill' examples")


def main():
    check_json_files()
    check_skill_files()
    check_templates()
    check_docs()

    if ERRORS:
        print("Smoke test failed:\n")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Smoke test passed.")
    return 0


ERRORS = []


if __name__ == "__main__":
    sys.exit(main())
