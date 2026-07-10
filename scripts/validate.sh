#!/bin/sh
set -eu
export PYTHONDONTWRITEBYTECODE=1

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_dir=$(dirname -- "$script_dir")
cd "$repo_dir"

python3 product-decision-agent/scripts/test_quality_gate.py
python3 product-decision-agent/scripts/quality_gate.py evaluation/sample_output_case_*.md
python3 scripts/check_publication.py

if python3 product-decision-agent/scripts/quality_gate.py evaluation/sample_output_bad_example.md; then
  echo "Expected the deliberate bad example to fail." >&2
  exit 1
fi

pass_cases=$(grep -c '| PASS |' evaluation/self_test_report.md)
if [ "$pass_cases" -lt 36 ]; then
  echo "Expected at least 36 documented PASS cases, found $pass_cases." >&2
  exit 1
fi

echo "Project validation passed."
