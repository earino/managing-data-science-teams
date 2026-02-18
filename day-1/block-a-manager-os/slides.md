---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 1 – Block A"
---

# The Manager's Operating System

**Day 1 — Block A | 11:00–12:40**

**Learning Outcomes**
By the end of this block you will be able to:
- Construct a Manager OS with cadences, rituals, artifacts, and decision hygiene
- Draft a Team Charter anchored to your case context
- Map stakeholders on a Power/Interest grid
- Apply RACI to common analytics team decisions

<!-- Talk track: Welcome to Managing Data Science Teams. I'm excited to spend these two days with you. This opening block is about the operating system you'll run as a manager — the repeatable patterns that make your team predictable, trustworthy, and effective. By the end of this session, you'll have two concrete artifacts: a Team Charter and a Stakeholder Map. Let's get started. -->

---

## What Is a Manager?

> "A manager's output = the output of their organization + the output of neighboring organizations under their influence."
> — Andy Grove, *High Output Management*

You are not a "boss." You are a **system builder**.

Your job is to create the conditions where your team does its best work — and to extend that influence across the organization.

<!-- Talk track: Let's start with a question — what IS a manager? Andy Grove, former CEO of Intel, gave us the best definition I've ever seen. Read this quote carefully. Notice it says nothing about telling people what to do. Your output is not YOUR work — it's the output of your team and the teams you influence. That reframe is everything. You are not a boss. You are a system builder. Your job is to design the system that produces great work. Who here has had a great manager? What made them great? I bet it wasn't that they were the smartest person in the room. -->

---

## Manager vs. Tech Lead vs. PM

Three overlapping circles — the analytics manager spans all three but **owns People**.

| Dimension | Manager | Tech Lead | PM |
|---|---|---|---|
| **Primary concern** | People & org health | Technical quality & architecture | Product outcomes & roadmap |
| **Success metric** | Team retention, delivery, growth | Code quality, system reliability | User adoption, business impact |
| **Key ritual** | 1:1s, calibration, hiring | Design reviews, code reviews | Sprint planning, user research |
| **Superpower** | Context & coaching | Depth & standards | Prioritization & storytelling |

The analytics manager is unique: you live at the intersection. You need enough technical depth to earn trust, enough product sense to prioritize, and enough people skill to build a team.

<!-- Talk track: So where does the analytics manager sit in an organization? There are three classic leadership roles that often overlap. The Manager owns people — hiring, retention, growth, performance. The Tech Lead owns technical quality — architecture decisions, code review standards, reliability. The PM owns product outcomes — what we build, for whom, and why. Here's the thing about analytics managers: you span all three circles. You need to understand the tech deeply enough that your team trusts your judgment, you need to understand the product well enough to prioritize the right work, and you own the people. That makes the role uniquely demanding — and uniquely rewarding. -->

---

## Team Topologies for Analytics

From Skelton & Pais — four fundamental team types:

| Topology | Analytics Version | Example |
|---|---|---|
| **Stream-aligned** | Embedded analysts in a product team | "Growth Analytics" sits inside the Growth pod |
| **Platform** | Data infrastructure & tooling | The team that owns the warehouse, pipelines, BI tool |
| **Enabling** | Data literacy & training | A small team that teaches PMs to self-serve |
| **Complicated-subsystem** | ML / specialized modeling | The fraud-detection or forecasting team |

**Think about your case context:** Which topology best describes your team? Most analytics orgs are a mix.

<!-- Talk track: Team Topologies is a book by Skelton and Pais that gives us a language for how teams relate to each other. I want you to think about these four types through an analytics lens. Stream-aligned teams are embedded — they sit inside a product squad and serve that squad directly. Platform teams build the infrastructure everyone depends on. Enabling teams exist to make other teams more capable — think data literacy programs. And complicated-subsystem teams handle genuinely hard technical problems like ML or forecasting. Look at your case context card. Which topology fits? If you're in the small startup context, you're probably one team doing everything. If you're in the large enterprise, you might have all four. -->

---

## The Manager OS Concept

Your **operating system** has four layers:

1. **Cadences** — the rhythm (daily / weekly / monthly / quarterly)
2. **Rituals** — the meetings and practices that fill those cadences
3. **Artifacts** — the documents that capture decisions and alignment
4. **Decision hygiene** — the meta-practices that keep decisions clean

Think of it like software: cadences are the scheduler, rituals are the processes, artifacts are the data store, and decision hygiene is the error-handling layer.

<!-- Talk track: Here's the core mental model for this block. Your Manager OS has four layers. Cadences are the clock — how often things happen. Rituals are the actual meetings and practices. Artifacts are the written documents that create shared memory. And decision hygiene is how you make sure decisions are actually good. I like the software analogy: cadences are your cron scheduler, rituals are your running processes, artifacts are your database, and decision hygiene is your error handling. Over the next ninety minutes, we're going to build out each layer for YOUR context. -->

---

## Cadences That Work

| Cadence | What happens | Why it matters |
|---|---|---|
| **Daily** | Async standup (Slack/Teams post) or skip entirely | Visibility without meetings |
| **Weekly** | 1:1s with each report + team sync | Course-correct fast; build trust |
| **Monthly** | Metrics review + mini-retro | Catch drift; celebrate wins |
| **Quarterly** | Planning + calibration + roadmap refresh | Strategic alignment; career growth |

**The rhythm creates predictability.** Your team should always know what's coming and never be surprised.

The biggest mistake new managers make: too many meetings with no rhythm. Pick a cadence and protect it.

<!-- Talk track: Let's start with cadences. Here are the four I recommend. Daily — and honestly, for most analytics teams, you can skip the daily standup or make it async. A Slack post is fine. Weekly is where the magic happens: your 1:1s and one team sync. Monthly, you zoom out and look at metrics — are we on track? And quarterly, you do real planning and calibration. The key insight is that the rhythm itself creates predictability. Your team should never wonder "when will I get to talk to my manager about this?" They should always know: Wednesday at 2pm. That predictability is a gift you give your team. -->

---

## 1:1s That Actually Work

**Structure (30 minutes):**
- **10 min** — Their agenda (what's on their mind?)
- **10 min** — Your agenda (context, feedback, asks)
- **10 min** — Career & growth (not every week, but regularly)

**Anti-patterns to avoid:**
- **The Status Update Trap** — "What did you do this week?" (Use async for this)
- **The Therapy Session** — Empathy is good, but you're not a therapist
- **The Canceled 1:1** — The fastest way to signal "you don't matter"
- **The Monologue** — If you're talking more than 50%, something's wrong

**Pro tip:** Keep a shared running doc. Both sides add agenda items before the meeting.

<!-- Talk track: The 1:1 is the single most important ritual in your Manager OS. Let me be blunt: if you cancel 1:1s regularly, you are failing as a manager. Here's a simple structure that works. First ten minutes are theirs — they set the agenda. Middle ten minutes are yours — context from leadership, feedback, specific asks. Last ten minutes are about their career and growth. Now, let me name the anti-patterns. The status update trap — don't use a 1:1 to ask "what did you do this week." That's what Slack is for. The therapy session — you should be empathetic, but if every 1:1 turns into emotional processing, something structural is wrong. And the canceled 1:1 — nothing says "you don't matter to me" faster. Who here has had a manager who regularly canceled 1:1s? How did that feel? -->

---

## Decision Logs & Memos

**Why writing beats meetings:**
- Writing forces clarity — you can't hand-wave in prose
- Writing scales — 50 people can read a memo; 50 people can't be in a meeting
- Writing creates institutional memory

**The 1-page Decision Memo:**

| Section | Purpose |
|---|---|
| **Context** | What situation prompted this decision? |
| **Options** | At least 3 options with pros/cons |
| **Recommendation** | Which option and why |
| **Risks** | What could go wrong and how we'd mitigate |
| **Decision Type** | Type 1 (irreversible) or Type 2 (reversible) |

**Default to Type 2.** Most decisions are reversible. Move fast on those. Slow down on Type 1.

<!-- Talk track: Jeff Bezos popularized the Type 1 / Type 2 framework. Type 1 decisions are one-way doors — hard or impossible to reverse. Type 2 decisions are two-way doors — you can walk back through if it doesn't work. Here's the insight: most decisions are Type 2, but organizations treat them all like Type 1. That's where bureaucracy comes from. Your job as a manager is to identify which type each decision is and set the right speed. For Type 2 decisions, empower your team to just go. For Type 1 decisions, write a memo. The act of writing a decision memo forces you to think clearly. You can't hide behind vague language when you have to write it down. We have a template for this that you'll use throughout the course. -->

---

## The Team Charter

**What it is:** A 1-2 page document that captures your team's identity and operating agreements.

**Sections:**
- **Purpose & Mission** — Why does this team exist? (2-3 sentences)
- **Scope & Boundaries** — What's in, what's explicitly out
- **Principles** — 3-5 operating rules the team lives by
- **Key Interfaces** — Who do you interact with and how?
- **Success Metrics** — How do you know if you're winning?

**Why it matters:** Alignment without constant re-negotiation. When someone asks "should we do X?" the charter helps answer.

**Example principle:** *"We ship insights, not dashboards. If an analysis doesn't lead to a decision, we ask why before starting it."*

<!-- Talk track: The Team Charter is the first artifact in your Manager OS. Think of it as your team's constitution. It answers the fundamental questions: why do we exist, what do we do, what don't we do, and how do we operate? Let me give you a real example. I once joined a team where every PM in the company felt entitled to ask for any analysis at any time. The team was drowning. We wrote a charter that said: "We serve the Growth and Monetization pods. Other teams submit requests through a quarterly intake process." That one sentence saved hundreds of hours. You're going to write your own charter in about fifteen minutes. Let me show you what the template looks like. -->

---

## The Stakeholder Map

**Power/Interest Grid:**

|  | **Low Interest** | **High Interest** |
|---|---|---|
| **High Power** | Keep Satisfied | Manage Closely |
| **Low Power** | Monitor | Keep Informed |

**For each stakeholder, capture:**
- Name/Role
- What they need from you
- What you need from them
- Engagement strategy (frequency + channel)

**The hidden stakeholders:** Don't forget IT, Legal/Privacy, Finance, and the engineers who maintain your pipelines. New managers always under-map.

<!-- Talk track: The stakeholder map is your relationship radar. This 2x2 grid comes from classic project management but it's incredibly useful for analytics managers. High power, high interest — these are your bread and butter stakeholders. You manage them closely. High power, low interest — these are dangerous. Think of the CFO who doesn't care about analytics until something goes wrong. You need to keep them satisfied. Low power, high interest — these are often your power users, the PMs who love data. Keep them informed. And low power, low interest — just monitor. Here's my biggest tip: new managers always under-map. They forget IT, Legal, Privacy, Finance. Those stakeholders will block you at the worst possible moment if you haven't built the relationship. -->

---

## RACI in 60 Seconds

| Letter | Meaning | Rule |
|---|---|---|
| **R** | Responsible — does the work | Can be multiple people |
| **A** | Accountable — owns the outcome | **Exactly one person per decision** |
| **C** | Consulted — input before the decision | Keep this list short |
| **I** | Informed — told after the decision | Default for most people |

**Common mistakes:**
- Everyone is "Consulted" on everything (consensus paralysis)
- No clear "A" (diffusion of responsibility)
- RACI for trivial decisions (overhead kills velocity)

**Use RACI for the 5-10 decisions that cause the most confusion.** Not for everything.

<!-- Talk track: RACI is one of those frameworks that people either love or hate. I'm going to teach you to use it well, which means using it sparingly. R is who does the work. A is who owns the outcome — and this is the critical one. There must be exactly one A per decision. If two people think they're accountable, nobody is. C is who you consult before deciding, and I is who you inform after. The biggest mistake I see is organizations that RACI everything. Don't do that. Pick the five to ten decisions that cause the most confusion or conflict, and RACI those. Things like: who decides our metrics definitions? Who approves a new dashboard going to production? Who decides if we take on a new stakeholder? Those deserve a RACI. "What color should the chart be?" does not. -->

---

## Activity: Draft Your Team Charter

**Time: 25 minutes** | Use the template provided

Using your chosen case context (Small / Medium / Large), draft a Team Charter.

**Your charter must include:**
1. **Purpose & Mission** — Why does this analytics team exist?
2. **Scope & Boundaries** — What's in scope? What's explicitly NOT?
3. **3 Operating Principles** — Rules your team lives by
4. **Key Interfaces** — At least 4 teams/roles you interact with
5. **Success Metrics** — 3-5 KPIs for your team's first year
6. **Cadences** — What meetings happen and when?

**Tip:** Be specific to your case context. A startup charter looks very different from an enterprise charter.

<!-- Talk track: All right, let's put this into practice. Open the Team Charter template — it's in your materials. You have 25 minutes. I want you to work individually, anchored to your case context. If you chose the small startup, your charter should reflect that reality — limited resources, scrappy, moving fast. If you chose the large enterprise, think about governance, compliance, cross-team coordination. Be specific. Don't write generic platitudes. "We value data quality" is not a principle. "Every metric has a documented definition and an owner before it goes to production" — that's a principle. I'll circulate and answer questions. Go. -->

---

## Activity: Map Your Stakeholders

**Time: 20 minutes** | Use the template provided

Map your stakeholders on the Power/Interest grid.

**Requirements:**
- Identify **at least 6 stakeholders** (roles, not names)
- For each, note:
  - Power level (High / Low)
  - Interest level (High / Low)
  - What they need from you
  - What you need from them
  - Your engagement strategy

**Prompts to jog your thinking:**
- Who funds your team?
- Who consumes your outputs?
- Who controls access to data or systems?
- Who could block your work if unhappy?
- Who do you depend on but rarely talk to?

<!-- Talk track: Excellent work on the charters. Now flip to the Stakeholder Map template. You have 20 minutes. I want at least six stakeholders, and I want you to really think about the ones you might miss. Here are some prompts. Who funds your team? That's probably a VP or C-suite — high power. Who consumes your outputs? Product managers, maybe marketing — high interest. Who controls your data access? That might be IT or engineering — and if you haven't built that relationship, you'll be blocked when you need a new data source. Who could kill your project if they got upset? Think Legal, Privacy, Compliance. Go deep here. This map will serve you for the rest of the course. -->

---

## Pair Share

**Time: 10 minutes (5 minutes each)**

Find a partner — ideally someone who chose a **different** case context.

**Share your stakeholder map and discuss:**
- Who are your "Manage Closely" stakeholders and why?
- Which stakeholder did you almost forget?
- Where do your maps differ because of your case contexts?

**Listen for:** assumptions your partner made that you didn't. Different contexts surface different blind spots.

<!-- Talk track: Okay, time's up on the individual work. Find a partner — and try to pair with someone who chose a different case context than you. You have five minutes each. Share your stakeholder map. I want you to focus on two things: first, who are your "manage closely" stakeholders and why? Second, which stakeholder did you almost leave off the map? That second question is the interesting one. The stakeholders we forget are often the ones who cause us the most trouble later. Go ahead, pair up. -->

---

## Debrief

**Let's hear from the room:**

- Who found a stakeholder they almost missed? What was it?
- Did anyone realize their case context changes WHO the key stakeholders are?
- What's one principle from your charter that you're genuinely proud of?

**Key insight:** The stakeholders you forget to map are usually the ones who block you later. The charter principles you're most proud of are usually the ones that will be hardest to enforce.

<!-- Talk track: Let's come back together. I want one volunteer — who found a stakeholder they almost missed? Tell us who it was and why you almost left them off. Great. Notice a pattern here — the stakeholders we overlook tend to be the ones with "quiet power." They don't show up in your daily work, but they control something critical. IT controls your infrastructure. Legal controls your data access. Finance controls your budget. Map them early, build the relationship before you need something. That's proactive management. -->

---

## Your Manager OS So Far

After this block, you have:

- [x] **A mental model** — Manager as system builder, not boss
- [x] **A Team Charter** — Purpose, scope, principles, interfaces, metrics
- [x] **A Stakeholder Map** — Power/Interest grid with engagement strategies
- [x] **A sense of cadences** — Daily/weekly/monthly/quarterly rhythms
- [x] **Decision hygiene basics** — Type 1 vs. Type 2, decision memos, RACI

These are the **foundation** of your Manager OS. Every block builds on this.

**Reminder:** Your Team Charter and Stakeholder Map are due as drafts at end of Day 1.

<!-- Talk track: Let's take stock of where we are. In 100 minutes, you've built the foundation of your Manager Operating System. You have a charter that defines your team's identity. You have a stakeholder map that shows your relationship landscape. You have a framework for cadences and a toolkit for making good decisions. This is not theoretical — these are artifacts you will refine and submit. Your charter and stakeholder map are due as drafts by end of today. They don't need to be perfect, but they need to be substantive. Over the remaining blocks, we'll layer on hiring, roadmapping, performance management, and infrastructure. Everything connects back to what you built today. -->

---

## Transition to Block B

**After lunch: Block B — Hiring & Team Formation (13:30–15:10)**

You have your charter. You know your stakeholders. Now the question becomes:

> **"Who do I need on my team to fulfill this charter?"**

**Think about over lunch:**
- What's the first role you'd hire for your case context?
- What skills matter most — technical depth, communication, domain knowledge?
- How would you know if a candidate is "right"?

See you at 13:30.

<!-- Talk track: We're breaking for lunch. When you come back at 1:30, we'll tackle hiring and team formation. Here's what I want you to think about while you eat. Look at your charter — look at the purpose, the scope, the success metrics. Now ask yourself: who do I need on this team to actually deliver on that charter? What's the first role you'd hire? Is it a senior analyst who can mentor juniors? A data engineer who can fix the pipeline mess? An analytics engineer who bridges the gap? We'll dig into structured hiring, work-sample design, and interview loops. Enjoy lunch, and I'll see you back here at 1:30. -->
