#!/usr/bin/env bash
# build.sh — Render all Marp slide decks to HTML, then run validation and overflow checks.
#
# Usage:
#   ./scripts/build.sh          # render + validate + overflow check
#   ./scripts/build.sh --skip-render  # just run checks (if HTML already exists)

set -euo pipefail
cd "$(dirname "$0")/.."

SKIP_RENDER=false
for arg in "$@"; do
  case "$arg" in
    --skip-render) SKIP_RENDER=true ;;
  esac
done

# 1. Render slides to HTML
if [ "$SKIP_RENDER" = false ]; then
  echo "═══ Rendering Marp slides to HTML ═══"
  for f in day-*/block-*/slides.md; do
    marp --html "$f" 2>&1
  done
  echo ""
fi

# 2. Pedagogical validation (81 checks)
echo "═══ Pedagogical Validation ═══"
python3 scripts/validate.py
VALIDATE_EXIT=$?
echo ""

# 3. Overflow detection
echo "═══ Slide Overflow Check ═══"
python3 scripts/check-overflow.py
OVERFLOW_EXIT=$?
echo ""

# Summary
echo "═══ Build Summary ═══"
if [ $VALIDATE_EXIT -eq 0 ]; then
  echo "✓ Validation: all checks passed"
else
  echo "✗ Validation: some checks failed"
fi

if [ $OVERFLOW_EXIT -eq 0 ]; then
  echo "✓ Overflow: all slides fit"
else
  echo "✗ Overflow: some slides overflow (see above)"
fi

exit $(( VALIDATE_EXIT + OVERFLOW_EXIT ))
