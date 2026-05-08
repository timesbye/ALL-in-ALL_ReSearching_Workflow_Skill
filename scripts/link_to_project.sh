#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: ./scripts/link_to_project.sh /path/to/project"
  exit 1
fi

PROJECT_PATH="$1"
TOOLKIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AI_DIR="$PROJECT_PATH/.ai"
TOOLKIT_LINK="$AI_DIR/toolkit"

if [ ! -d "$PROJECT_PATH" ]; then
  echo "Project path does not exist: $PROJECT_PATH"
  exit 1
fi

mkdir -p "$AI_DIR"

if [ -e "$TOOLKIT_LINK" ]; then
  echo "Existing toolkit link found: $TOOLKIT_LINK"
  echo "Remove it manually if you want to recreate the link."
  exit 0
fi

ln -s "$TOOLKIT_ROOT" "$TOOLKIT_LINK"

echo "Linked toolkit to project:"
echo "$TOOLKIT_LINK"
