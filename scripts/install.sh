#!/bin/sh
set -eu

usage() {
  cat <<'EOF'
Usage: ./scripts/install.sh <codex|claude|cursor|agents> [project-directory]

Without project-directory, install for the current user.
With project-directory, install only for that project.
EOF
}

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  usage
  exit 2
fi

agent="$1"
project_dir="${2:-}"
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_dir=$(dirname -- "$script_dir")
source_dir="$repo_dir/product-decision-agent"

case "$agent" in
  codex)
    user_root="$HOME/.agents/skills"
    project_root=".agents/skills"
    ;;
  claude)
    user_root="$HOME/.claude/skills"
    project_root=".claude/skills"
    ;;
  cursor)
    user_root="$HOME/.cursor/skills"
    project_root=".cursor/skills"
    ;;
  agents)
    user_root="$HOME/.agents/skills"
    project_root=".agents/skills"
    ;;
  *)
    usage
    exit 2
    ;;
esac

if [ -n "$project_dir" ]; then
  destination="$project_dir/$project_root/product-decision-agent"
else
  destination="$user_root/product-decision-agent"
fi

mkdir -p "$destination"
cp -R "$source_dir/." "$destination/"

printf 'Installed product-decision-agent to %s\n' "$destination"
