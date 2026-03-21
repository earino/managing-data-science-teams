#!/usr/bin/env python3
"""
Inject expected clock times into Marp slide talk tracks.

Times are derived from the minute-by-minute timing tables in each block's
facilitator-notes.md. Each slide gets a comment like:

    <!-- ⏱ Expected: 11:05 | Minute 5 of 100 -->

For skipped slides (present in deck but not presented):

    <!-- ⏱ Expected: ~11:15 | SKIP — advance past -->

For activity slides (slide stays up during timed activity):

    <!-- ⏱ Expected: 11:45 | Activity: Draft Team Charter (22 min) -->

Usage:
    python3 scripts/inject-timing.py          # dry-run (shows what would change)
    python3 scripts/inject-timing.py --apply   # actually modify files
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Timing data — manually verified against each block's facilitator-notes.md
# Format: list of (clock_time, slide_list, optional_note)
#   clock_time: "HH:MM"
#   slide_list: list of 1-based slide numbers
#   note: None, "SKIP", or activity description
# ---------------------------------------------------------------------------

def r(a, b):
    """Inclusive range helper."""
    return list(range(a, b + 1))


BLOCKS = [
    # ---- BLOCK A: Manager's Operating System (Day 1, 11:00–12:40, 100 min, 55 slides) ----
    {
        "path": ROOT / "day-1" / "block-a-manager-os" / "slides.md",
        "start": "11:00",
        "duration": 100,
        "expected_slides": 55,
        "entries": [
            ("11:00", r(1, 3), None),
            ("11:05", r(4, 9), None),
            ("11:10", r(10, 11), None),
            ("11:15", [12], None),
            ("11:15", r(13, 14), "SKIP"),
            ("11:18", r(15, 18), None),
            ("11:21", r(19, 21), None),
            ("11:21", [22], "SKIP"),
            ("11:24", [23], None),
            ("11:24", r(24, 25), "SKIP"),
            ("11:27", r(26, 27), None),
            ("11:27", r(28, 30), "SKIP"),
            ("11:30", r(31, 32), None),
            ("11:30", r(33, 35), "SKIP"),
            ("11:33", r(36, 40), None),
            ("11:33", r(41, 43), "SKIP"),
            ("11:37", r(44, 46), "Activity brief — Team Charter; activity starts at 11:45"),
            ("12:07", r(47, 48), "Activity brief — Stakeholder Map"),
            ("12:09", [49], "Activity: Map Stakeholders (18 min)"),
            ("12:27", [50], "Pair Share (5 min)"),
            ("12:32", r(51, 55), "Debrief + Transition to Block B"),
        ],
    },

    # ---- BLOCK B: Hiring & Team Formation (Day 1, 13:30–15:10, 100 min, 58 slides) ----
    {
        "path": ROOT / "day-1" / "block-b-hiring" / "slides.md",
        "start": "13:30",
        "duration": 100,
        "expected_slides": 58,
        "entries": [
            ("13:30", r(1, 9), None),
            ("13:35", r(10, 20), None),
            ("13:45", r(21, 24), None),
            ("13:55", r(25, 33), None),
            ("13:55", r(34, 36), "SKIP"),
            ("14:05", r(37, 42), None),
            ("14:05", r(43, 47), "SKIP"),
            ("14:10", r(48, 50), "Activity brief — JD + Rubric; activity starts at 14:13"),
            ("14:38", r(51, 53), "Role-Play Setup"),
            ("15:02", r(54, 58), "Debrief"),
        ],
    },

    # ---- BLOCK C: Roadmaps, Bets, and Alignment (Day 1, 15:30–17:10, 100 min, 45 slides) ----
    {
        "path": ROOT / "day-1" / "block-c-roadmaps" / "slides.md",
        "start": "15:30",
        "duration": 100,
        "expected_slides": 45,
        "entries": [
            ("15:30", r(1, 2), None),
            ("15:32", r(3, 8), None),
            ("15:37", r(9, 10), None),
            ("15:42", r(11, 15), None),
            ("15:48", r(16, 21), None),
            ("15:48", [22], "SKIP"),
            ("15:52", [23], None),
            ("15:52", r(24, 25), "SKIP"),
            ("15:55", r(26, 31), None),
            ("16:00", r(32, 33), None),
            ("16:03", [34], None),
            ("16:05", r(35, 36), "Activity brief — Roadmap; activity starts at 16:06"),
            ("16:36", r(37, 38), "Activity brief — Exec Narrative; activity starts at 16:37"),
            ("16:57", r(39, 40), "Red-Team brief; exercise starts at 16:58"),
            ("17:06", [41], "Debrief (1 min)"),
            ("17:07", r(42, 45), "Checkpoint upload + Close"),
        ],
    },

    # ---- BLOCK D: Growth & Performance (Day 2, 11:00–12:40, 100 min, 33 slides) ----
    # NOTE: Facilitator notes use an older slide numbering (22 slides).
    # Actual deck has 33 slides due to content splits.
    # Mapping verified against actual slide content.
    {
        "path": ROOT / "day-2" / "block-d-growth" / "slides.md",
        "start": "11:00",
        "duration": 100,
        "expected_slides": 33,
        "entries": [
            ("11:00", r(1, 2), None),      # Title + Learning Outcomes
            ("11:03", r(3, 4), None),       # Welcome Back (2 slides)
            ("11:06", [5], None),           # Why Growth & Performance Matter
            ("11:09", [6], None),           # Career Ladders
            ("11:13", r(7, 8), None),       # What "Senior" Means (2 slides)
            ("11:18", [9], None),           # PGP vs PIP
            ("11:21", r(10, 11), None),     # PGP Structure + SBI Model
            ("11:25", [12], None),          # Radical Candor
            ("11:28", r(13, 14), None),     # Performance Cycles (2 slides)
            ("11:32", r(15, 16), None),     # Calibration Sessions (2 slides)
            ("11:35", r(17, 18), None),     # Ethical PIP (2 slides)
            ("11:35", r(19, 21), "Activity: SBI Feedback Role-Play (22 min)"),
            ("11:57", r(22, 24), "Activity: Mock Calibration (17 min)"),
            ("12:14", r(25, 27), "Activity: PGP Draft (17 min)"),
            ("12:31", r(28, 33), "Debrief + Key Takeaways + Transition"),
        ],
    },

    # ---- BLOCK E: Infrastructure & Cross-Functional Interfaces (Day 2, 13:30–15:10, 100 min, 30 slides) ----
    # NOTE: Facilitator notes count Marp config as "slide 1".
    # Actual slide 1 = notes slide 2, etc.
    {
        "path": ROOT / "day-2" / "block-e-infrastructure" / "slides.md",
        "start": "13:30",
        "duration": 100,
        "expected_slides": 30,
        "entries": [
            ("13:30", r(1, 3), None),       # Title + Learning Outcomes + Shifting Gears
            ("13:32", r(4, 5), "Why Infrastructure Matters (4 min)"),
            ("13:36", r(6, 7), "XFN Universe + Failure Modes (6 min)"),
            ("13:42", r(8, 10), "Bidirectional SLAs (6 min)"),
            ("13:48", r(11, 13), "Blueprint + Architecture Diagrams (8 min)"),
            ("13:56", r(14, 15), "Build vs. Buy + Hidden Costs (8 min)"),
            ("14:04", [16], "Pair discussion: build or buy (2 min)"),
            ("14:06", r(17, 21), "Stack by Size — small/medium/large + migration trap (10 min)"),
            ("14:16", r(22, 23), "IT, Procurement, Privacy (6 min)"),
            ("14:22", r(24, 26), "Activity: Data Infra One-Pager (30 min)"),
            ("14:52", r(27, 28), "Debrief + portfolio connection (8 min)"),
            ("15:00", r(29, 30), "Buffer + Transition to Block F"),
        ],
    },

    # ---- BLOCK F: Leading Up & Executive Communication (Day 2, 15:30–17:10, 100 min, 28 slides) ----
    {
        "path": ROOT / "day-2" / "block-f-leading-up" / "slides.md",
        "start": "15:30",
        "duration": 100,
        "expected_slides": 28,
        "entries": [
            ("15:30", r(1, 4), None),       # Title + Learning Outcomes + Final Block framing
            ("15:32", r(5, 8), "Pyramid Principle / BLUF / Executive Attention (8 min)"),
            ("15:40", r(9, 10), "Three Executive Questions + Anti-Patterns (6 min)"),
            ("15:46", r(11, 12), "Art of the Ask (6 min)"),
            ("15:52", r(13, 16), "Communicating Failure lecture (10 min)"),
            ("16:02", r(17, 18), "Discussion: delivering worst news (15 min)"),
            ("16:17", [19], "First 90 Days (compressed, 5 min)"),
            ("16:22", r(20, 21), "BLUF Rehearsal — pair exercise (8 min)"),
            ("16:30", [22], "AI and the Changing Manager Role (3 min)"),
            ("16:33", r(23, 24), "Async QBR briefing (8 min)"),
            ("16:41", r(25, 26), "Portfolio checklist + logistics (5 min)"),
            ("16:46", r(27, 28), "Course close + celebration (10 min)"),
        ],
    },
]


def parse_time(t):
    """Parse 'HH:MM' into total minutes since midnight."""
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def format_minute(clock_time, start_time):
    """Return minute offset from block start."""
    return parse_time(clock_time) - parse_time(start_time)


def build_slide_map(block):
    """Build {slide_number: (clock_time, minute_offset, note)} for a block."""
    slide_map = {}
    for clock_time, slides, note in block["entries"]:
        minute = format_minute(clock_time, block["start"])
        for s in slides:
            if s in slide_map:
                # Keep the first (most specific) entry
                continue
            slide_map[s] = (clock_time, minute, note)
    return slide_map


def make_timing_comment(clock_time, minute, duration, note):
    """Create the timing HTML comment."""
    if note and note == "SKIP":
        return f"<!-- ⏱ Expected: ~{clock_time} (min {minute}/{duration}) | SKIP — advance past -->"
    elif note:
        return f"<!-- ⏱ Expected: {clock_time} (min {minute}/{duration}) | {note} -->"
    else:
        return f"<!-- ⏱ Expected: {clock_time} (min {minute}/{duration}) -->"


def split_slides(content):
    """Split a Marp markdown file into frontmatter + list of slide contents.

    Returns (frontmatter_str, [slide_content_str, ...])
    where frontmatter_str includes both --- delimiters.
    """
    lines = content.split("\n")

    # Find frontmatter boundaries
    sep_indices = [i for i, line in enumerate(lines) if line.strip() == "---"]
    if len(sep_indices) < 2:
        raise ValueError("Could not find frontmatter delimiters")

    fm_end = sep_indices[1]
    frontmatter = "\n".join(lines[: fm_end + 1])

    # Everything after frontmatter
    rest = "\n".join(lines[fm_end + 1 :])

    # Split by --- separators
    # We need to split on lines that are exactly "---"
    slide_parts = re.split(r"\n---\n", rest)

    return frontmatter, slide_parts


def inject_timing(block, dry_run=True):
    """Inject timing comments into a block's slides.md."""
    path = block["path"]
    content = path.read_text()

    # Check if timing already injected
    if "<!-- ⏱" in content:
        print(f"  SKIPPING {path.name} — timing already present")
        return False

    frontmatter, slides = split_slides(content)
    num_slides = len(slides)

    if num_slides != block["expected_slides"]:
        print(f"  ERROR: Expected {block['expected_slides']} slides, found {num_slides}")
        return False

    slide_map = build_slide_map(block)
    duration = block["duration"]

    # Check for unmapped slides
    unmapped = [s for s in range(1, num_slides + 1) if s not in slide_map]
    if unmapped:
        print(f"  WARNING: Unmapped slides: {unmapped}")
        return False

    # Inject timing comment into each slide
    new_slides = []
    for i, slide_content in enumerate(slides):
        slide_num = i + 1
        clock_time, minute, note = slide_map[slide_num]
        comment = make_timing_comment(clock_time, minute, duration, note)

        # Insert timing comment at the start of the slide content
        # Preserve leading newline(s) if any
        stripped = slide_content.lstrip("\n")
        leading_newlines = len(slide_content) - len(stripped)
        # Always have exactly one blank line before the timing comment
        new_slide = "\n" + comment + "\n" + stripped

        new_slides.append(new_slide)

    # Reassemble
    new_content = frontmatter + "\n---\n".join(new_slides)

    if dry_run:
        # Show a sample
        print(f"  Would modify {path}")
        print(f"  {num_slides} slides, all mapped")
        # Show first 3 timing comments as sample
        for i in range(min(3, num_slides)):
            slide_num = i + 1
            clock_time, minute, note = slide_map[slide_num]
            comment = make_timing_comment(clock_time, minute, duration, note)
            print(f"    Slide {slide_num}: {comment}")
        if num_slides > 3:
            print(f"    ... and {num_slides - 3} more")
    else:
        path.write_text(new_content)
        print(f"  Modified {path} ({num_slides} slides)")

    return True


def main():
    dry_run = "--apply" not in sys.argv

    if dry_run:
        print("DRY RUN — pass --apply to actually modify files\n")

    for block in BLOCKS:
        name = block["path"].parent.name
        print(f"\n{name}:")
        inject_timing(block, dry_run=dry_run)

    if dry_run:
        print("\n\nDry run complete. Use --apply to modify files.")


if __name__ == "__main__":
    main()
