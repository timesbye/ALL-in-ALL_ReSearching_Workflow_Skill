#!/usr/bin/env bash
set -euo pipefail

TOOLKIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_SOURCE="$TOOLKIT_ROOT/skills/scientific-figure-making"
CODEX_SKILLS="$HOME/.codex/skills"
SKILL_TARGET="$CODEX_SKILLS/scientific-figure-making"

if [ ! -d "$SKILL_SOURCE" ]; then
  echo "Skill source does not exist: $SKILL_SOURCE"
  exit 1
fi

mkdir -p "$CODEX_SKILLS"

if [ -e "$SKILL_TARGET" ]; then
  echo "Existing skill target found: $SKILL_TARGET"
  echo "Remove it manually if you want to recreate the link."
  exit 0
fi

ln -s "$SKILL_SOURCE" "$SKILL_TARGET"

echo "Installed scientific-figure-making skill to Codex:"
echo "$SKILL_TARGET"
