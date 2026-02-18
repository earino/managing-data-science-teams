---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 1 – Block C"
---

# Roadmaps, Bets, and Alignment

**Block C — 15:30-17:10 (100 minutes)**

**Learning Outcomes:**
- Build a 12-month roadmap tied to business outcomes
- Write a 2-page executive narrative
- Stress-test plans through structured red-team critique

<!-- Talk track: Welcome to the last block of Day 1. You have your Manager OS and your hiring plan. Now we answer the question every executive asks: where is this team going, and why should I fund it? By the end of this block you will have a roadmap, the start of an executive narrative, and you will have survived your first red-team exercise. We also have a hard stop at 17:10 for the Day 1 Checkpoint submission. -->

---

# Roadmaps Are Not Gantt Charts

A roadmap is a **communication tool**, not a project plan.

It answers: **"Where are we going and why?"**
It does NOT answer: "What's the exact timeline?"

> The map is not the territory.
> — Alfred Korzybski

A Gantt chart is a promise. A roadmap is a **bet register**.

<!-- Talk track: The single biggest mistake new analytics managers make is treating the roadmap like a project plan. A Gantt chart says we will deliver feature X on March 15th. A roadmap says we believe investing in churn modeling this quarter will reduce monthly churn by two percentage points, and here is why we believe that. If your roadmap has specific dates on it, you have built a Gantt chart and you will be held to those dates. Roadmaps communicate direction, priorities, and trade-offs. They are living documents that change as you learn. -->

---

# The Analytics Roadmap Structure

## Three Horizons

| Horizon | Timeframe | Commitment Level | Example |
|---------|-----------|-----------------|---------|
| **Now** | This quarter | Committed — actively staffed | Churn prediction model v1 |
| **Next** | Next quarter | Planned — scoped but flexible | Self-serve experimentation platform |
| **Later** | 6-12 months | Exploratory — directional only | Real-time personalization engine |

**Each item needs:**
- What it is
- Why it matters to the business (not to your team)
- Rough size (T-shirt: S/M/L/XL)
- Key dependencies

<!-- Talk track: The three-horizon model is the simplest roadmap structure that actually works. The Now column is what your team is actively building this quarter. These items are committed and staffed. The Next column is what you plan to do next quarter, scoped enough that you could start tomorrow if priorities shifted. The Later column is directional — it shows where you think the team is heading, but the details are intentionally vague. Each item must answer the question a VP would ask: why does this matter to the business? If you cannot articulate that, the item does not belong on the roadmap. -->

---

# RICE Prioritization

**A framework for comparing unlike things**

| Factor | Question | Scale |
|--------|----------|-------|
| **R**each | How many people or decisions does this affect? | # per quarter |
| **I**mpact | How much does it move the metric? | 0.25 / 0.5 / 1 / 2 / 3 |
| **C**onfidence | How sure are we about R, I, and E? | 100% / 80% / 50% |
| **E**ffort | How many person-months? | Person-months |

$$\text{RICE Score} = \frac{R \times I \times C}{E}$$

RICE is a **conversation starter**, not a calculator.

<!-- Talk track: RICE comes from Intercom and it is the most practical prioritization framework I have found for analytics teams. Reach is how many people, decisions, or dollars are affected. Impact is how much it moves the needle — use the scale, do not make up your own. Confidence is your honest assessment of how sure you are about the other estimates. And Effort is person-months of work. You divide the top by the bottom and get a score. But here is the important thing: the score is not the answer. The score is the starting point for a conversation. If the model says project A scores higher than project B but your gut says otherwise, that disagreement is the most valuable part of the exercise. Dig into it. -->

---

# North Star vs. Guardrails

```
                    ┌─────────────────┐
                    │  NORTH STAR     │
                    │  The ONE number  │
                    │  that captures   │
                    │  team value      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────┴─────┐ ┌─────┴─────┐ ┌─────┴─────┐
        │ GUARDRAIL │ │ GUARDRAIL │ │ GUARDRAIL │
        │ Must NOT  │ │ Must NOT  │ │ Must NOT  │
        │ get worse │ │ get worse │ │ get worse │
        └───────────┘ └───────────┘ └───────────┘
```

**North Star:** The one metric that best captures the value your team delivers.
**Guardrails:** Things that must NOT get worse while you optimize the North Star.
**Input metrics:** Things you can directly influence through your team's work.

<!-- Talk track: Every analytics team needs a North Star metric — the single number that best captures the value you deliver to the business. For a growth analytics team, it might be monthly active paying users. For a risk analytics team, it might be loss rate. The North Star gives your team focus. But optimizing one metric without constraints is dangerous. That is what guardrails are for. These are the metrics that must not get worse while you chase the North Star. If your North Star is revenue per user, your guardrails might be user satisfaction score, data quality SLA, and model fairness metrics. Without guardrails, you optimize yourself into a corner. -->

---

# The Metrics Tree

```
Business Outcome:     Revenue Growth
                          │
North Star:          Monthly Active Paying Users
                     ╱              ╲
Input Metrics:  Activation Rate    Retention Rate
                    │                    │
Team Activities: Onboarding         Churn modeling,
                 funnel analysis,    cohort analysis,
                 signup experiment   win-back targeting
```

**Draw yours.** Start from the business outcome your executive cares about. Work down to what your team can actually do.

The tree answers: **"How does my team's daily work connect to the number the CEO reports to the board?"**

<!-- Talk track: The metrics tree is the bridge between your team's daily work and the number the CEO reports to the board. Start at the top with the business outcome your executive sponsor cares about most. Then identify your North Star — the metric your team most directly influences. Break that into input metrics, the levers your team can actually pull. And at the bottom, list the specific team activities that move those input metrics. When a stakeholder asks why you are spending three weeks on churn modeling, you point to the tree. Churn modeling improves retention rate, which drives monthly active paying users, which drives revenue growth. If you cannot draw this tree, your roadmap is disconnected from the business. -->

---

# Communicating Trade-offs

## Frame as choices, not complaints

| Instead of... | Say... |
|---------------|--------|
| "We don't have enough resources" | "We can do A or B in Q1 — which creates more value?" |
| "That's not possible" | "Here's what it would cost: 6 weeks and we'd pause the churn model" |
| "The data isn't ready" | "We need 3 weeks of instrumentation before we can answer that question reliably" |

## The Cost of Delay

> "Every week we delay the experimentation platform costs us approximately $40K in unoptimized conversion — here's the math."

Product and Eng are your **partners**, not your opponents.

<!-- Talk track: One of the hardest skills for a new analytics manager is communicating trade-offs without sounding like you are complaining or saying no. The key is framing. Never say we do not have enough resources. Instead, present a choice: we can do A or B this quarter, which one creates more value for the business? This reframes you from a bottleneck into a strategic partner. The cost of delay is your most powerful tool here. If you can quantify what it costs the business to wait another week on a project, executives will prioritize for you. And remember: Product and Engineering are your partners. You are all trying to move the same business metrics. Approach every trade-off conversation as a joint problem-solving exercise, not a negotiation. -->

---

# The 2-Page Executive Narrative

## Structure

1. **Context** — Where we are (team, state, environment)
2. **What We Did** — Key wins and metrics moved
3. **What We Learned** — Insights and surprises
4. **What's Next** — Priorities and bets for next quarter
5. **What We Need** — Asks and blockers

**Written in prose, not bullet points.**

> Executives read narratives; teams read dashboards.

This is the document that gets forwarded to the CEO's CEO.

<!-- Talk track: The two-page executive narrative is the single most important document an analytics manager writes. It is not a status update. It is not a dashboard. It is a story about where your team is, what you have accomplished, what you have learned, and where you are going. It is written in prose because prose forces clarity of thought. Bullet points let you hide behind vague statements. When you write in complete sentences, you have to actually think about what you are saying. This is the document that your VP forwards to the C-suite. It is the document that gets read in the board meeting prep. Every word matters. -->

---

# Writing for Executives

## BLUF: Bottom Line Up Front

**Lead with the answer. Then provide the evidence.**

> **Bad:** "Over the past quarter, our team conducted extensive analysis of user behavior patterns across multiple segments, examining retention cohorts, engagement metrics, and conversion funnels. After careful analysis, we found that..."
>
> **Good:** "We reduced 30-day churn by 18% this quarter, saving an estimated $2.1M in annual revenue. Here's how."

### Rules

- No jargon. "We improved model AUC by 0.12" means nothing to a CFO.
- Quantify everything. Dollars, percentages, users affected.
- One page = one main idea. Do not cram.
- Write for the person who has 3 minutes and 47 unread emails.

<!-- Talk track: BLUF — Bottom Line Up Front — is a military communication concept that every analytics manager should internalize. Executives do not have time to read through your methodology to find the conclusion buried on page two. Lead with the answer. We reduced churn by 18 percent. Then explain how and why. No jargon means no jargon. If you write AUC or p-value in an executive narrative, you have failed. Translate everything into business language: dollars, users, time, risk. And remember who your reader is — someone with three minutes between meetings and 47 unread emails. Respect their time. -->

---

# Risk Registers

Every roadmap has risks. **Acknowledging them is not weakness — it is honest planning.**

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|
| Key data engineer leaves | Medium | High | Cross-train, document pipelines | You |
| Privacy regulation change | Low | High | Monthly legal sync, flexible architecture | Legal + You |
| Stakeholder priority shift | High | Medium | Quarterly roadmap reviews with VP | You |

### Your top 3 risks should be on slide 2 of every executive presentation.

Executives trust leaders who name risks before they become surprises.

<!-- Talk track: Every roadmap has risks, and the worst thing you can do is pretend they do not exist. A risk register is a simple table that forces you to name what could go wrong, assess how likely it is and how bad it would be, and document what you are doing about it. Your top three risks should appear on the second slide of every executive presentation — right after the summary, before the details. Why? Because executives trust leaders who name risks early. It shows you have thought about what could go wrong and you have a plan. Risks are not weaknesses. They are signs that you are planning honestly. An executive who is surprised by a risk will lose trust in you. An executive who was warned about a risk three months ago will respect your judgment. -->

---

# Activity: 12-Month Roadmap
## 30 minutes

**Build a 12-month roadmap for your case context.**

1. Define your **North Star metric** and **3 guardrail metrics**
2. Brainstorm at least **8 initiatives** your team could pursue
3. **RICE score** each initiative
4. Place initiatives in **Now / Next / Later** based on RICE scores and dependencies
5. Identify the **top 3 dependencies** that could block your plan

**Use the `roadmap-rice.md` template.**

Work individually, but talk to your case-context peers if you get stuck.

<!-- Talk track: This is the big activity for this block. You have 30 minutes to build a 12-month roadmap for your case context. Start by defining your North Star metric — what is the one number that best captures the value your team delivers? Then identify three guardrails. Next, brainstorm at least eight initiatives. Do not self-censor — get them all on paper first. Then RICE score each one. Finally, place them into Now, Next, and Later columns. Use the template I have provided. Work individually, but if you are stuck on what initiatives make sense for your case context, talk to the people at your table who chose the same context. I will be circulating to help. -->

---

# Activity: Executive Narrative Draft
## 15 minutes

**Write the first page of your 2-page executive narrative.**

Focus on two sections:
1. **Context** — Where your team is right now. Team size, current capabilities, business environment, key constraints.
2. **What's Next** — Your top 3 priorities for the next quarter and why they matter.

**Use the `exec-narrative.md` template.**

Write in **complete sentences**. No bullet points.
Imagine your reader is your VP's VP.

<!-- Talk track: Now take 15 minutes to write the first page of your executive narrative. Focus on Context and What is Next. Write in complete sentences — I know bullet points are tempting, but resist. Imagine your reader is two levels above you. They do not know the details of your team's daily work. They need to understand where you are and where you are going in about 90 seconds of reading. This draft will become part of your portfolio, and you will refine it further before the Day 2 QBR simulation. Do not try to make it perfect — get the structure and the key messages right. Polish comes later. -->

---

# Red-Team: Kill the Project
## 10 minutes

**Pair up with someone from a DIFFERENT case context.**

Your job: **find the fatal flaw** in their roadmap.

Ask:
- "What assumption, if wrong, kills this entire plan?"
- "What is the biggest risk you haven't identified?"
- "Which initiative has the lowest confidence score — and why is it still on the roadmap?"
- "If your headcount gets cut by one person, what falls apart?"

**Be constructive but ruthless.** The goal is to make the roadmap stronger, not to win an argument.

<!-- Talk track: This is my favorite exercise of the day. Pair up with someone who chose a different case context than yours. You have 10 minutes total — 5 minutes each direction. Your job is to find the fatal flaw in their roadmap. Ask the hard questions: what assumption, if wrong, kills this plan? What is the biggest risk they have not identified? If they lose one headcount, what breaks? Be constructive but do not pull your punches. The best feedback is specific and actionable. Do not just say the roadmap is unrealistic — say which initiative is unrealistic and why. This exercise simulates what will happen when you present your roadmap to your VP. Better to find the flaws now than in that meeting. -->

---

# Red-Team Debrief

**What survived? What didn't?**

- Which assumptions were most vulnerable?
- What risks did your partner identify that you missed?
- How did hearing a different case context's perspective change your thinking?

> "The best roadmaps get stronger through criticism."

**Update your roadmap and risk register** with what you just learned.
Take 3 minutes now to add at least one new risk or modify one initiative.

<!-- Talk track: Let us debrief. Raise your hand if your partner found a flaw you had not considered. Good — that is the point. The best roadmaps are not the ones that survive criticism unchanged. They are the ones that get stronger through criticism. Take three minutes right now to update your roadmap. Add at least one new risk to your risk register, or modify one initiative based on what your partner said. This is exactly what happens in real quarterly planning — you present your plan, smart people poke holes in it, and you make it better. The ability to accept and integrate critical feedback is one of the most important skills an analytics manager can develop. -->

---

# Day 1 Checkpoint

## Due by 17:10 today — HARD DEADLINE

**Submit three artifacts (all drafts — completeness, not polish):**

1. **Team Charter** (from Block A)
2. **Stakeholder Map** (from Block A)
3. **Roadmap Outline** with RICE scoring (from Block C)

**This is 10% of your grade — pass/fail on completeness.**

Upload to the LMS before you leave.
Missing sections are okay. Empty templates are not.

<!-- Talk track: Here is your hard deadline for today. By 17:10 — that is when this block ends — you need to submit three artifacts to the LMS. Your Team Charter from Block A, your Stakeholder Map from Block A, and your Roadmap Outline with RICE scoring from this block. These are all drafts. I am grading on completeness, not polish. If a section is rough, that is fine. If a section is empty, that is not fine. This checkpoint is worth 10 percent of your grade and it is pass-fail. Upload all three documents before you leave the room. If you are having technical issues with the LMS, email them to me directly before 17:10. -->

---

# What's Coming on Day 2

**Monday, March 23**

| Block | Topic | Key Activity |
|-------|-------|-------------|
| **D** (11:00) | Growth & Performance | Draft a PGP + calibration summary |
| **E** (13:30) | Data Infra & Vendors | Data infra blueprint + RFP scoring |
| **F** (15:30) | QBR Simulation | Present your roadmap to a mock exec panel |

### Before Day 2:
- **Refine your hiring packet draft** (due Thursday 23:59)
- **Read the QBR simulation brief** (posted on LMS tonight)
- Review your roadmap — Day 2 Block F uses it

<!-- Talk track: Here is what is coming on Day 2 next Monday. Block D covers growth and performance — you will draft a personal growth plan and a calibration-ready performance summary. Block E is about data infrastructure and vendor management — practical stuff about building your data stack. And Block F is the big one — the QBR simulation. You will present your roadmap and executive narrative to a mock executive panel, and they will ask you hard questions. Before Day 2, you have homework. Refine your hiring packet draft and submit it by Thursday at 23:59. I will use those drafts in the Day 2 role-plays. Also read the QBR simulation brief, which I will post on the LMS tonight. And review your roadmap — you will be presenting it. -->

---

# Close Day 1

**You now have the core of your Manager OS.**

- You have a **charter** that defines how your team operates
- You know your **stakeholders** and how to work with them
- You have a **hiring plan** to build the team you need
- You have a **roadmap** that connects your work to business outcomes
- You have the start of an **executive narrative** that tells the story

Day 2 is about **people, infrastructure, and presenting it all.**

> "Management is not about having all the answers. It's about building the system that finds them."

Thank you. See you on March 23.

<!-- Talk track: That is Day 1. Take a moment to appreciate what you have built today. You walked in this morning with a case context and an empty folder. You now have a team charter, a stakeholder map, the beginning of a hiring plan, a twelve-month roadmap with RICE scoring, and the first page of an executive narrative. That is the core of a Manager Operating System. On Day 2, we will add the people dimension — growth plans, performance management, difficult conversations — and the technical dimension — data infrastructure, vendor management, working with IT. And in the final block, you will present everything in a QBR simulation. Submit your checkpoint artifacts now, and I will see you on March 23. Have a good week. -->
