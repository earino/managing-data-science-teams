# The Manager Operating System — Reference Guide

**ECBS5256 — Managing Data Science Teams | CEU Vienna**

---

## Introduction

Every computer needs an operating system — the invisible layer that schedules processes, manages resources, and ensures applications can do their real work without constantly reinventing the basics. The Manager Operating System (Manager OS) is the same idea applied to analytics leadership. It is the set of cadences, rituals, artifacts, and decision-making practices that run in the background of your management practice, creating predictability for your team and freeing everyone — including you — to focus on the work that actually matters.

A well-designed Manager OS removes ambiguity. Your team knows when they will hear from you, how decisions get made, and where to find the information they need. Stakeholders know what to expect and when. You, as the manager, stop relying on heroics and memory, replacing them with systems that scale. The absence of a Manager OS is not freedom — it is chaos that masquerades as flexibility.

This document provides the reference architecture. It describes the full set of cadences, rituals, artifacts, and decision frameworks available to you. Your job is not to adopt every element wholesale. It is to adapt the OS to your case context, company size, and team maturity. A three-person startup analytics team and a fifty-person data organization at a multinational need very different configurations of the same underlying components.

---

## Cadences

| Cadence | Activities | Approx. Time |
|---|---|---|
| **Daily** | Async standup (optional, via Slack/Teams); scan dashboards and alerts; be available for questions and unblocking | ~15 min |
| **Weekly** | 1:1s with each direct report (30 min each); team sync meeting (45 min); stakeholder check-in (ad hoc); review and update the decision log | 3--5 hours |
| **Bi-weekly / Monthly** | Metrics review with team; retrospective (what is working, what is not); cross-functional sync with Product and Engineering | 2--3 hours |
| **Quarterly** | Planning cycle (roadmap refresh, RICE re-scoring); calibration prep; executive QBR preparation; team health check | 1--2 days |
| **Annually** | Career conversations; compensation review prep; team structure review; budget planning | 1--2 weeks (spread out) |

---

## Rituals and Their Purpose

### 1:1s

| | |
|---|---|
| **Purpose** | Coaching, unblocking, career growth. This is *their* meeting, not yours. |
| **Format** | Their agenda first, your agenda second. Never let this become a status update — that is what async tools are for. |
| **Frequency** | Weekly (new reports or struggling ICs) to bi-weekly (senior, autonomous reports). |
| **Duration** | 30 minutes. |
| **Attendees** | You and one direct report. |
| **Artifacts** | Running 1:1 doc (shared); action items; notes for PGP updates. |

### Team Sync

| | |
|---|---|
| **Purpose** | Coordination, context sharing, celebration. |
| **Format** | Wins (2 min) -> Blockers (5 min) -> Announcements and context (10 min) -> Open floor. |
| **Frequency** | Weekly. |
| **Duration** | 30--45 minutes. Hard stop. |
| **Attendees** | Full team. |
| **Artifacts** | Meeting notes with action items; updated blockers list. |

### Metrics Review

| | |
|---|---|
| **Purpose** | Understand team impact, spot trends, connect work to outcomes. |
| **Format** | Dashboard walkthrough; discuss anomalies and surprising numbers; assign action items for investigation or follow-up. |
| **Frequency** | Bi-weekly or monthly. |
| **Duration** | 45--60 minutes. |
| **Attendees** | Full team, optionally key stakeholders. |
| **Artifacts** | Annotated dashboard snapshots; action items; trend notes for QBR prep. |

### Retrospective

| | |
|---|---|
| **Purpose** | Continuous improvement. Learn from what happened, not who to blame. |
| **Format** | Three columns: what went well, what did not go well, what to change. Blameless. Vote on top items, assign owners for changes. |
| **Frequency** | Bi-weekly or monthly; also after major project completions. |
| **Duration** | 45--60 minutes. |
| **Attendees** | Full team. |
| **Artifacts** | Retro summary; committed action items with owners and deadlines. |

### Planning

| | |
|---|---|
| **Purpose** | Align on priorities, allocate resources, build the narrative for stakeholders. |
| **Format** | RICE scoring of candidate projects; roadmap refresh; draft executive narrative; identify dependencies and risks. |
| **Frequency** | Quarterly. |
| **Duration** | Half-day to full-day session. |
| **Attendees** | Manager, tech leads, senior ICs. Stakeholder input gathered beforehand. |
| **Artifacts** | Updated roadmap; RICE scores; executive narrative draft; resource allocation plan. |

### QBR (Quarterly Business Review)

| | |
|---|---|
| **Purpose** | Executive alignment and accountability. Show impact, surface risks, make asks. |
| **Format** | Structured presentation: key metrics and trends -> wins and delivered impact -> risks and mitigations -> asks (headcount, budget, access, decisions). |
| **Frequency** | Quarterly. |
| **Duration** | 30--60 minutes (presentation); several hours of prep. |
| **Attendees** | You, your leadership chain, key cross-functional partners. |
| **Artifacts** | QBR deck or memo; metrics appendix; recorded asks and commitments. |

---

## Artifacts

| Artifact | What It Is | When to Create / Update | Primary Audience |
|---|---|---|---|
| **Team Charter** | Mission, scope, principles, and boundaries of your team | At team formation; revisit quarterly | Team, stakeholders, new hires |
| **Stakeholder Map** | Visual map of who depends on you, who you depend on, influence vs. authority | At team formation; update quarterly or after reorgs | You, your manager |
| **RACI Matrix** | Responsible, Accountable, Consulted, Informed for key processes | When responsibilities are unclear; update as roles change | Team, cross-functional partners |
| **Decision Log** | Record of significant decisions: context, options considered, rationale, outcome | Ongoing — every significant decision | Team, future you, successors |
| **Roadmap** | Prioritized view of planned work across time horizons (now, next, later) | Quarterly refresh; minor updates as needed | Stakeholders, team, executives |
| **Executive Narrative** | One-page story of what your team does, why it matters, and what it needs | Quarterly, aligned with QBR | Executives, skip-level leadership |
| **PGP (Personal Growth Plan)** | Individual development goals and progress for each direct report | Created together in career conversations; reviewed in 1:1s | Each direct report, you, HR |
| **Performance Summaries** | Written assessment of each report's performance for the review period | Review cycle (typically semi-annual or annual) | Report, HR, calibration panels |
| **Risk Register** | Known risks to team delivery, with likelihood, impact, and mitigations | Ongoing; reviewed in planning and QBR prep | You, your manager, stakeholders |
| **Data Infra Blueprint** | Architecture overview of your data stack: sources, pipelines, storage, serving | At team formation; update when infra changes materially | Team, engineering partners, new hires |

---

## Decision Hygiene

### Type 1 vs. Type 2 Decisions

- **Type 1 (irreversible or very costly to reverse):** Hiring, firing, major vendor commitments, org restructuring, large budget allocations. *Decide slowly.* Gather input. Sleep on it. Document the reasoning.
- **Type 2 (reversible, low cost to undo):** Tool choices, process experiments, project prioritization within a quarter, meeting format changes. *Decide fast.* Run the experiment. Iterate based on data.

Most decisions are Type 2. The most common management failure is treating every decision like Type 1.

### Decision Memo Format

Keep it to one page:

1. **Context** — What is the situation? Why does a decision need to be made now?
2. **Options** — What are the realistic alternatives? (At least two, including "do nothing.")
3. **Recommendation** — What do you recommend and why?
4. **Risks** — What could go wrong? What are the mitigations?

### When to Decide Alone, Consult, or Delegate

Use the "who has the information?" test:

- **Decide alone** when you have the information and the decision is within your authority.
- **Consult then decide** when others have critical information or the decision affects them significantly. Gather input, but you own the call.
- **Delegate** when someone on your team has better information, the decision is within their scope, and the cost of a suboptimal choice is low. Make the delegation explicit: "This is your call."

---

## Adapting by Company Size

| | Small (0 -> 1) | Medium (1 -> N) | Large (N -> Scale) |
|---|---|---|---|
| **Cadences** | Informal. Lean toward over-communication — the team is small enough that a missed signal can derail a week. | Formalize. Written agendas, documented decisions, consistent schedule. Trust erodes fast without structure. | Structured and protected. Your calendar *is* your strategy — what you attend signals what matters. |
| **Artifacts** | Minimal. A team charter and a roadmap are enough. Over-documenting at this stage is waste. | Full set. Especially invest in the stakeholder map and RACI — ambiguity about roles is the #1 scaling pain. | Governance-heavy. Everything documented for audit, compliance, and organizational memory. |
| **Decision-making** | Fast. You are often the decider and the executor. Bias toward action. | Delegate more. Establish clear decision rights. Your job shifts from making decisions to designing the decision-making system. | Influence without authority. Navigate politics. Build coalitions. Decisions happen in hallways and pre-meetings. |
| **Key challenge** | Doing the IC work AND the management work simultaneously without burning out on either. | Scaling yourself through others. Letting go of the work you used to do with your own hands. | Alignment across many stakeholders with competing priorities and different incentive structures. |

---

## Recommended Reading

- **Andy Grove, *High Output Management*** — The original Manager OS. Grove's concept of "managerial leverage" is the intellectual foundation for everything in this document. Start here.

- **Camille Fournier, *The Manager's Path*** — A practical guide to each stage of the management career ladder, from tech lead to CTO. Especially strong on the transition from IC to manager.

- **Will Larson, *An Elegant Puzzle*** — Systems thinking applied to engineering and analytics leadership. Excellent on sizing teams, managing technical debt, and organizational design.

- **Skelton and Pais, *Team Topologies*** — A framework for how to structure teams for fast flow of delivery. Useful for thinking about team boundaries, interaction modes, and cognitive load.

- **Forsgren, Humble, and Kim, *Accelerate*** — The research behind measuring delivery performance (the DORA metrics). Gives you a rigorous, evidence-based vocabulary for team effectiveness.

---

*This is a reference document for ECBS5256. Adapt the components to your case context — your Manager OS should reflect the team, company, and constraints you are designing for, not a generic template.*
