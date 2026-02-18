# ECBS5256 Course Build — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the complete v1 of ECBS5256 "Managing Data Science Teams" — Marp slide decks with talk-track speaker notes, facilitator notes, student templates, case contexts, and assessment materials.

**Architecture:** TDD-for-pedagogy approach. First build a Python validation script that encodes what a well-formed course looks like (file structure, Marp validity, speaker notes coverage, template structure, syllabus alignment). Then build content block-by-block, running validators after each block to confirm pedagogical alignment. Each block is self-contained in its own folder.

**Tech Stack:** Markdown (Marp syntax), Python 3 (validation), Bash (orchestration)

---

### Task 1: Create Directory Structure

**Files:**
- Create: all directories per design doc

**Step 1: Create the full directory tree**

```bash
cd /Users/earino/CEU/managing-analytics-teams
mkdir -p day-1/block-a-manager-os/templates
mkdir -p day-1/block-b-hiring/templates
mkdir -p day-1/block-c-roadmaps/templates
mkdir -p day-2/block-d-growth/templates
mkdir -p day-2/block-e-infra-vendor/templates
mkdir -p day-2/block-f-qbr-simulation/templates
mkdir -p case-contexts
mkdir -p assessment
mkdir -p resources
```

**Step 2: Verify structure**

```bash
find . -type d | sort
```

Expected: all directories from design doc exist.

---

### Task 2: Build Validation Script

**Files:**
- Create: `validate.py`

This is the "test suite" for the course. It must FAIL before any content exists (red), then pass incrementally as we add content (green).

**Step 1: Write the validation script**

Create `validate.py` with these checks:

1. **Structure check** — verify all required files exist:
   - 6 `slides.md` files (one per block)
   - 6 `facilitator-notes.md` files
   - All template files per design doc
   - 3 case context files
   - Assessment files
   - `marp-theme.css`
   - `resources/manager-os-reference.md`

2. **Marp front matter check** — every `slides.md` starts with valid YAML front matter containing `marp: true`

3. **Speaker notes check** — every slide (separated by `\n---\n`) that has content (not just front matter or a blank separator) contains an HTML comment `<!-- ... -->` with at least 20 characters of talk track

4. **Template structure check** — every template file contains these sections:
   - A YAML-style header block or markdown header with "Context"
   - At least 3 `## ` sections
   - A section matching "Evaluation Criteria" or "How This Will Be Assessed"

5. **Syllabus alignment check** — cross-reference against known learning outcomes:
   - LO1 "Manager OS" → block-a slides + team-charter + stakeholder-map + raci + decision-memo
   - LO2 "Hiring packet" → block-b slides + job-description + work-sample + rubric + interview-loop
   - LO3 "Roadmap" → block-c slides + roadmap-rice + exec-narrative
   - LO4 "PGP" → block-d slides + pgp + performance-summary
   - LO5 "Data infrastructure" → block-e slides + data-infra-blueprint + rfp-scoring-matrix
   - LO6 "Align leadership" → block-f slides + qbr-outline

6. **Case context check** — each case context file has at least 5 `## ` sections and mentions key terms (stakeholders, constraints, data)

7. **Assessment check** — grading-rubrics.md contains sections for each portfolio component from syllabus

Output: colored pass/fail per check, summary count, exit code 1 if any failures.

**Step 2: Run validation — expect all failures**

```bash
python3 validate.py
```

Expected: all checks FAIL (red). This is our "red" phase.

---

### Task 3: Create Marp Theme

**Files:**
- Create: `marp-theme.css`

**Step 1: Write the CSS theme**

A clean, professional theme with:
- CEU-appropriate color palette (navy, white, accent gold)
- Clean sans-serif typography
- Styled headers, blockquotes (for pull quotes), and tables
- Slide number styling

**Step 2: Run validation**

```bash
python3 validate.py
```

Expected: marp-theme.css check now passes.

---

### Task 4: Create Case Contexts

**Files:**
- Create: `case-contexts/small-seed-stage.md`
- Create: `case-contexts/medium-series-b.md`
- Create: `case-contexts/large-enterprise.md`

**Step 1: Write "DataPulse" (Small / 0→1)**

~1.5 pages covering:
- **Company Profile:** Seed-stage B2C fitness app, 12 employees, $2M seed round, 50K MAU
- **Current Data State:** Firebase Analytics + random console.logs, no warehouse, founder queries production DB
- **Key Stakeholders:** CEO (wants growth metrics), Head of Product (wants funnel data), sole backend engineer
- **Pain Points:** No one trusts the numbers, A/B tests run on vibes, can't answer board questions about retention
- **Constraints:** $5K/mo budget for tools, no dedicated data person yet, need results in 90 days
- **Your Role:** First analytics hire, reporting to CEO, building from zero

**Step 2: Write "MarketBridge" (Medium / 1→N)**

~1.5 pages covering:
- **Company Profile:** Series B two-sided marketplace (home services), 150 employees, $30M raised, 500K transactions/month
- **Current Data State:** Segment + Mixpanel for product; Postgres read replica for ad-hoc SQL; Fivetran loading into BigQuery but nobody owns it; 3 analysts embedded in teams
- **Key Stakeholders:** VP Product (wants self-serve dashboards), Head of Growth (wants experimentation platform), Legal/Privacy officer (GDPR backlog), CTO (worried about data costs)
- **Pain Points:** Analysts are ticket-takers, PMs don't trust dashboards, privacy review blocks launches, no metric definitions agreed upon
- **Constraints:** $25K/mo data tooling budget, hiring freeze except for your team (can hire 2), EU data residency requirements
- **Your Role:** New Head of Analytics, reporting to CTO, inheriting 3 analysts and a messy stack

**Step 3: Write "FinGuard" (Large / N→Scale)**

~1.5 pages covering:
- **Company Profile:** Regional bank, 5,000 employees, publicly traded, heavy regulatory oversight (OCC, GDPR)
- **Current Data State:** On-prem Teradata warehouse, Tableau server (200+ dashboards, most broken), Informatica ETL, new Databricks pilot in cloud, data mesh aspirations but governance committee moves slowly
- **Key Stakeholders:** Chief Data Officer (your boss, wants ROI story), Head of Risk (needs model governance), IT/Infrastructure VP (controls procurement), Business line heads (skeptical of centralized analytics)
- **Pain Points:** 18-month procurement cycles, shadow analytics teams in every business unit, no one trusts the "single source of truth," ML models deployed without monitoring, regulatory exam coming in 6 months
- **Constraints:** $2M annual budget (sounds big but mostly Teradata license), 15-person team (mix of legacy SQL devs and new data scientists), everything needs IT security review
- **Your Role:** VP of Analytics, 2 years in, trying to modernize while keeping the lights on

**Step 4: Run validation**

```bash
python3 validate.py
```

Expected: case context checks pass.

---

### Task 5: Block A — The Manager's OS for Analytics

**Files:**
- Create: `day-1/block-a-manager-os/slides.md`
- Create: `day-1/block-a-manager-os/facilitator-notes.md`
- Create: `day-1/block-a-manager-os/templates/team-charter.md`
- Create: `day-1/block-a-manager-os/templates/stakeholder-map.md`
- Create: `day-1/block-a-manager-os/templates/raci.md`
- Create: `day-1/block-a-manager-os/templates/decision-memo.md`

**Step 1: Write slides.md**

Marp deck (~15-18 slides) following this flow:

1. **Title slide** — "The Manager's OS for Analytics" / Block A / 11:00-12:40 / Learning outcomes
2. **"What is a Manager?"** — Grove's output equation, the shift from IC to multiplier
3. **Manager vs. Tech Lead vs. PM** — Venn diagram of responsibilities, where analytics managers sit
4. **Team Topologies for Analytics** — stream-aligned, platform, enabling, complicated-subsystem applied to data teams
5. **The Manager OS concept** — cadences (daily/weekly/monthly/quarterly), rituals, artifacts, decision hygiene
6. **1:1s that work** — structure, anti-patterns, the update trap vs. coaching
7. **Decision logs & memos** — why writing > meetings, Amazon 6-pager concept adapted for analytics
8. **Activity Brief: Team Charter** — instructions, time box (25 min), what to include
9. **Activity Brief: Stakeholder Map** — instructions, time box (20 min), power/interest grid
10. **Debrief prompt** — share one surprise from your stakeholder map
11. **Transition** — preview Block B (hiring)

Every content slide gets a `<!-- talk track: ... -->` with 2-4 sentences of what to say.

**Step 2: Write facilitator-notes.md**

Cover:
- **Pre-class setup:** what to have on screen, handouts, room arrangement
- **Timing breakdown:** minute-by-minute for the 100-minute block
- **Key teaching points:** what to emphasize per slide
- **Common student questions** and how to handle them
- **Contingencies:** what to cut if running long, what to expand if running short
- **Transition notes:** how to bridge to Block B

**Step 3: Write templates (team-charter.md, stakeholder-map.md, raci.md, decision-memo.md)**

Each with: context header, guided sections, one example, evaluation criteria.

**Step 4: Run validation**

```bash
python3 validate.py
```

Expected: Block A checks pass.

---

### Task 6: Block B — Hiring & Team Formation

**Files:**
- Create: `day-1/block-b-hiring/slides.md`
- Create: `day-1/block-b-hiring/facilitator-notes.md`
- Create: `day-1/block-b-hiring/templates/job-description.md`
- Create: `day-1/block-b-hiring/templates/work-sample.md`
- Create: `day-1/block-b-hiring/templates/rubric.md`
- Create: `day-1/block-b-hiring/templates/interview-loop.md`

**Step 1: Write slides.md**

Marp deck (~15-18 slides):

1. **Title slide** — "Hiring & Team Formation" / Block B / 13:30-15:10
2. **The cost of a bad hire** — data on mis-hires in analytics, the "brilliant jerk" problem
3. **Role design before recruiting** — what does this role actually need to do in 90 days?
4. **Leveling basics** — IC vs. lead vs. manager levels, skills matrices for analytics
5. **Structured interviews > unstructured** — the research, why gut feel fails
6. **Work sample design** — what makes a good take-home/live exercise for analytics roles
7. **Rubric calibration** — how to score consistently, norming sessions
8. **The interview loop** — who interviews for what, debrief protocol, avoiding groupthink
9. **Candidate experience** — timelines, communication, rejection with dignity
10. **Activity Brief: Build Your Hiring Packet** — JD + work sample + rubric + loop (35 min)
11. **Role-play brief** — panel interview simulation setup
12. **Debrief** — what signals did you look for? what would you change?
13. **Transition** — preview Block C, remind about Thursday draft deadline

**Step 2: Write facilitator-notes.md**

**Step 3: Write templates (job-description.md, work-sample.md, rubric.md, interview-loop.md)**

**Step 4: Run validation**

---

### Task 7: Block C — Roadmaps, Bets, and Alignment

**Files:**
- Create: `day-1/block-c-roadmaps/slides.md`
- Create: `day-1/block-c-roadmaps/facilitator-notes.md`
- Create: `day-1/block-c-roadmaps/templates/roadmap-rice.md`
- Create: `day-1/block-c-roadmaps/templates/exec-narrative.md`
- Create: `day-1/block-c-roadmaps/templates/risk-register.md`

**Step 1: Write slides.md**

Marp deck (~15-18 slides):

1. **Title slide** — "Roadmaps, Bets, and Alignment" / Block C / 15:30-17:10
2. **Roadmaps are not Gantt charts** — the roadmap as a communication tool, not a project plan
3. **RICE prioritization** — Reach, Impact, Confidence, Effort applied to analytics projects
4. **North Star vs. Guardrails** — input metrics, output metrics, the metrics tree
5. **Communicating trade-offs** — "we can do X or Y, not both" — framing for Product/Eng
6. **The 2-page executive narrative** — structure: context, what we did, what we learned, what's next, what we need
7. **Risk registers** — identifying what could go wrong, mitigation strategies
8. **Activity Brief: 12-Month Roadmap** — build using RICE, time box (30 min)
9. **Activity Brief: Exec Narrative draft** — 2-page structure, time box (20 min)
10. **Red-team: Kill the Project** — pairs try to destroy each other's roadmap; find fatal flaws
11. **Debrief** — what survived the red team?
12. **Day 1 Checkpoint reminder** — submit Charter + Stakeholder Map + Roadmap Outline by 17:10

**Step 2: Write facilitator-notes.md**

**Step 3: Write templates (roadmap-rice.md, exec-narrative.md, risk-register.md)**

**Step 4: Run validation**

---

### Task 8: Block D — Growth & Performance

**Files:**
- Create: `day-2/block-d-growth/slides.md`
- Create: `day-2/block-d-growth/facilitator-notes.md`
- Create: `day-2/block-d-growth/templates/pgp.md`
- Create: `day-2/block-d-growth/templates/performance-summary.md`

**Step 1: Write slides.md**

Marp deck (~15-18 slides):

1. **Title slide** — "Growth & Performance" / Block D / 11:00-12:40
2. **Career ladders for analytics** — IC track vs. management track, what "senior" actually means
3. **The Personal Growth Plan** — what it is, why it matters, structure (strengths, gaps, actions, timeline)
4. **Feedback that lands** — SBI model (Situation-Behavior-Impact), radical candor quadrant
5. **Performance cycles** — annual review trap, continuous feedback, calibration sessions
6. **Writing calibration-ready summaries** — how to write about your people so the committee gets it right
7. **The ethical PIP** — when performance management goes wrong, how to do it with integrity
8. **Difficult conversations** — frameworks for delivering hard news, the COIN model
9. **Activity Brief: Draft a PGP** — for yourself or a fictional report (25 min)
10. **Activity Brief: Calibration summary** — write one for a fictional team member (20 min)
11. **Debrief** — what was hardest to write? why?
12. **Transition** — preview Block E

**Step 2: Write facilitator-notes.md**

**Step 3: Write templates (pgp.md, performance-summary.md)**

**Step 4: Run validation**

---

### Task 9: Block E — XFN, Vendor, IT & Data Infra

**Files:**
- Create: `day-2/block-e-infra-vendor/slides.md`
- Create: `day-2/block-e-infra-vendor/facilitator-notes.md`
- Create: `day-2/block-e-infra-vendor/templates/data-infra-blueprint.md`
- Create: `day-2/block-e-infra-vendor/templates/rfp-scoring-matrix.md`

**Step 1: Write slides.md**

Marp deck (~15-18 slides):

1. **Title slide** — "XFN, Vendor, IT & Data Infra" / Block E / 13:30-15:10
2. **Cross-functional interfaces** — Product, Eng, Design, Legal, Privacy — who needs what from analytics
3. **SLAs and contracts between teams** — what you owe them, what they owe you
4. **The small-org data infra blueprint** — Sources → Ingestion → Warehouse → Metrics → Governance → Observability
5. **Build vs. Buy** — decision framework, total cost of ownership, the hidden cost of "free"
6. **The modern data stack (pragmatic view)** — what actually matters at each company stage
7. **Working with IT and procurement** — speaking their language, security reviews, vendor management
8. **RFP and vendor scoring** — how to evaluate tools systematically
9. **Privacy and governance basics** — GDPR, data classification, retention policies
10. **Activity Brief: Data Infra One-Pager** — "Our next 6 months" for your case context (25 min)
11. **Activity Brief: RFP Scoring Matrix** — evaluate 3 tools for one need (20 min)
12. **Debrief** — what trade-offs did you make?
13. **Transition** — preview Block F (QBR simulation)

**Step 2: Write facilitator-notes.md**

**Step 3: Write templates (data-infra-blueprint.md, rfp-scoring-matrix.md)**

**Step 4: Run validation**

---

### Task 10: Block F — Leading Up & Across; QBR Simulation

**Files:**
- Create: `day-2/block-f-qbr-simulation/slides.md`
- Create: `day-2/block-f-qbr-simulation/facilitator-notes.md`
- Create: `day-2/block-f-qbr-simulation/templates/qbr-outline.md`
- Create: `day-2/block-f-qbr-simulation/templates/portfolio-checklist.md`

**Step 1: Write slides.md**

Marp deck (~12-15 slides):

1. **Title slide** — "Leading Up & Across; QBR Simulation" / Block F / 15:30-17:10
2. **Executive communication** — what execs care about, the pyramid principle, BLUF
3. **Decisions and risks** — escalation frameworks, the "disagree and commit" pattern
4. **Incident postmortems** — blameless culture, 5-whys for analytics failures
5. **Alignment across org sizes** — how your Manager OS adapts (small/medium/large)
6. **QBR Simulation Brief** — format, time per group, what the "exec panel" will evaluate
7. **QBR Evaluation Criteria** — clarity, business alignment, realism, handling of questions
8. **[QBR simulation happens here — no slides, just facilitation]**
9. **Debrief & feedback** — what worked, what to improve
10. **Portfolio checklist** — what's due, when, in what format
11. **Your next 90 days** — personal action plan prompt
12. **Close** — thank you, resources, office hours info

**Step 2: Write facilitator-notes.md**

Including detailed QBR simulation logistics: group size, timing per presentation, how to play the exec panel role, scoring approach.

**Step 3: Write templates (qbr-outline.md, portfolio-checklist.md)**

**Step 4: Run validation**

---

### Task 11: Assessment Materials

**Files:**
- Create: `assessment/grading-rubrics.md`
- Create: `assessment/peer-feedback-form.md`
- Create: `assessment/portfolio-checklist.md`

**Step 1: Write grading-rubrics.md**

One rubric per portfolio component, each with Excellent / Good / Needs Work descriptors:
- Participation & Preparedness (20%)
- Day 1 Checkpoint (10%) — pass/fail criteria
- Hiring Packet (20%)
- Roadmap + Exec Narrative (25%)
- Manager OS (15%)
- PGP + Performance Summary (5%)
- Peer Feedback Quality (5%)

**Step 2: Write peer-feedback-form.md**

Structured form with:
- What artifact are you reviewing?
- What works well? (specific)
- What's missing or unclear?
- One concrete suggestion for improvement
- Overall assessment (Ready / Almost / Needs significant revision)

**Step 3: Write portfolio-checklist.md**

Student-facing checklist with every required artifact, format requirements, and submission instructions.

**Step 4: Run validation**

---

### Task 12: Manager OS Reference

**Files:**
- Create: `resources/manager-os-reference.md`

**Step 1: Write the reference document**

A 2-3 page reference synthesizing the Manager OS concept:
- Cadences (daily standup, weekly 1:1, bi-weekly team meeting, monthly metrics review, quarterly planning)
- Artifacts (team charter, stakeholder map, RACI, decision log, roadmap, exec narrative)
- Decision hygiene (when to decide alone, when to consult, when to delegate)
- Adaptation notes for small/medium/large contexts

**Step 2: Run validation**

---

### Task 13: Final Validation & Summary

**Step 1: Run full validation**

```bash
python3 validate.py
```

Expected: ALL checks pass (green).

**Step 2: Generate a manifest**

List all files created with line counts and brief descriptions.

**Step 3: Summarize what was built**

Final report: file count, total content volume, what each block covers, any known gaps or TODOs for v2.
