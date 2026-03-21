---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 2 – Block E"
---
<!-- ⏱ Expected: 13:30 (min 0/100) -->
<!-- _class: title -->

# Block E: Infrastructure & Cross-Functional Interfaces

**Day 2 | 13:30–15:10 (100 minutes)**

---

<!-- ⏱ Expected: 13:30 (min 0/100) -->
## Learning Outcomes

By the end of this block you will be able to:
- Map cross-functional interfaces and document bidirectional SLAs
- Understand the canonical data stack and ask the right questions about each layer
- Apply a build-vs-buy framework grounded in Total Cost of Ownership
- Sketch a data infrastructure plan for your case context

<!-- Talk track: This is the most technical block in the course, but it's technical in the way a manager needs to be technical. You don't need to configure a Snowflake instance. You need to know what questions to ask, what trade-offs exist, and how to work with IT, Legal, and Engineering to make infrastructure decisions that your team can live with for the next two years. -->

---

<!-- ⏱ Expected: 13:30 (min 0/100) -->
## Shifting Gears

This morning was intense — feedback, calibration, hard conversations.

**Take 90 seconds now:**
Write down one thing from this morning you want to remember. Then set it aside.

We're moving from the **emotional work** of growing people to the **practical work** of infrastructure and cross-functional relationships. Different energy, same importance.

<!-- Talk track: Before we dive in, let's acknowledge the shift. This morning was heavy. You practiced giving uncomfortable feedback, you debated performance ratings with real stakes, and some of those conversations hit close to home. Take 90 seconds. Write down one thing from this morning that you want to carry forward. Then set it aside. We're shifting gears to something concrete and practical — infrastructure, tools, and the teams you depend on to get work done. -->

---

<!-- ⏱ Expected: 13:32 (min 2/100) | Why Infrastructure Matters (3 min) -->
## Why Infrastructure Matters for Analytics Managers

You don't need to be a data engineer — but you need to understand the stack well enough to **make decisions**.

- Infrastructure choices are **2–3 year commitments** — the wrong warehouse compounds into months of lost productivity
- Your analysts can only analyze what they can **access**. If the infrastructure is broken, their skills don't matter
- **The manager's job:** You're not configuring Snowflake. You're deciding *whether* to use it, *how much* to spend, and *who* owns it when it breaks

<!-- Talk track: These are not reversible decisions. When you pick a data warehouse, you're committing your team's workflows, your SQL dialect, and your cost structure for two to three years. Here's a scenario I've seen: a team of brilliant analysts, all with PhDs, completely blocked because their data pipeline broke over a weekend and nobody knew how to fix it. Three days of zero output. Your job is not to fix the pipeline — it's to make sure the right decisions were made so that doesn't happen. -->

---

<!-- ⏱ Expected: 13:36 (min 6/100) | XFN Universe + Failure Modes (6 min) -->
<!-- _class: compact -->
## Your Cross-Functional Universe

Analytics doesn't exist in a vacuum. Your key interfaces:

| Interface | What they care about |
|---|---|
| **Product** | What to measure, experiment results |
| **Engineering** | How to collect data, system reliability |
| **Legal / Privacy** | What you can store, for how long |
| **Finance** | What it all costs |
| **IT / Infra** | Where it runs, who has access |

**Mental model:** Analytics sits at the center of a hub-and-spoke. Every spoke is a relationship you must actively manage.

<!-- Talk track: Here's a number that surprises most new analytics managers: you will spend thirty to forty percent of your time on cross-functional work. Not analyzing data. Not building dashboards. Managing relationships with other teams. You depend on Engineering to instrument events. You depend on IT to provision access. You depend on Legal to clear your data usage. And here's the thing — if any one of these relationships is broken, your team stalls. Not "slows down." Stalls. Let me show you what that looks like. -->

---

<!-- ⏱ Expected: 13:36 (min 6/100) | XFN Failure Modes -->
## The XFN Failure Modes

What actually goes wrong when cross-functional relationships aren't managed:

- **Engineering changes a schema** and breaks your pipeline at 2 AM. Your morning dashboards are wrong. The CEO asks questions before you know there's a problem.
- **Legal blocks your new analytics tool** three months into implementation. You've already migrated data and trained the team.
- **Finance doesn't approve your vendor renewal.** Dashboards go dark.
- **Product launches a feature without instrumentation.** The VP asks "how is it performing?" and you have no data.

Each failure mode maps to a **preventable relationship gap**. That's what SLAs are for.

<!-- Talk track: Let me make this concrete with real failure stories. Story one: Engineering ships a database migration over the weekend. They rename three columns. Your pipeline fails at 2 AM. Your morning dashboards are blank. The CEO pulls them up at 8 AM and asks what's going on — and you find out from the CEO, not from Engineering. Story two: you spend three months evaluating and implementing a new analytics tool. Then Legal tells you the data processing agreement doesn't meet GDPR. Three months of work, unwound. Story three: Finance doesn't renew your BI tool license because nobody flagged the budget cycle deadline. Dashboards go dark. Every one of these is preventable with a written SLA and a regular check-in. -->

---

<!-- ⏱ Expected: 13:42 (min 12/100) | Bidirectional SLAs (6 min) -->
## What Each Team Needs — It's Bidirectional

| Team | They need from you | You need from them |
|---|---|---|
| **Product** | Metrics definitions, experiment results | Clear, prioritized business questions |
| **Engineering** | Data contracts, schema documentation | Advance notice of schema changes |
| **Legal** | Data inventories, consent tracking | Timely privacy reviews |
| **Finance** | Cost attribution, ROI analysis | Reasonable budget cycles |
| **IT** | Security compliance docs | Procurement timelines, cloud access |

<!-- Talk track: Notice the pattern — every relationship is bidirectional. You owe them things and they owe you things. Most new managers only think about what they need: "Engineering should tell me about schema changes." But Engineering needs things from you too — data contracts, documentation, SLAs for query load on their systems. If you only make demands without offering commitments, the relationship dies. The managers who do this well think in trades, not requests. -->

---

<!-- ⏱ Expected: 13:42 (min 12/100) | SLA Template -->
## Building Bidirectional SLAs — Template

**Template:**

> **Analytics will** provide [deliverable X] within [Y timeframe].
> **[Partner team] will** provide [deliverable Z] within [W timeframe].
> **Escalation path:** [name/role] if SLA is missed.
> **Review cadence:** Monthly sync to assess and adjust.

SLAs work when **both sides see value**. If it feels one-sided, it won't survive the first quarter.

<!-- Talk track: Here's a practical template. Four lines — that's it. What you'll provide and by when. What they'll provide and by when. Who to escalate to when someone misses — and you need a real name here, not "management." And how often you review the agreement. Start with your most critical relationship — usually Engineering — and get one SLA working well before expanding to others. The key: both sides need to see value. If the SLA only benefits you, the other team will ignore it within a month. -->

---

<!-- ⏱ Expected: 13:42 (min 12/100) | SLA Example -->
## Building Bidirectional SLAs — Example

**Analytics ↔ Engineering SLA:**

> Analytics will review schema change impact assessments within **3 business days**.
> Engineering will notify analytics **2 sprints before** any schema change to tracked events.
> Escalation: VP Engineering and Head of Analytics.
> Review: First Monday of each month.

Both sides get something: Engineering gets fast turnaround on impact assessments, and you get advance notice of changes.

<!-- Talk track: Here's a concrete example for the Engineering relationship. You commit to reviewing schema change impacts within three business days — that's fast, and Engineering values fast turnaround. They commit to notifying you two sprints before any schema change — that's the advance notice you need to update your pipelines before anything breaks. Both sides get something. And when someone misses the SLA? You don't send a passive-aggressive Slack message. You escalate to the names on the document. Draft one of these for each key partner. It takes thirty minutes and saves hundreds of hours of fire-fighting. -->

---

<!-- ⏱ Expected: 13:48 (min 18/100) | Blueprint + Architecture (6 min) -->
## The Data Infrastructure Blueprint

The canonical flow — every modern data stack follows this pattern:

**Sources** --> **Ingestion** --> **Storage** --> **Transform** --> **Semantic Layer** --> **Visualization**

With cross-cutting concerns at every layer:

- **Governance:** Who owns what? Who can access what?
- **Observability:** Is it working? How do you know?
- **Cost management:** What does each layer cost?

**Anchor this slide.** We'll come back to it throughout the block.

<!-- Talk track: Let me walk you through this with a concrete example. Your app generates a click event when a user signs up. That event flows through ingestion — something like Fivetran pulls it into your warehouse. Storage is where it lands — BigQuery, Snowflake. Transform is where dbt cleans it up and joins it with other tables. The semantic layer is where you define what "active user" means so the whole company uses the same number. And visualization is the Looker dashboard your VP checks every Monday. At every layer, you're asking: is it working, what happens when it breaks, and what does it cost? This flow is the mental model for the rest of this block. -->

---

<!-- ⏱ Expected: 13:48 (min 18/100) | Reading Architecture Diagrams -->
## Reading an Architecture Diagram

| Layer | What it does (plain English) | Key question |
|---|---|---|
| **Sources** | Where data originates (app, APIs, files) | "Capturing everything we need?" |
| **Ingestion** | Moves data from sources to storage | "How fresh? Minutes, hours, days?" |
| **Storage** | The central repository (warehouse) | "Cost? Can it scale?" |
| **Transform** | Cleans raw data into usable tables | "How do we verify correctness?" |
| **Semantic Layer** | Defines metrics so everyone agrees | "One definition of 'revenue'?" |
| **Visualization** | Dashboards end users see | "Can stakeholders self-serve?" |

<!-- Talk track: Each layer does one thing. Even if you've built models in Python and run complex SQL, infrastructure architecture is a different vocabulary. This table translates it. The key questions in the right column are what you ask as a manager — you don't need to know how ingestion works, you need to know how fresh the data is. -->

---

<!-- ⏱ Expected: 13:54 (min 24/100) | Build vs. Buy (8 min) -->
## Build vs. Buy — The Framework

**Four questions in order:**

1. **Is this a core differentiator?** If yes: build.
   - Your recommendation algorithm? Build. Your data warehouse? Buy.

2. **Is this commodity infrastructure?** If yes: buy.
   - Ingestion, storage, BI tooling — these are solved problems.

3. **Do you have the team to maintain it?** If no: buy.
   - "Free" open source costs your engineers' time. Forever.

4. **What's the Total Cost of Ownership?**
   - License + implementation + training + maintenance + **opportunity cost**

**Default to buy** for infrastructure. Default to build for business logic.

<!-- Talk track: Build versus buy is one of the most consequential decisions you'll make. The rule of thumb: default to buy for infrastructure, default to build for business logic. Infrastructure is commodity. Business logic is where your team adds unique value. And when you decide to buy — involve IT from day one, not after you've already started a trial. Procurement takes two to six times longer than you expect. If you need a tool by Q3, start the process in Q1. One more thing: AI tools are a new line item in your stack. API costs for LLMs, AI coding assistants, model serving — these are real infrastructure decisions now, and the same build-vs-buy framework applies. -->

---

<!-- ⏱ Expected: 13:54 (min 24/100) | Hidden Costs -->
<!-- _class: compact -->
## The Hidden Costs of "Free"

Open-source tools have **real costs** — your engineers' time.

**Airflow (open-source) vs. managed alternatives:**

| Cost component | Self-hosted Airflow | Managed (e.g., Astronomer) |
|---|---|---|
| License | $0 | ~$300–1,200/mo |
| Engineer setup | 40–80 hours | 4–8 hours |
| Monthly maintenance | 8–16 hours/mo | ~0 hours/mo |
| Upgrades (annual) | 20–40 hours | Included |
| **Annual engineer cost** | **~$30K–50K in loaded salary** | **~$4K–14K in subscription** |

**When "free" actually costs more than "paid":** almost always, unless you have a dedicated platform team.

The real question: what does your team **not build** while maintaining this tool?

<!-- Talk track: This is the slide I wish someone had shown me earlier in my career. Open source is not free. Add it up: thirty to fifty thousand dollars a year in engineer salary to run a "free" tool. Versus four to fourteen thousand for a managed service. And here's the real kicker — it's not just the money. It's what your team doesn't build while they're maintaining Airflow. Every hour your data engineer spends debugging a scheduler crash is an hour they're not building the pipeline your PM is waiting for. That opportunity cost is the hidden killer. -->

---

<!-- ⏱ Expected: 14:02 (min 32/100) | Pair discussion (2 min) -->
## Quick Check: Build or Buy?

**2 minutes — turn to your neighbor:**

Think about your case context. Name **one tool or capability** your team needs. Would you build it or buy it? Why?

Apply the four questions. Be ready to share your answer and your reasoning.

<!-- Talk track: Before we move on, let's apply what we just covered. Turn to the person next to you. Think about your case context — name one tool or capability your team needs. Would you build it or buy it? Use the four questions. You have two minutes. Go. -->

---

<!-- ⏱ Expected: 14:04 (min 34/100) | Stack Progression -->
## How Stacks Evolve — The Progression Story

Every analytics stack follows the same arc:

1. **Small (Seed/A):** Get trusted numbers, fast. Buy everything. $500–2K/month.
2. **Medium (Series B/C):** Self-serve metrics, experimentation, observability. You start making real build-vs-buy decisions. $10K–30K/month.
3. **Large (Enterprise):** Domain autonomy, ML at scale, regulatory compliance. Your challenge isn't the tools — it's governance and organizational alignment. $100K+/month.

**The pattern:** You start scrappy. You add observability when you get burned by bad data. You add governance when you get audited. You never build the "right" architecture on day one — you evolve toward it.

<!-- Talk track: Before I show you specific tool choices, here's the story that every data stack lives through. You start scrappy — a warehouse, a BI tool, a spreadsheet for governance. That's fine. Then you get burned: a dashboard shows wrong numbers, the CEO asks questions, and you realize you need observability. So you add it. Then you get audited, or a regulator asks about PII, and you realize you need governance. So you add it. Nobody builds the right architecture on day one. You evolve toward it. Let me show you what each stage looks like. -->

---

<!-- ⏱ Expected: 14:07 (min 37/100) | Stack by Size — Small -->
<!-- _class: compact -->
## Small Org Stack (0 to 1)

**Goal:** Trusted numbers, fast. Don't over-engineer.

| Layer | Tool | Why |
|---|---|---|
| **Sources** | Product DB + basic events | Start with what you have |
| **Ingestion** | Fivetran or Airbyte | Managed connectors; don't build this |
| **Storage** | BigQuery or Snowflake (free tier) | Start small, scale later |
| **Transform** | dbt (Core or Cloud) | SQL-based; version-controlled; testable |
| **Viz** | Metabase or Preset | Open-source options exist; low cost |
| **Governance** | Naming conventions + a spreadsheet | Seriously. This is enough to start. |

**Monthly cost:** $500–2,000. **Skip everything else** — data catalog, ML platform, feature store. Add complexity when you feel **real pain**, not anticipated pain.

<!-- Talk track: Now let's see what these decisions look like in practice. Keep your build-vs-buy lens on. If you're in the small startup case context, this is your stack. Notice: almost everything here is "buy." Total cost: under two thousand a month. And here's the discipline part — skip everything not on this list. No data catalog for fifty tables. No ML platform when you don't have models in production. Add complexity when you feel real pain, not anticipated pain. -->

---

<!-- ⏱ Expected: 14:07 (min 37/100) | Stack by Size — Medium -->
<!-- _class: compact -->
## Medium Org Stack (1 to N)

**Goal:** Self-serve metrics, experimentation, data trust at scale. $10K–30K/month.

Add to the small stack:

| Addition | Why now |
|---|---|
| Event platform (Segment/RudderStack) | Structured event collection; identity resolution |
| Experimentation (Statsig/Eppo) | Rigorous A/B testing, not spreadsheet math |
| Semantic layer (dbt metrics/Cube) | Single source of truth for metric definitions |
| Observability (Monte Carlo/Elementary) | Know when data breaks before your stakeholders do |

**Governance:** Formal data owners. Published SLAs. Access controls.

<!-- Talk track: At medium scale, the critical addition is observability. Without it, here's what happens: your dashboard shows stale data for six hours. Nobody on your team notices. The CEO pulls it up in a meeting and says "why does this say yesterday's numbers?" You find out from the CEO. With observability — Monte Carlo, Elementary — you get an alert at 6 AM saying "data freshness SLA violated." You fix it before anyone notices. That single tool changes your relationship with the rest of the company. Monthly cost jumps to ten to thirty thousand, but one prevented incident pays for it. -->

---

<!-- ⏱ Expected: 14:07 (min 37/100) | Stack by Size — Large -->
<!-- _class: compact -->
## Large Org Stack (N to Scale)

**Goal:** Domain autonomy, ML at scale, regulatory compliance. $100K+/month.

Add to the medium stack:

| Addition | Why now |
|---|---|
| Data mesh / domain ownership | Each domain owns its data products; central team sets standards |
| ML platform (MLflow/SageMaker/Vertex) | Model training, versioning, deployment at scale |
| Model governance (cards, bias audits) | Regulatory and ethical requirements |
| Cost management (Kubecost, billing dashboards) | $100K+/mo demands accountability |

**Your challenge isn't the tools — it's governance and organizational alignment.**

<!-- Talk track: At enterprise scale, the challenges are fundamentally different. You're not trying to get trusted numbers — you're trying to maintain trust across dozens of teams, petabytes of data, and strict regulatory requirements. Data mesh means each business domain owns its data products — the central team sets standards but doesn't own every pipeline. You need model governance because regulators will ask. And you need cost management because at a hundred thousand a month, someone in finance is going to want accountability. For those of you in the large enterprise case context: your challenge in the activity isn't "what tools do I pick?" It's "what can I actually get approved in six months given procurement, legal, and budget cycles?" -->

---

<!-- ⏱ Expected: 14:04 (min 34/100) | The Migration Trap -->
## The Migration Trap

What happens when you outgrow your stack:

1. **Spreadsheets to a real warehouse** — Painful but straightforward. Budget 2–3 months.
2. **Warehouse to warehouse** — Every query, dashboard, and integration rebuilt. Budget 6–12 months.
3. **"We built it ourselves and now we can't maintain it"** — The custom pipeline one engineer built, who then left. Nobody understands it.

**Key insight:** Plan for the **next** migration when choosing the current tool. Ask: "How hard will it be to leave this vendor in 3 years?"

Avoid proprietary lock-in where you can. Use standard SQL. Use standard file formats.

<!-- Talk track: Let me talk about what happens when you outgrow your stack. Story three is the scariest: a brilliant engineer builds a custom ingestion pipeline. Beautiful code. Handles edge cases nobody else thought of. Then that engineer leaves. Now nobody understands how it works, it breaks every few weeks, and nobody can fix it properly. You're stuck maintaining a system you can't modify and can't replace without a six-month migration project. The lesson: when you choose a tool today, ask yourself how hard it will be to leave it in three years. Use standard SQL. Use standard file formats. Make migration a design criterion, not an afterthought. -->

---

<!-- ⏱ Expected: 14:13 (min 43/100) | What You Inherit (3 min) -->
## Your First Month: What You Inherit

You will almost never build a stack from scratch. You will **inherit** one. Before proposing changes, audit what exists:

- **What are we paying for?** List every tool with its monthly cost and contract renewal date
- **Who owns each pipeline?** If the answer is "nobody" or "the person who left," that's your first risk
- **What breaks most often?** Ask the team — they know. The answer tells you where to invest first
- **What's undocumented?** Undocumented pipelines are the ones that break at 2 AM with no runbook

**The rule:** Spend 30 days understanding before spending 30 minutes proposing.

<!-- Talk track: One more thing before the activity. You will almost never build a stack from scratch. You'll inherit one — and it will be messy. Before you propose any changes, spend your first month auditing what exists. What tools are we paying for? Who owns each pipeline? What breaks most? What's undocumented? The undocumented pipelines are the ones that break at 2 AM with no runbook. Spend thirty days understanding before you spend thirty minutes proposing. This connects directly to the First 90 Days framework you'll see in Block F. -->

---

<!-- ⏱ Expected: 14:16 (min 46/100) | Privacy & Governance Basics (3 min) -->
## Privacy & Governance Basics

**GDPR essentials for analytics managers** (you're at CEU Vienna — this is your legal reality):

| Concept | What it means for you |
|---|---|
| **Lawful basis** | You need a legal reason to process personal data |
| **Data minimization** | Collect only what you need. "We might need it someday" is not a reason |
| **Right to erasure** | Users can ask you to delete their data. Your pipeline must support this |

**Data classification — know your tiers:**
- **Public** → blog metrics, benchmarks | **Internal** → aggregate dashboards
- **Confidential** → user-level data, financials | **Restricted** → PII, health, payment data

<!-- Talk track: Since you're studying in Vienna, this isn't optional knowledge — it's your legal reality. GDPR gives you three concepts to internalize. Lawful basis: you need a legal reason to process personal data. Data minimization: collect only what you need for a specific purpose. Right to erasure: if a user asks to be deleted, your pipeline needs to handle it. And classify your data — know what's public, what's internal, what's confidential, and what's restricted. Every table in your warehouse should have a retention policy. "Keep forever" is not a policy — it's a liability. -->

---

<!-- ⏱ Expected: 14:19 (min 49/100) | Activity: Data Infra Decision Brief (20 min) -->
<!-- _class: divider -->

## Activity: Data Infra Decision Brief

## 20 Minutes

<!-- Talk track: Time for hands-on work. This is focused and fast — three items, twenty minutes. -->

---

<!-- ⏱ Expected: 14:19 (min 49/100) | Activity -->
## Activity: Data Infra Decision Brief

**Time: 20 minutes | Working individually.**

1. **Current state** (5 min) — What exists today? Biggest pain point?

2. **AI impact** (8 min) — How does AI change your case context? Pick one lens:
   - **Infrastructure:** AI tools — build or buy? At what cost?
   - **People:** How do hiring criteria or team norms change?
   - **Governance:** What new risks or policies do you need?

3. **VP proposal** (7 min) — One paragraph, BLUF: What do you need? Why? Cost? Consequence of no?

<!-- Talk track: Three items, twenty minutes. First: current state — what exists and what's the biggest pain point. Five minutes. Second: how does AI change your case context? Pick the lens that feels most urgent — infrastructure, people, or governance. No wrong answer — the choice itself tells you something about your priorities. Eight minutes. Third: write a one-paragraph proposal to your VP. Lead with what you need. That's BLUF — you practiced it in Day 1. Seven minutes. Go. -->

---

<!-- ⏱ Expected: 14:19 (min 49/100) | Activity Example -->
## Example: What a Good Decision Brief Looks Like

**Current state:** "We run on BigQuery + dbt + Metabase. No observability. Dashboards broke twice last month — stakeholders found out before we did."

**AI impact (governance lens):** "Three analysts use Claude daily for code and analysis drafts. No policy exists. Last week an analyst pasted customer churn data including email addresses into a prompt. We need an AI usage policy before someone pastes payment data."

**VP proposal:** "We need two things: Monte Carlo for data observability ($1,500/month) and an approved AI usage policy (staff time only). Without observability, we'll keep getting surprised by broken dashboards. Without the AI policy, one analyst's mistake becomes a GDPR incident."

<!-- Talk track: Here's what a good one looks like. Notice the current state is one sentence — not an architecture diagram. The AI impact picks a specific lens and names a specific incident. And the VP proposal leads with what's needed, quantifies the cost, and names the consequence of no. That's BLUF. Aim for this level of specificity. -->

---

<!-- ⏱ Expected: 14:39 (min 69/100) | Debrief + Share-Out (15 min) -->
## Debrief: Share Your VP Proposal

**Share-out:** 2-3 volunteers read their VP proposal aloud (60 sec each).
- Is the BLUF clear? Would you fund it?

**Discussion:** What AI lens did you pick? What made you choose it?

**Key insight:** The "right" answer depends on your constraints. **The framework is the answer.**

_Portfolio connection: Data Infrastructure Blueprint and RFP Scoring Matrix are optional artifacts in `resources/`._

<!-- Talk track: Let's hear some proposals. Who wants to go first? Read your VP paragraph — sixty seconds. Class: is the BLUF clear? Would you fund it? After two or three, let's talk AI lenses. Who picked infrastructure? Governance? What made you choose? Notice how case context drove that decision. That's the real lesson — and it's exactly the skill Block F formalizes. -->

---

<!-- ⏱ Expected: 14:54 (min 84/100) | Transition -->
<!-- _class: divider -->

## Up Next: Block F

## Leading Up & Executive Communication
### 15:30–17:10

<!-- Talk track: That wraps Block E. After the break, Block F is about communicating upward — executive communication, handling failure, and your first 90 days as a manager. We'll also cover the async QBR — your capstone deliverable. See you at 3:30. -->

---

<!-- ⏱ Expected: 14:54 (min 84/100) | Transition -->
## Transition to Block F

**After break: Block F — Leading Up & Executive Communication (15:30–17:10)**

Executive communication frameworks, a discussion on communicating failure, your first 90 days as a manager, and the async QBR briefing.

> **During the break, think about:** What's the hardest thing you'd have to communicate to an executive in your case context?

See you at 15:30.

<!-- Talk track: We're taking a break. When you come back, Block F is about leadership communication — the Pyramid Principle, communicating failure, your first 90 days, and we'll brief you on the async QBR that's your capstone deliverable. During the break, think about the hardest thing you'd have to tell an executive in your case context. See you at 3:30. -->
