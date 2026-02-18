# Course Build Design: ECBS5256 – Managing Data Science Teams

**Date:** 2026-02-18
**Status:** Approved

## Goal

Build a complete v1 of the course: slide decks (Marp), facilitator notes, student templates, case contexts, and assessment materials.

## Format Decisions

- **Slides:** Markdown with Marp front matter. Each slide includes speaker notes (talk track / teleprompter) in `<!-- -->` blocks.
- **Facilitator notes:** Separate `facilitator-notes.md` per block with timing, setup, facilitation tips, contingencies.
- **Templates:** Structured markdown with guidance prompts, examples, and evaluation criteria.
- **Style:** Workshop-driver — lean concept slides that set up hands-on activities. Most class time is doing, not watching slides.

## Validation Approach (TDD for Pedagogy)

Before writing content, build validation scripts that check:

1. **Syllabus alignment** — every learning outcome maps to at least one slide deck and one template; every deliverable has a template.
2. **Marp validity** — all slide files have correct front matter and parse without errors.
3. **Completeness** — every block has slides, facilitator notes, and templates; all required files exist.
4. **Speaker notes coverage** — every content slide has a talk-track comment.
5. **Template structure** — every template has context header, sections, guidance, and evaluation criteria.
6. **Cross-references** — case contexts are referenced in templates; rubrics match portfolio components.

## File Structure

```
managing-analytics-teams/
├── syllabus.md
├── marp-theme.css
├── validate.sh                 # pedagogical alignment checker
├── day-1/
│   ├── block-a-manager-os/
│   │   ├── slides.md
│   │   ├── facilitator-notes.md
│   │   └── templates/
│   │       ├── team-charter.md
│   │       ├── stakeholder-map.md
│   │       ├── raci.md
│   │       └── decision-memo.md
│   ├── block-b-hiring/
│   │   ├── slides.md
│   │   ├── facilitator-notes.md
│   │   └── templates/
│   │       ├── job-description.md
│   │       ├── work-sample.md
│   │       ├── rubric.md
│   │       └── interview-loop.md
│   └── block-c-roadmaps/
│       ├── slides.md
│       ├── facilitator-notes.md
│       └── templates/
│           ├── roadmap-rice.md
│           ├── exec-narrative.md
│           └── risk-register.md
├── day-2/
│   ├── block-d-growth/
│   │   ├── slides.md
│   │   ├── facilitator-notes.md
│   │   └── templates/
│   │       ├── pgp.md
│   │       └── performance-summary.md
│   ├── block-e-infra-vendor/
│   │   ├── slides.md
│   │   ├── facilitator-notes.md
│   │   └── templates/
│   │       ├── data-infra-blueprint.md
│   │       └── rfp-scoring-matrix.md
│   └── block-f-qbr-simulation/
│       ├── slides.md
│       ├── facilitator-notes.md
│       └── templates/
│           ├── qbr-outline.md
│           └── portfolio-checklist.md
├── case-contexts/
│   ├── small-seed-stage.md
│   ├── medium-series-b.md
│   └── large-enterprise.md
├── assessment/
│   ├── grading-rubrics.md
│   ├── peer-feedback-form.md
│   └── portfolio-checklist.md
└── resources/
    └── manager-os-reference.md
```

## Slide Rhythm (per block)

1. Title slide — block name, time, learning outcomes
2. Concept slides (3-5) — framework, visual model, provocative question
3. Activity brief — what to build, time box, instructions
4. Discussion/debrief prompt
5. Transition slide

Every content slide has `<!-- talk track -->` speaker notes.

## Case Contexts

Three ~1-2 page scenarios:
- **Small (0→1):** "DataPulse" — seed-stage B2C fitness app, messy logging, no analytics hire yet
- **Medium (1→N):** "MarketBridge" — Series B marketplace, partial event tracking, privacy backlog, PMs want self-serve
- **Large (N→Scale):** "FinGuard" — regulated enterprise bank, data-mesh initiative, strict procurement, ROI pressure

Each includes: company profile, current data state, key stakeholders, pain points, constraints.

## Templates

Each template includes:
- Context header (case context, student name, date)
- Sections with guidance prompts
- One lightweight example (fictional company)
- Evaluation criteria (aligned to rubric)

## Assessment

- Per-component rubrics with Excellent / Good / Needs Work descriptors
- Portfolio checklist for self-assessment
- Structured peer feedback form
