# ECBS5256: Managing Data Science Teams

## Course Overview

**A workshop-driven intensive on analytics leadership — from hiring to roadmaps to executive alignment.**

This course is part of Central European University's MS in Business Analytics program. Students build a complete **Manager Operating System** by producing real management artifacts anchored to one of three realistic company scenarios. The capstone is an async QBR video where students present their roadmap to a virtual executive panel.

## Key Information

| | |
|---|---|
| **Instructor** | Eduardo Ariño de la Rubia, Professor of Practice |
| **Contact** | By appointment, D-207 |
| **Format** | Two-day intensive, in-person |
| **Dates** | Monday March 16 & Monday March 23, 2026 |
| **Location** | CEU Vienna Campus, Room B-421 |
| **LMS** | Moodle |

## Course Structure

Each day has three 100-minute blocks with breaks between them.

### Day 1 — March 16

| Time | Block | Topic |
|------|-------|-------|
| 11:00–12:40 | **A** | The Manager's Operating System |
| 13:30–15:10 | **B** | Hiring & Team Formation |
| 15:30–17:10 | **C** | Roadmaps, Bets & Alignment |

### Day 2 — March 23

| Time | Block | Topic |
|------|-------|-------|
| 11:00–12:40 | **D** | Growth, Performance & Feedback |
| 13:30–15:10 | **E** | Infrastructure & Cross-Functional Interfaces |
| 15:30–17:10 | **F** | Leading Up & Executive Communication |

## What Students Build

All work is anchored to one of three case contexts that students choose on Day 1:

- **DataPulse** (Seed-stage) — First data hire at a fitness app startup
- **MarketBridge** (Series B) — New Head of Analytics at a two-sided marketplace
- **FinGuard** (Enterprise) — VP of Enterprise Analytics at a 120-year-old bank

### Portfolio Artifacts

| Artifact | Built In | Due |
|----------|----------|-----|
| Team Charter | Block A | Day 1 Checkpoint (draft) |
| Stakeholder Map | Block A | Day 1 Checkpoint (draft) |
| Hiring Packet (JD, work sample, rubric, interview loop) | Block B | March 30 |
| 12-Month Roadmap with RICE scoring | Block C | Day 1 Checkpoint (draft) |
| Executive Narrative (2 pages) | Block C | March 30 |
| Personal Growth Plan | Block D | March 30 |
| Performance Summary | Block D | March 30 |
| QBR Outline | Block F | March 30 |

## Repository Structure

```
├── syllabus.md                    # Full course syllabus
├── marp-theme.css                 # Custom Marp presentation theme
│
├── case-contexts/                 # Three realistic company scenarios
│   ├── small-seed-stage.md        # DataPulse (seed-stage B2C app)
│   ├── medium-series-b.md         # MarketBridge (Series B marketplace)
│   └── large-enterprise.md        # FinGuard (enterprise bank)
│
├── assessment/                    # Grading and evaluation
│   ├── grading-rubrics.md         # Detailed rubrics for all components
│   ├── portfolio-checklist.md     # Submission requirements
│   └── peer-feedback-form.md      # Structured peer review template
│
├── day-1/
│   ├── block-a-manager-os/
│   │   ├── slides.md              # Marp presentation source
│   │   ├── facilitator-notes.md   # Detailed teaching guide
│   │   └── templates/             # Team charter, stakeholder map, RACI, decision memo
│   ├── block-b-hiring/
│   │   ├── slides.md
│   │   ├── facilitator-notes.md
│   │   ├── materials/             # 4 candidate profiles for role-play
│   │   └── templates/             # JD, work sample, rubric, interview loop
│   └── block-c-roadmaps/
│       ├── slides.md
│       ├── facilitator-notes.md
│       └── templates/             # Roadmap-RICE, exec narrative, risk register
│
├── day-2/
│   ├── block-d-growth/
│   │   ├── slides.md
│   │   ├── facilitator-notes.md
│   │   ├── materials/             # SBI scenario cards, calibration profiles
│   │   └── templates/             # PGP, performance summary
│   ├── block-e-infrastructure/
│   │   ├── slides.md
│   │   └── facilitator-notes.md
│   └── block-f-leading-up/
│       ├── slides.md
│       ├── facilitator-notes.md
│       └── templates/             # QBR outline, portfolio checklist
│
├── resources/                     # Reference materials and self-study
│   ├── manager-os-reference.md    # Complete Manager OS reference guide
│   ├── data-infrastructure-guide.md
│   ├── between-days-checklist.md  # Reading and work guide for the week between days
│   └── advanced-infrastructure/   # Optional deep-dive on data stack decisions
│
└── scripts/                       # Build and validation tools
    ├── build.sh                   # Render slides + validate + check overflow
    ├── validate.py                # 82 pedagogical checks
    └── check-overflow.py          # Slide content overflow detection
```

## Grading

| Component | Weight | Due |
|-----------|--------|-----|
| Participation & Preparedness | 15% | Ongoing |
| Day 1 Checkpoint (draft artifacts) | 10% | March 16, 17:10 |
| Hiring Packet | 20% | March 30, 23:59 CET |
| Roadmap + Executive Narrative | 15% | March 30, 23:59 CET |
| QBR Outline + QBR Video | 10% | March 30, 23:59 CET |
| Manager OS Document | 15% | March 30, 23:59 CET |
| PGP + Performance Summary | 15% | March 30, 23:59 CET |

Full rubrics are in [`assessment/grading-rubrics.md`](assessment/grading-rubrics.md).

## Recommended Reading

### Before Day 1

- Camille Fournier, *The Manager's Path*, Ch. 1–3 (~70 pp)
- Andy Grove, *High Output Management*, Ch. 4 (~30 pp)

### Before Day 2

- Andy Grove, *High Output Management*, Ch. 11 (~30 pp)
- Camille Fournier, *The Manager's Path*, Ch. 6 (~30 pp)
- Will Larson, *An Elegant Puzzle*, Part 2 & §5.3 (~80 pp)

## For Students

1. Start with [`syllabus.md`](syllabus.md) for the full course overview
2. Read your chosen case context in [`case-contexts/`](case-contexts/)
3. Templates for each block are in the corresponding `templates/` directory
4. Check [`resources/between-days-checklist.md`](resources/between-days-checklist.md) for between-session work

## For Instructors

Slides use [Marp](https://marp.app/) (Markdown Presentation Ecosystem). Each block has a `slides.md` source file and a detailed `facilitator-notes.md` with minute-by-minute timing, teaching points, and contingency plans.

To build slides:

```bash
# Install dependencies (one time)
npm install
pip install marp-cli  # or install via npm

# Build all slides (render + validate + overflow check)
bash scripts/build.sh

# Build a single deck
bash scripts/build.sh day-1/block-a-manager-os/slides.md
```

Press `p` in the browser to enter presenter mode with talk track notes.

## Academic Integrity

- **Permitted:** Reviewing course materials, discussing concepts with classmates, consulting official documentation, using AI tools as a thinking partner (with attribution)
- **Required:** Cite AI assistance in your portfolio if used substantively
- **Prohibited:** Submitting AI-generated artifacts without meaningful personal contribution, copying classmate work, sharing solutions

See the full policy in [`syllabus.md`](syllabus.md).

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (Creative Commons Attribution 4.0 International). You are free to share and adapt this material with attribution.

## Author

**Eduardo Ariño de la Rubia** (rubiae@ceu.edu)

Professor of Practice, Central European University. Former Senior Director of Data Science at Meta; Chief Data Scientist at Domino Data Lab.

## Contributing

Contributions are welcome! If you have suggestions for improvements — new case contexts, better templates, additional resources, or corrections — please open an issue or submit a pull request. All contributions must be compatible with the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
