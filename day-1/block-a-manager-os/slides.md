---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 1 – Block A"
---
<!-- ⏱ Expected: 11:00 (min 0/100) -->
<!-- _class: title -->

# The Manager's Operating System

## Day 1 — Block A | 11:00–12:40

<!-- Talk track: Welcome to Managing Data Science Teams. I'm excited to spend these two days with you. This opening block is about the operating system you'll run as a manager — the repeatable patterns that make your team predictable, trustworthy, and effective. By the end of this session, you'll have two concrete artifacts: a Team Charter and a Stakeholder Map. Let's get started. -->

---

<!-- ⏱ Expected: 11:00 (min 0/100) -->
## Learning Outcomes

By the end of this block you will be able to:
- Construct a Manager OS with cadences, rituals, artifacts, and decision hygiene
- Draft a Team Charter anchored to your case context
- Map stakeholders on a Power/Interest grid
- Apply RACI to common analytics team decisions

<!-- Talk track: Here's what we're building toward in this block. Four concrete outcomes — and by the end, you'll have artifacts for each one. -->

---

<!-- ⏱ Expected: 11:00 (min 0/100) -->
## Welcome & Course Overview

**Your instructor:** Eduardo Ariño de la Rubia, Professor of Practice at CEU

**What this 2-day intensive covers:**
- Day 1: Manager OS, Hiring & Team Formation, Roadmaps & Alignment
- Day 2: Growth & Performance, Infrastructure & Cross-Functional Interfaces, Leading Up & Executive Communication

**What makes this course different:**
- **Workshop-driven** — you will build, not just listen
- You leave with a **portfolio of real artifacts**: charters, stakeholder maps, hiring rubrics, roadmaps, performance frameworks
- Every artifact is anchored to a realistic case context that YOU choose

<!-- Talk track: Let me introduce myself. I'm Eduardo Ariño de la Rubia, and I'm a Professor of Practice here at CEU. My background is in building and leading analytics and data science teams. This course is two days, and it is intense — the full lifecycle of analytics management. But here's what's different: this is not a lecture course. You're going to build things. By the end of Day 2, you'll have a portfolio of management artifacts that you could actually use on the job Monday morning. -->

---

<!-- ⏱ Expected: 11:05 (min 5/100) -->
## Why This Course Exists

**The problem:** Analytics managers are almost always promoted from IC roles with **zero management training**. You were the best analyst, so now you manage analysts — but these are completely different jobs.

**The cost of bad management in analytics:**
- **Talent flight** — your best people leave because they feel unseen or undirected
- **Lost credibility** — the team becomes the "dashboard team" instead of a strategic partner
- **Misaligned priorities** — you build what the loudest stakeholder wants, not what matters
- **Burnout** — without structure, everything is urgent and nothing is planned

Management is a **learnable craft**, not an innate talent.

<!-- Talk track: So why does this course exist? The analytics industry has a management problem. You're a great analyst, and then someone says "congratulations, you're now managing five people." Nobody teaches you how. The cost of getting it wrong is enormous — talent flight, lost credibility, misaligned priorities, burnout. The good news is that management is a craft. It's learnable. That's what we're here to do. -->

---

<!-- ⏱ Expected: 11:05 (min 5/100) -->
## How This Course Works

**Three case contexts** that anchor everything:

| Context | Company | Stage | Analytics Team |
|---|---|---|---|
| **Small** | DataPulse | Seed-stage startup | You are the first analytics hire |
| **Medium** | MarketBridge | Series B scale-up | You manage a team of 3 |
| **Large** | FinGuard | Enterprise financial services | You lead a 15+ person analytics org |

<!-- Talk track: Here's how the course works mechanically. We have three case contexts. Each one represents a different stage of analytics team maturity. DataPulse is a seed-stage startup — you're the first analytics hire, there's no infrastructure, and the CEO wants "data-driven decisions" but doesn't know what that means. MarketBridge is a Series B company — you've been hired to manage a small team that grew organically, and there's technical debt and unclear roles. FinGuard is an enterprise — you're leading a large analytics org with compliance requirements, multiple stakeholder groups, and legacy systems. -->

---

<!-- ⏱ Expected: 11:05 (min 5/100) -->
## How This Course Works

- You **choose one case context** and anchor ALL artifacts to it
- Everything builds: charter informs hiring, hiring informs roadmap, roadmap informs stakeholder communication
- You leave with a **coherent portfolio**, not disconnected exercises
- **Portfolio due:** one week after Day 2

<!-- Talk track: You're going to pick one of these, and everything you build in this course will be anchored to that context. Your charter, your stakeholder map, your hiring rubric, your roadmap — they all connect. At the end, you'll have a portfolio that tells a coherent story about how you'd manage an analytics team in your chosen context. The portfolio is due one week after Day 2 — polished, refined, and ready for me to review. -->

---

<!-- ⏱ Expected: 11:05 (min 5/100) -->
## Choose Your Case Context

Pick one now. You will use this for every activity across both days.

**DataPulse (Seed-Stage Startup)**
- 12-person company, Series Seed funding, 50K MAU and growing fast
- You are the FIRST analytics hire — no team, no infrastructure, no data warehouse
- The CEO wants "data-driven culture" but data lives in Firebase Analytics, Amplitude (free tier), and spreadsheets — plus the CEO runs raw PostgreSQL queries directly

<!-- Talk track: Okay, decision time. Read through these three contexts. DataPulse is the scrappy startup — if you pick this, you'll be thinking about how to build everything from zero with almost no resources. It's exciting, but it's also terrifying. -->

---

<!-- ⏱ Expected: 11:05 (min 5/100) -->
## Choose Your Case Context

**MarketBridge (Series B Scale-Up)**
- ~150-person two-sided marketplace (think Thumbtack), Series B, $30M raised
- You manage 3 analysts who previously reported to different PMs
- Dashboards everywhere, conflicting metric definitions, no documentation

<!-- Talk track: MarketBridge is the messy middle — the team exists but it's chaotic. If you pick this, you'll be thinking about how to bring order to an existing team. You'll be dealing with conflicting metric definitions, analysts who built their own pipelines, and a team that grew up without structure. -->

---

<!-- ⏱ Expected: 11:05 (min 5/100) -->
## Choose Your Case Context

**FinGuard (Enterprise Financial Services)**
- 5,000-person regulated financial institution
- You lead a 15+ person analytics org across multiple business lines
- Strict compliance requirements, centralized data governance, legacy on-prem warehouse being migrated to cloud

**Write your choice down. There are no wrong answers — each context teaches different lessons.**

<!-- Talk track: FinGuard is the enterprise — if you pick this, you'll be dealing with governance, politics, compliance, and the challenge of leading through layers of hierarchy. Pick one. Write it down. Commit to it. There's no wrong answer, but you do need to commit. Every exercise for the rest of the course is anchored to this choice. Take thirty seconds, make your pick, and let's move on. -->

---

<!-- ⏱ Expected: 11:10 (min 10/100) -->
## What Is a Manager?

> "A manager's output = the output of their organization + the output of neighboring organizations under their influence."
> — Andy Grove, *High Output Management*

You are not a "boss." You are a **system builder**.

Your job is to create the conditions where your team does its best work — and to extend that influence across the organization.

<!-- Talk track: Let's start with a question — what IS a manager? Andy Grove, former CEO of Intel, gave us the best definition I've ever seen. Read this quote carefully. Notice it says nothing about telling people what to do. Your output is not YOUR work — it's the output of your team and the teams you influence. That reframe is everything. You are not a boss. You are a system builder. Your job is to design the system that produces great work. Who here has had a great manager? What made them great? I bet it wasn't that they were the smartest person in the room. -->

---

<!-- ⏱ Expected: 11:10 (min 10/100) -->
## Manager vs. Tech Lead vs. PM

Three overlapping circles — the analytics manager spans all three but **owns People**.

| Dimension | Manager | Tech Lead | PM |
|---|---|---|---|
| **Primary concern** | People & org health | Technical quality & architecture | Product outcomes & roadmap |
| **Success metric** | Team retention, delivery, growth | Code quality, system reliability | User adoption, business impact |
| **Key ritual** | 1:1s, calibration, hiring | Design reviews, code reviews | Sprint planning, user research |
| **Superpower** | Context & coaching | Depth & standards | Prioritization & storytelling |

<!-- Talk track: So where does the analytics manager sit in an organization? There are three classic leadership roles that often overlap. The Manager owns people — hiring, retention, growth, performance. The Tech Lead owns technical quality — architecture decisions, code review standards, reliability. The PM owns product outcomes — what we build, for whom, and why. Look at this table carefully. Notice how each role has a different primary concern, a different success metric, a different key ritual, and a different superpower. In a small company, one person might wear all three hats. In a large company, these are distinct roles that need to collaborate. The tensions between these roles are some of the most productive tensions in an organization — when managed well. -->

---

<!-- ⏱ Expected: 11:15 (min 15/100) -->
## The Analytics Manager Is Unique

You live at the intersection. You need enough technical depth to earn trust, enough product sense to prioritize, and enough people skill to build a team.

**Why this overlap matters:**
- If you have no technical depth, your team won't respect your judgment on scoping or tradeoffs
- If you have no product sense, you'll build technically impressive things nobody uses
- If you have no people skill, your best analysts will leave for a manager who invests in them

**This is not a "choose two" situation.** You need baseline competence in all three.

<!-- Talk track: The analytics manager role is uniquely demanding because you can't fully delegate any of the three circles. No technical depth — your team won't respect your judgment. No product sense — you build things nobody uses. No people skill — your best analysts leave. This is not "choose two." You need all three. That's what makes this role hard, and it's also what makes it rewarding. -->

---

<!-- ⏱ Expected: ~11:15 (min 15/100) | SKIP — advance past -->
<!-- _class: skip -->

## When the VP Asks "Why Is Churn Up?"

A concrete scenario to illustrate the three roles:

**The PM** frames the business context: "Churn spiked 2.3 points this quarter, concentrated in our SMB segment. We think it's related to the pricing change we made in Q2, but we need analysis to confirm."

**The Tech Lead** explains the technical investigation: "We built a survival model segmenting by pricing cohort. The data shows the Q2 pricing tier is 40% more likely to churn within 90 days."

<!-- Talk track: Let me make this concrete. Imagine your VP sends a Slack message at 9am: "Why is churn up? I need answers before the board meeting." Watch how the three roles respond differently. The PM gives business context — they know the churn number, they have a hypothesis, and they can frame why it matters. The Tech Lead does the actual analytical work — they build the model, run the analysis, and present the findings with appropriate rigor. -->

---

<!-- ⏱ Expected: ~11:15 (min 15/100) | SKIP — advance past -->
<!-- _class: skip -->

## When the VP Asks "Why Is Churn Up?"

**The Manager** ensures the right person is assigned and the team isn't overwhelmed: "I'm going to pull Jordan off the dashboard migration for two days to run this analysis. I'll let the platform team know about the delay. And I'll set up a 30-minute readout with the VP for Thursday so we have a clear deadline."

**Notice:** The Manager's contribution isn't analytical — it's operational. Clearing the path, managing the tradeoff, setting the timeline. That IS the work.

<!-- Talk track: But the Manager? The Manager's job is to make sure the right person is working on it, that they have the time and space to do good work, that someone else's project isn't silently slipping, and that there's a clear deadline and delivery format. That orchestration work is invisible but essential. If nobody does it, the analysis either doesn't happen, happens too slowly, or happens at the cost of three other commitments nobody bothered to renegotiate. -->

---

<!-- ⏱ Expected: 11:18 (min 18/100) -->
## Team Topologies for Analytics

From Skelton & Pais — four fundamental team types:

| Topology | Analytics Version | Example |
|---|---|---|
| **Stream-aligned** | Embedded analysts in a product team | "Growth Analytics" sits inside the Growth pod |
| **Platform** | Data infrastructure & tooling | The team that owns the warehouse, pipelines, BI tool |
| **Enabling** | Data literacy & training | A small team that teaches PMs to self-serve |
| **Complicated-subsystem** | ML / specialized modeling | The fraud-detection or forecasting team |

<!-- Talk track: Team Topologies is a book by Skelton and Pais that gives us a language for how teams relate to each other. I want you to think about these four types through an analytics lens. Stream-aligned teams are embedded — they sit inside a product squad and serve that squad directly. Think of a "Growth Analytics" team that sits in the Growth pod — they go to the Growth standup, they know the Growth roadmap, they're fully context-loaded. Platform teams build the infrastructure everyone depends on — the data warehouse, the ETL pipelines, the BI tools. Enabling teams exist to make other teams more capable — data literacy programs, self-serve training, office hours. And complicated-subsystem teams handle genuinely hard technical problems like fraud detection models or demand forecasting. Each type has different management challenges. Stream-aligned teams risk losing their analytics identity. Platform teams risk becoming disconnected from business outcomes. Enabling teams struggle to show impact. Complicated-subsystem teams can become ivory towers. -->

---

<!-- ⏱ Expected: 11:18 (min 18/100) -->
## Applying Team Topologies to Your Case Context

**Which topology best describes your team?** Most analytics orgs are a mix.

**DataPulse (startup):** You are probably one person doing all four topologies at once. You're building the pipeline, embedding with the product team, training PMs to read dashboards, and maybe building a basic churn model. This is normal at a startup — but it means you need to be intentional about where you spend your time.

<!-- Talk track: Now take this framework and apply it to your case. If you're DataPulse, you don't have the luxury of team topologies — you ARE the team. But it's still useful to think about which hat you're wearing at any given moment. Am I doing platform work right now, or am I doing embedded analytics? That awareness helps you manage your time. -->

---

<!-- ⏱ Expected: 11:18 (min 18/100) -->
## Applying Team Topologies to Your Case Context

**MarketBridge (scale-up):** You likely have stream-aligned analysts who grew up embedded in different pods, but no platform team. That's why there are conflicting metric definitions — nobody owns the infrastructure. Your first move might be carving out a platform function.

<!-- Talk track: If you're MarketBridge, I bet your biggest problem is that you have a bunch of stream-aligned analysts with no platform underneath them. Everyone built their own pipeline, everyone defined metrics differently, and now you're trying to consolidate. Sound familiar? Your first move is probably to carve out someone whose job is owning the platform — even if it's 20% of one person's time to start. -->

---

<!-- ⏱ Expected: 11:18 (min 18/100) -->
## Applying Team Topologies to Your Case Context

**FinGuard (enterprise):** You probably have all four topologies, but they may not talk to each other. The ML team might not know what the embedded analysts need. The platform team might be building for compliance, not for analyst productivity. Your challenge is coordination.

<!-- Talk track: And if you're FinGuard, you probably have all four types but they've calcified into silos. The ML team ships models that the business analysts can't interpret. The platform team builds infrastructure the analysts don't use. Your job is to create the interaction modes between these teams — regular syncs, shared documentation, explicit service-level agreements between the platform team and the stream-aligned analysts. -->

---

<!-- ⏱ Expected: 11:21 (min 21/100) -->
## The Manager OS Concept

Your **operating system** has four layers:

1. **Cadences** — the rhythm (daily / weekly / monthly / quarterly)
2. **Rituals** — the meetings and practices that fill those cadences
3. **Artifacts** — the documents that capture decisions and alignment
4. **Decision hygiene** — the meta-practices that keep decisions clean

Think of it like software: cadences are the scheduler, rituals are the processes, artifacts are the data store, and decision hygiene is the error-handling layer.

<!-- Talk track: Here's the core mental model for this block. Your Manager OS has four layers. Cadences are the clock — how often things happen. Rituals are the actual meetings and practices. Artifacts are the written documents that create shared memory. And decision hygiene is how you make sure decisions are actually good. I like the software analogy: cadences are your cron scheduler, rituals are your running processes, artifacts are your database, and decision hygiene is your error handling. Over this block, we're going to build out each layer for YOUR context. -->

---

<!-- ⏱ Expected: 11:21 (min 21/100) -->
## AI-Augmented Manager OS

LLMs add a **force multiplier** to every OS layer:

| OS Layer | AI Augmentation |
|---|---|
| **Cadences** | Auto-generate 1:1 agendas from your manager log and team updates |
| **Artifacts** | LLM-draft decision memos — you edit for judgment, not from scratch |
| **Decision hygiene** | Red-team your own thinking: "What am I missing?" |
| **Stakeholder comms** | Translate technical wins into exec-ready language in seconds |

<!-- Talk track: I want to add a layer to the OS model. LLMs are becoming a force multiplier for every layer we just discussed. You can use an LLM to draft your 1:1 agendas from your manager log, draft decision memos in 5 minutes instead of 45, stress-test your own reasoning before sharing it, and translate technical work into business language for stakeholders. This isn't about replacing your judgment — it's about freeing up your time so you can focus on the judgment calls that actually require a human. -->

---

<!-- ⏱ Expected: 11:21 (min 21/100) -->
## AI-Augmented Manager OS

**The key principle:** AI handles the drafting. You own the judgment.

- **Example:** Feed an LLM your last 3 weekly updates → get a draft exec summary in 30 seconds → spend 5 minutes editing for nuance and accuracy
- **Example:** Before a difficult stakeholder meeting, role-play the conversation with an LLM to anticipate objections
- **Hidden stakeholder:** Whoever controls your LLM/API budget is on your stakeholder map

<!-- Talk track: Let me give you two concrete examples. First, take your last three weekly team updates, paste them into an LLM, and ask for a draft executive summary. You'll get a solid first draft in 30 seconds. Then you spend 5 minutes editing for nuance, accuracy, and judgment. That's 5 minutes instead of 30, and the quality is just as high because you're the editor. Second, before a difficult stakeholder meeting, role-play the conversation with the LLM. Ask it to play the skeptical CFO. Practice your responses. You'll walk in more prepared than you've ever been. And here's a new hidden stakeholder for your map: whoever controls your team's LLM and API budget. As AI-assisted workflows grow, compute costs can balloon. Map that person now. -->

---

<!-- ⏱ Expected: ~11:21 (min 21/100) | SKIP — advance past -->
<!-- _class: skip -->

## What Happens Without a Manager OS?

Without an OS, you get **chaos that feels like busyness**:

- **No cadences** — problems fester until they become conflicts
- **No artifacts** — decisions get relitigated because nobody wrote them down
- **No rituals** — career conversations and priority reviews fall through cracks
- **No decision hygiene** — the loudest voice wins, not the best argument

**You have seen this.** Every analytics team that feels "chaotic" or "reactive" is usually missing one or more of these layers.

<!-- Talk track: Let me paint the picture of what happens without a Manager OS. Without cadences, problems fester — a small misunderstanding Monday becomes a conflict by Friday. Without artifacts, decisions get relitigated — you had the metrics conversation three months ago but nobody wrote it down. Without rituals, career conversations just don't happen. And without decision hygiene, whoever is loudest wins. If any of this sounds familiar, good. That's why we're building your OS today. -->

---

<!-- ⏱ Expected: 11:24 (min 24/100) -->
## Cadences That Work

| Cadence | What happens | Why it matters |
|---|---|---|
| **Daily** | Async standup (Slack/Teams post) or skip entirely | Visibility without meetings |
| **Weekly** | 1:1s with each report + team sync | Course-correct fast; build trust |
| **Monthly** | Metrics review + mini-retro | Catch drift; celebrate wins |
| **Quarterly** | Planning + calibration + roadmap refresh | Strategic alignment; career growth |

**The rhythm creates predictability.** The biggest mistake new managers make: too many meetings with no rhythm. Pick a cadence and protect it.

<!-- Talk track: Let's start with cadences. Here are the four I recommend. Daily — for most analytics teams, you can skip the daily standup or make it async. Weekly is where the magic happens: your 1:1s and one team sync. Monthly, you zoom out and look at metrics. Quarterly, you do real planning and calibration. The key insight is that the rhythm itself creates predictability. Your team should never wonder "when will I get to talk to my manager about this?" -->

---

<!-- ⏱ Expected: ~11:24 (min 24/100) | SKIP — advance past -->
<!-- _class: skip -->

## Designing Your Cadence

**Meeting Audit Exercise** — before adding meetings, audit what exists:

1. List every recurring meeting you attend or own
2. For each, ask: Does it have an **owner**? A **standing agenda**? A **decision or action item** as output?
3. If a meeting fails all three — kill it or convert it to async

<!-- Talk track: Before you start adding meetings, audit what you already have. I've done this exercise with dozens of managers, and every single time, we find at least two or three recurring meetings that have no owner, no agenda, and no clear output. If it fails all three — kill it or convert it to async. You just freed up hours in your calendar. -->

---

<!-- ⏱ Expected: ~11:24 (min 24/100) | SKIP — advance past -->
<!-- _class: skip -->

## Designing Your Cadence

**Introducing cadences to a team that has none:**

- **Don't overhaul everything at once.** Start with weekly 1:1s and one team sync. That's it.
- **Explain the "why" before the "what."** People resist new meetings; they won't resist 30 guaranteed minutes with their manager.
- **Timebox aggressively.** A 25-minute meeting that ends on time builds more trust than a 60-minute meeting that rambles.
- **Protect the cadence.** The first time you cancel a new ritual, you signal it's optional. Don't.

<!-- Talk track: Now, if you're starting from scratch — maybe you picked DataPulse and there's literally no team yet — start small. Weekly 1:1s and one team sync. That's your entire meeting load. Don't introduce a monthly metrics review until you actually have metrics to review. And here's the most important piece: when you introduce a new cadence, explain why. "I'm adding a weekly 1:1 because I want to make sure you always have dedicated time with me" lands completely differently than "we're adding a new meeting to the calendar." People don't hate meetings. They hate bad meetings. Give them good ones, and they'll protect the cadence themselves. -->

---

<!-- ⏱ Expected: 11:27 (min 27/100) -->
## 1:1s That Actually Work

**Structure (30 minutes):**
- **10 min** — Their agenda (what's on their mind?)
- **10 min** — Your agenda (context, feedback, asks)
- **10 min** — Career & growth (not every week, but regularly)

**Pro tip:** Keep a shared running doc. Both sides add agenda items before the meeting.

<!-- Talk track: The 1:1 is the single most important ritual in your Manager OS. Let me be blunt: if you cancel 1:1s regularly, you are failing as a manager. Here's a simple structure that works. First ten minutes are theirs — they set the agenda. This is critical. The 1:1 is their meeting, not yours. You're there to listen, unblock, and support. Middle ten minutes are yours — context from leadership, feedback you need to give, specific asks. Last ten minutes are about their career and growth. You don't need to do the career portion every week, but you should do it at least once a month. And the shared doc is non-negotiable. Both of you add items before the meeting so you're not wasting time figuring out what to talk about. -->

---

<!-- ⏱ Expected: 11:27 (min 27/100) -->
## 1:1 Anti-Patterns

**Anti-patterns to avoid:**
- **The Status Update Trap** — "What did you do this week?" (Use async for this)
- **The Therapy Session** — Empathy is good, but you're not a therapist
- **The Canceled 1:1** — The fastest way to signal "you don't matter"
- **The Monologue** — If you're talking more than 50%, something's wrong

**Diagnostic signals:**
- Boring 1:1s = relationship isn't deep enough yet
- Every 1:1 is a fire drill = structural problem, not a 1:1 problem
- "I don't have anything" every week = they don't trust the space yet

<!-- Talk track: Let me name the anti-patterns. The status update trap — that's what Slack is for. The therapy session — help them solve the problem, don't just absorb the emotion. The canceled 1:1 — nothing says "you don't matter" faster. The monologue — if you're talking more than half the time, it's a broadcast, not a conversation. And watch the diagnostic signals: boring 1:1s mean the relationship isn't deep enough. Fire-drill 1:1s mean you have a structural problem upstream. "I don't have anything" means they don't trust the space yet — that's on you to fix. -->

---

<!-- ⏱ Expected: ~11:27 (min 27/100) | SKIP — advance past -->
<!-- _class: skip -->

## Handling Difficult 1:1s: The Silent Report

**The report who never has agenda items:**
- They might not trust the space yet. Give it time and keep showing up.
- Offer prompts: "What's the most frustrating thing you dealt with this week?" or "If you could change one thing about how we work, what would it be?"
- Share your own vulnerabilities first — model that the 1:1 is a safe space for real talk.

<!-- Talk track: Let me give you tactical advice for common difficult situations. First, the report who shows up and says "I don't have anything." This is almost never true — they just don't trust the space yet, or they don't know what's appropriate to bring up. Give them prompts. I like to ask "what's the most frustrating thing you've dealt with this week?" That question almost always unlocks something. -->

---

<!-- ⏱ Expected: ~11:27 (min 27/100) | SKIP — advance past -->
<!-- _class: skip -->

## Handling Difficult 1:1s: The Silent Report

**The silent report:**
- Some people process internally. Try written 1:1s — share questions 24 hours ahead.
- Walk-and-talk or informal settings sometimes open people up more than a conference room.
- Be patient. Trust is built in small moments over months, not in one conversation.

<!-- Talk track: Then there's the truly silent report. Some people are just internal processors. That's okay. Try a written format — share questions in advance and let them respond in writing if that's more comfortable. I had a brilliant analyst once who said almost nothing in our 1:1s until I switched to walking meetings. Something about not making eye contact and moving through space opened her up completely. Experiment. There's no single right format. -->

---

<!-- ⏱ Expected: ~11:27 (min 27/100) | SKIP — advance past -->
<!-- _class: skip -->

## Handling Difficult 1:1s: The Complainer

**The report who only brings complaints:**
- Validate first, then redirect: "I hear you. That does sound frustrating. What do you think we should do about it?"
- If it's about a coworker, ask "Have you talked to them directly?" before offering to intervene.
- Pattern-match across complaints — is there a structural issue underneath? If so, fix the structure, not the symptoms.

<!-- Talk track: Second common situation: the report who turns every 1:1 into a complaint session. Start by validating — their frustration is real. But then redirect toward action. "What should we do about it?" And if they're complaining about a coworker, always ask if they've talked to that person directly. Most importantly, pattern-match. If the same themes keep coming up, there might be a real structural problem underneath. Maybe the team process is broken, or the workload distribution is unfair. In that case, the complaining is actually useful signal. Your job is to separate the signal from the noise and fix the root cause. -->

---

<!-- ⏱ Expected: 11:30 (min 30/100) -->
## Decision Logs & Memos

**Why writing beats meetings:**
- Writing forces clarity — you can't hand-wave in prose
- Writing scales — 50 people can read a memo; 50 can't be in a meeting
- Writing creates institutional memory

<!-- Talk track: Let's talk about written decision-making. There are three reasons writing beats meetings for important decisions. First, writing forces clarity — you literally cannot hand-wave when you have to put words on a page. Second, writing scales — you can share a memo with fifty people, but you can't have a productive meeting with fifty people. Third, writing creates institutional memory — six months from now, you can look back and understand why a decision was made. -->

---

<!-- ⏱ Expected: 11:30 (min 30/100) -->
## Decision Logs & Memos

**The 1-page Decision Memo has five sections:**

- **Context** — What situation prompted this decision?
- **Options** — At least 3 options with pros/cons
- **Recommendation** — Which option and why
- **Risks** — What could go wrong and how we'd mitigate
- **Decision Type** — Type 1 (irreversible) or Type 2 (reversible)

**Default to Type 2.** Most decisions are reversible — move fast on those. Slow down on Type 1. Empower your team to go on Type 2; write a memo for Type 1.

<!-- Talk track: Here is the template for a one-page decision memo. Five sections, each with a clear purpose. Context sets the scene, Options forces creative thinking, Recommendation commits to a path, Risks shows you've thought about downsides, and Decision Type tells everyone how fast to move. The key question to always ask is: "Is this a one-way door or a two-way door?" For Type 2 decisions, empower your team to just go. Don't require a memo for every small call. For Type 1 decisions, write a memo — the act of writing forces clear thinking. That single question will save your team from both reckless speed and unnecessary paralysis. -->

---

<!-- ⏱ Expected: ~11:30 (min 30/100) | SKIP — advance past -->
<!-- _class: skip -->

## Example Decision Memo

**Context:** MarketBridge uses Amplitude. Engineering proposes migrating to Snowplow + Snowflake.

**Options:**

| Option | Pros | Cons |
|---|---|---|
| **A: Stay on Amplitude** | No migration cost | $120K/yr; vendor lock-in |
| **B: Full in-house** | Full data ownership | 3-4 month migration |
| **C: Hybrid** | PMs unaffected | Two systems to maintain |

<!-- Talk track: Let me show you what a real decision memo looks like. This is for MarketBridge — should we migrate from Amplitude to an in-house event tracking system? Notice the structure. The context is crisp — one paragraph, everyone understands the situation. Then three options. Not two, because two options creates a false binary. Three forces you to think creatively. Look at the pros and cons — they're specific. Not "it's expensive" but "$120K per year." Not "it takes time" but "3-4 month migration." Specificity is what separates a useful memo from a waste of paper. -->

---

<!-- ⏱ Expected: ~11:30 (min 30/100) | SKIP — advance past -->
<!-- _class: skip -->

## Example Decision Memo

**Recommendation:** Option C (Hybrid), migrating to full in-house (Option B) in 12 months. This de-risks the migration while giving analytics immediate access to raw event data.

**Risks:** Dual systems create metric discrepancy risk. Mitigate with a shared event taxonomy document and weekly reconciliation checks for the first 3 months.

<!-- Talk track: The recommendation is Option C — the hybrid approach. And notice the reasoning: it de-risks the migration. That's strategic thinking. The risks section is specific about what could go wrong and how to mitigate it. -->

---

<!-- ⏱ Expected: ~11:30 (min 30/100) | SKIP — advance past -->
<!-- _class: skip -->

## Example Decision Memo

**Decision Type:** Type 2 — reversible. If the hybrid approach fails, we revert to Amplitude-only within a month.

This classification matters because it tells everyone "we don't need to agonize over this for three weeks." Write the memo, circulate it, make the call.

<!-- Talk track: And at the bottom, this is classified as Type 2 — reversible. If it doesn't work, we go back. That classification matters because it tells everyone "we don't need to agonize over this for three weeks." Write the memo, circulate it, make the call. This is what decision hygiene looks like in practice. You'll write your own memos like this during the course. -->

---

<!-- ⏱ Expected: 11:33 (min 33/100) -->
## The Team Charter

**What it is:** A 1-2 page document capturing your team's identity and operating agreements.

**Sections:**
- **Purpose & Mission** — Why does this team exist? (2-3 sentences)
- **Scope & Boundaries** — What's in, what's explicitly out
- **Principles** — 3-5 operating rules the team lives by
- **Key Interfaces** — Who do you interact with and how?
- **Success Metrics** — How do you know if you're winning?
- **Cadences & Rituals** — Recurring meetings and their purpose

<!-- Talk track: The Team Charter is the first artifact in your Manager OS. Think of it as your team's constitution. It answers the fundamental questions: why do we exist, what do we do, what don't we do, and how do we operate? The template has six sections — the last one, Cadences and Rituals, connects directly to what we covered earlier about management rhythms. -->

---

<!-- ⏱ Expected: 11:33 (min 33/100) -->
## The Team Charter

**Why it matters:** Alignment without constant re-negotiation. When someone asks "should we do X?" the charter helps answer.

**Example principle:** *"We ship insights, not dashboards. If an analysis doesn't lead to a decision, we ask why before starting it."*

<!-- Talk track: Let me give you a real example. I once joined a team where every PM in the company felt entitled to ask for any analysis at any time. The team was drowning. We wrote a charter that said: "We serve the Growth and Monetization pods. Other teams submit requests through a quarterly intake process." That one sentence saved hundreds of hours. You're going to write your own charter in about twenty minutes. Let me show you what the template looks like. -->

---

<!-- ⏱ Expected: 11:33 (min 33/100) -->
## The Stakeholder Map

**Power/Interest Grid:**

| Power / Interest | Low Interest | High Interest |
|---|---|---|
| **High Power** | Keep Satisfied | Manage Closely |
| **Low Power** | Monitor | Keep Informed |

<!-- Talk track: The stakeholder map is your relationship radar. This 2x2 grid comes from classic project management but it's incredibly useful for analytics managers. High power, high interest — these are your bread and butter stakeholders. You manage them closely. They're the VP of Product who cares deeply about data and has budget authority. High power, low interest — these are dangerous. Think of the CFO who doesn't care about analytics until something goes wrong, and then suddenly they care a lot. You need to keep them satisfied with periodic updates so they don't blindside you. Low power, high interest — these are often your power users, the PMs who love data but don't control your budget. Keep them informed and they'll be your advocates. And low power, low interest — just monitor. Don't waste energy here, but don't lose track of them either, because power and interest levels change. -->

---

<!-- ⏱ Expected: 11:33 (min 33/100) -->
## Stakeholder Map: What to Capture

**For each stakeholder, capture:**
- Name/Role
- What they need from you
- What you need from them
- Engagement strategy (frequency + channel)

**The hidden stakeholders:** Don't forget IT, Legal/Privacy, Finance, and the engineers who maintain your pipelines. New managers always under-map.

**Ask yourself:** "Who could block my work if I have NOT built a relationship with them?"

<!-- Talk track: For each stakeholder, capture not just who they are but the exchange. What do they need from you? What do you need from them? And don't forget the hidden stakeholders — IT controls your infrastructure, Legal controls your data access, Finance controls your budget. The engineers who maintain your pipelines can make or break your productivity. Ask yourself: who could block me if I haven't built a relationship with them? Those are the people you need to map. -->

---

<!-- ⏱ Expected: 11:33 (min 33/100) -->
## Stakeholder Map: Hidden Stakeholders by Context

- **DataPulse:** The CTO (cloud budget), the sole backend engineer, the LLM/API budget controller
- **MarketBridge:** Data engineering (pipeline), compliance officer, platform team (LLM costs)
- **FinGuard:** Model risk management, internal audit, vendor management, AI governance committee

> I once had a project blocked for six weeks because I didn't map the data privacy team. Map early, avoid delays.

<!-- Talk track: Every time I do this exercise with a new manager, they map the obvious ones — their boss, the PMs, the product team. But they miss IT, Legal, Privacy, Finance. Think about your case context — who could block you that you haven't thought of yet? The DataPulse folks should think about that one backend engineer. The MarketBridge folks should think about data engineering and compliance. The FinGuard folks should think about model risk management and internal audit. These are the relationships that, if you build them early, save you weeks of delay later. -->

---

<!-- ⏱ Expected: ~11:33 (min 33/100) | SKIP — advance past -->
<!-- _class: cut -->

## RACI in 60 Seconds

| Letter | Meaning | Rule |
|---|---|---|
| **R** | Responsible — does the work | Can be multiple people |
| **A** | Accountable — owns the outcome | **Exactly one person per decision** |
| **C** | Consulted — input before the decision | Keep this list short |
| **I** | Informed — told after the decision | Default for most people |

<!-- Talk track: RACI is one of those frameworks that people either love or hate. I'm going to teach you to use it well, which means using it sparingly. R is who does the work. A is who owns the outcome — and this is the critical one. There must be exactly one A per decision. If two people think they're accountable, nobody is. C is who you consult before deciding, and I is who you inform after. Let me emphasize that rule about the A — exactly one person. This is where organizations go wrong. They say "well, both the analytics manager and the PM are accountable for this metric." No. One person is accountable. The other person might be Responsible or Consulted, but there is one throat to choke, as the saying goes. That clarity is uncomfortable, but it's essential. -->

---

<!-- ⏱ Expected: ~11:33 (min 33/100) | SKIP — advance past -->
<!-- _class: cut -->

## RACI: Common Mistakes

**Common mistakes:**
- Everyone is "Consulted" on everything (consensus paralysis)
- No clear "A" (diffusion of responsibility)
- RACI for trivial decisions (overhead kills velocity)

**Use RACI for the 5-10 decisions that cause the most confusion.** Not for everything.

<!-- Talk track: The biggest mistake I see is organizations that RACI everything. Don't do that. Pick the five to ten decisions that cause the most confusion or conflict, and RACI those. And watch out for the "everyone is consulted" trap. If you consult eight people before every decision, you've created consensus paralysis. Keep the C list short. Most people should be I — informed after the fact. -->

---

<!-- ⏱ Expected: ~11:33 (min 33/100) | SKIP — advance past -->
<!-- _class: cut -->

## RACI: When to Use It

**Good candidates for RACI in an analytics team:**
- Who defines canonical metric definitions?
- Who approves a new dashboard going to production?
- Who decides whether to take on a new stakeholder request?
- Who signs off on a model before production?
- Who decides on tooling changes (new BI tool, new pipeline)?

**Bad candidates:** Chart colors. SQL style guides. Documentation location. These are decisions, but not worth formalizing.

<!-- Talk track: I've listed some good candidates here — metric definitions, dashboard approvals, stakeholder intake, model sign-off, tooling changes. These are the decisions where ambiguity causes real pain. If nobody knows who owns metric definitions, you'll have three different teams reporting three different churn numbers to the board. That's a RACI-worthy decision. But "what color should the chart be?" That does not need a RACI matrix. If you RACI trivial decisions, people will roll their eyes at the whole framework and ignore it even when it matters. Use it surgically, and it's powerful. Use it for everything, and it's bureaucracy. -->

---

<!-- ⏱ Expected: 11:37 (min 37/100) | Activity brief — Team Charter; activity starts at 11:45 -->
<!-- _class: divider -->

## Activity: Draft Your Team Charter

## 22 Minutes | `templates/team-charter.md`

<!-- Talk track: Time to put what you've learned into practice. For the next 22 minutes, you'll draft a Team Charter using your case context. Open the template — let's go. -->

---

<!-- ⏱ Expected: 11:37 (min 37/100) | Activity brief — Team Charter; activity starts at 11:45 -->
## Activity: Draft Your Team Charter

**Time: 22 minutes** | Open `templates/team-charter.md`

Using your chosen case context, draft a Team Charter with:
1. **Purpose & Mission** — Why does this analytics team exist?
2. **Scope & Boundaries** — What's in scope? What's explicitly NOT?
3. **3 Operating Principles** — Rules your team lives by

<!-- Talk track: All right, let's put this into practice. Open the Team Charter template — it's in your materials. You have 22 minutes. I want you to work individually, anchored to your case context. If you chose the small startup, your charter should reflect that reality — limited resources, scrappy, moving fast. If you chose the large enterprise, think about governance, compliance, cross-team coordination. -->

---

<!-- ⏱ Expected: 11:37 (min 37/100) | Activity brief — Team Charter; activity starts at 11:45 -->
## Activity: Draft Your Team Charter

Continue your Team Charter with:
4. **Key Interfaces** — At least 4 teams/roles you interact with
5. **Success Metrics** — 3-5 KPIs for your team's first year
6. **Cadences** — What meetings happen and when?

**Tip:** Be specific to your case. A startup charter looks very different from an enterprise charter. "We value data quality" is not a principle. "Every metric has a documented definition and an owner before it goes to production" is.

<!-- Talk track: Be specific. Don't write generic platitudes. I'll circulate and answer questions. Go. -->

---

<!-- ⏱ Expected: 12:07 (min 67/100) | Activity brief — Stakeholder Map -->
<!-- _class: divider -->

## Activity: Map Your Stakeholders

## 18 Minutes | `templates/stakeholder-map.md`

<!-- Talk track: Second activity. You'll map your stakeholders on the Power/Interest grid. Open the template. -->

---

<!-- ⏱ Expected: 12:07 (min 67/100) | Activity brief — Stakeholder Map -->
## Activity: Map Your Stakeholders

**Time: 18 minutes** | Open `templates/stakeholder-map.md`

Map your stakeholders on the Power/Interest grid.

**Requirements:**
- Identify **at least 6 stakeholders** (roles, not names)
- For each, note Power level (High / Low) and Interest level (High / Low)
- Also capture: what they need from you

<!-- Talk track: Excellent work on the charters. Now flip to the Stakeholder Map template. You have 18 minutes. I want at least six stakeholders, and I want you to really think about the ones you might miss. Use the prompts on the next slide to jog your thinking. -->

---

<!-- ⏱ Expected: 12:09 (min 69/100) | Activity: Map Stakeholders (18 min) -->
## Activity: Map Your Stakeholders

For each stakeholder, also note what you need from them and your engagement strategy.

**Prompts to jog your thinking:**
- Who funds your team?
- Who consumes your outputs?
- Who controls access to data or systems?
- Who could block your work if unhappy?
- Who do you depend on but rarely talk to?

<!-- Talk track: Here are some prompts. Who funds your team? That's probably a VP or C-suite — high power. Who consumes your outputs? Product managers, maybe marketing. Who controls your data access? Who could block your work if unhappy — think Legal, Privacy, Compliance. And who do you depend on but rarely talk to? Those invisible dependencies are the ones that will bite you later. Go deep here. -->

---

<!-- ⏱ Expected: 12:27 (min 87/100) | Pair Share (5 min) -->
## Pair Share

**Time: 5 minutes (2–3 minutes each)**

Find a partner — ideally someone who chose a **different** case context.

**Share your stakeholder map and discuss:**
- Who are your "Manage Closely" stakeholders and why?
- Which stakeholder did you almost forget?
- Where do your maps differ because of your case contexts?

**Listen for:** assumptions your partner made that you didn't.

<!-- Talk track: Okay, time's up on the individual work. Find a partner — and try to pair with someone who chose a different case context than you. You have five minutes each. Share your stakeholder map. Focus on who your "manage closely" stakeholders are, which stakeholder you almost left off, and where your maps differ. The stakeholders we forget are often the ones who cause us the most trouble later. -->

---

<!-- ⏱ Expected: 12:32 (min 92/100) | Debrief + Transition to Block B -->
## Debrief

**Let's hear from the room:**

- Who found a stakeholder they almost missed? What was it?
- Did anyone realize their case context changes WHO the key stakeholders are?
- What's one principle from your charter that you're genuinely proud of?

**Key insight:** The stakeholders you forget to map are usually the ones who block you later. The charter principles you're most proud of are usually the ones that will be hardest to enforce.

<!-- Talk track: Let's come back together. I want one volunteer — who found a stakeholder they almost missed? Tell us who it was and why you almost left them off. Great. Notice a pattern here — the stakeholders we overlook tend to be the ones with "quiet power." They don't show up in your daily work, but they control something critical. IT controls your infrastructure. Legal controls your data access. Finance controls your budget. Map them early, build the relationship before you need something. That's proactive management. -->

---

<!-- ⏱ Expected: 12:32 (min 92/100) | Debrief + Transition to Block B -->
## Your Manager OS So Far

After this block, you have:

- [x] **A mental model** — Manager as system builder, not boss
- [x] **A Team Charter** — Purpose, scope, principles, interfaces, metrics
- [x] **A Stakeholder Map** — Power/Interest grid with engagement strategies
- [x] **A sense of cadences** — Daily/weekly/monthly/quarterly rhythms
- [x] **Decision hygiene basics** — Type 1 vs. Type 2, decision memos, RACI

These are the **foundation** of your Manager OS. Every block builds on this.

**Reminder:** Your Team Charter and Stakeholder Map are due as drafts at end of Day 1.

<!-- Talk track: Let's take stock of where we are. In 100 minutes, you've built the foundation of your Manager Operating System. You have a charter that defines your team's identity. You have a stakeholder map that shows your relationship landscape. You have a framework for cadences and a toolkit for making good decisions. These are artifacts you will refine and submit. Your charter and stakeholder map are due as drafts by end of today. They don't need to be perfect, but they need to be substantive. -->

---

<!-- ⏱ Expected: 12:32 (min 92/100) | Debrief + Transition to Block B -->
<!-- _class: divider -->

## Up Next: Block B

## Hiring & Team Formation
### 13:30–15:10

<!-- Talk track: That wraps up Block A. After lunch, we move to hiring and team formation. -->

---

<!-- ⏱ Expected: 12:32 (min 92/100) | Debrief + Transition to Block B -->
## Transition to Block B

**After lunch: Block B — Hiring & Team Formation (13:30-15:10)**

You have your charter. You know your stakeholders. Now the question becomes:

> **"Who do I need on my team to fulfill this charter?"**

<!-- Talk track: We're breaking for lunch. When you come back at 1:30, we'll tackle hiring and team formation. Here's the key question: look at your charter — look at the purpose, the scope, the success metrics. Now ask yourself: who do I need on this team to actually deliver on that charter? -->

---

<!-- ⏱ Expected: 12:32 (min 92/100) | Debrief + Transition to Block B -->
## Transition to Block B

**Think about over lunch:**
- What's the first role you'd hire for your case context?
- What skills matter most — technical depth, communication, domain knowledge?
- How would you know if a candidate is "right"?

See you at 13:30.

<!-- Talk track: What's the first role you'd hire? Is it a senior analyst who can mentor juniors? A data engineer who can fix the pipeline mess? An analytics engineer who bridges the gap? We'll dig into structured hiring, work-sample design, and interview loops. Enjoy lunch, and I'll see you back here at 1:30. -->
