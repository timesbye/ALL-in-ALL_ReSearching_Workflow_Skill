#!/usr/bin/env bash
set -euo pipefail

TOOLKIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_ROOT="$TOOLKIT_ROOT/skills"
CODEX_SKILLS="$HOME/.codex/skills"

if [ ! -d "$SKILLS_ROOT" ]; then
  echo "Skills root does not exist: $SKILLS_ROOT"
  exit 1
fi

mkdir -p "$CODEX_SKILLS"

installed=()
skipped=()

for skill_source in "$SKILLS_ROOT"/*; do
  [ -d "$skill_source" ] || continue
  skill_name="$(basename "$skill_source")"
  skill_target="$CODEX_SKILLS/$skill_name"

  if [ -e "$skill_target" ]; then
    skipped+=("$skill_name")
    continue
  fi

  ln -s "$skill_source" "$skill_target"
  installed+=("$skill_name")
done

echo "Codex skill install complete."

if [ "${#installed[@]}" -gt 0 ]; then
  echo "Installed:"
  for skill_name in "${installed[@]}"; do
    echo "  - $skill_name"
  done
fi

if [ "${#skipped[@]}" -gt 0 ]; then
  echo "Skipped existing targets:"
  for skill_name in "${skipped[@]}"; do
    echo "  - $skill_name"
  done
fi
