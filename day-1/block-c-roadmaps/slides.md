---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 1 – Block C"
---
<!-- ⏱ Expected: 15:30 (min 0/100) -->
<!-- _class: title -->

# Roadmaps, Bets, and Alignment

## Day 1 — Block C | 15:30–17:10

<!-- Talk track: Welcome to the last block of Day 1. You have your Manager OS and your hiring plan. Now we answer the question every executive asks: where is this team going, and why should I fund it? By the end of this block you will have a roadmap, the start of an executive narrative, and you will have survived your first red-team exercise. We also have a hard stop at 17:10 for the Day 1 Checkpoint submission. -->

---

<!-- ⏱ Expected: 15:30 (min 0/100) -->
## Learning Outcomes

By the end of this block you will be able to:
- Build a 12-month roadmap tied to business outcomes
- Write a 2-page executive narrative
- Stress-test plans through structured red-team critique

<!-- Talk track: Three outcomes for this block. You'll build a roadmap, start an executive narrative, and survive a red-team exercise. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## The Roadmap Problem

Why are roadmaps in analytics **uniquely hard**? You are not building features. You are building **capability and trust**.

- Stakeholders don't really understand what analytics teams do day to day
- Leadership asks **"What have you shipped?"** and you need a better answer than "dashboards"
- Your most impactful work is often invisible — the analysis that prevented a bad decision, the data quality fix that stopped a silent failure

**The roadmap is your tool for making the invisible visible.** Without one, you are at the mercy of whoever yells loudest.

<!-- Talk track: Roadmaps for analytics teams are fundamentally different. A product team ships features users can see. Your best work is often invisible — the analysis that prevented a bad launch, the data quality fix nobody noticed. The roadmap is your translation layer. Without one, you are at the mercy of whoever yells loudest. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## What Good Analytics Roadmaps Do

A good analytics roadmap is not a wish list. It is a **strategic tool**:

1. **Translate technical work into business language** — "We built a churn model" becomes "We identified $3.2M in at-risk revenue"
2. **Protect your team from drive-by requests** — Point to the roadmap and ask "Which priority should we pause?"
3. **Create mutual accountability** — You deliver outcomes; stakeholders provide data access, expertise, and executive air cover
4. **Force explicit trade-offs** — Instead of trying to do everything and doing nothing well, you make visible choices

<!-- Talk track: A good roadmap does four things. It translates your work into business language. It protects your team from drive-by requests. It creates mutual accountability. And it forces explicit trade-offs instead of implicit ones where your team burns out trying to do everything. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## Block C Roadmap

**What we'll build in the next 100 minutes:**

| Component | What It Is |
|-----------|-----------|
| **North Star + Guardrails** | Metrics that define success and boundaries |
| **RICE-scored initiatives** | A prioritized backlog of analytics bets |
| **Now / Next / Later roadmap** | A 12-month plan without false precision |
| **Executive narrative** | The document your VP forwards to the C-suite |
| **Red-team critique** | Stress-testing your plan before a real executive does |

You will leave with **a draft roadmap and an executive narrative** — artifacts that feed into your Day 2 QBR.

<!-- Talk track: Here is what we are building. North Star and guardrails, RICE-scored initiatives, a Now/Next/Later roadmap, an executive narrative, and a red-team exercise. Everything feeds into your Day 2 QBR, so treat this as a real draft. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## Roadmaps Are Not Gantt Charts

A roadmap is a **communication tool**, not a project plan.

It answers: **"Where are we going and why?"**
It does NOT answer: "What's the exact timeline?"

> The map is not the territory. — Alfred Korzybski

A Gantt chart is a promise. A roadmap is a **bet register**.

<!-- Talk track: The single biggest mistake new analytics managers make is treating the roadmap like a project plan. A Gantt chart says we will deliver feature X on March 15th. A roadmap says we believe investing in churn modeling this quarter will reduce monthly churn by two percentage points, and here is why we believe that. If your roadmap has specific dates on it, you have built a Gantt chart and you will be held to those dates. Roadmaps communicate direction, priorities, and trade-offs. They are living documents that change as you learn. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## The Gantt Chart Trap

Your VP of Marketing asks for a churn prediction model. You put it on your Gantt chart: **deliver by March 15**.

- **February:** The data is messier than expected — key event tables are missing mobile data.
- **March 1:** You tell Marketing it will slip two weeks. They already scheduled campaigns around March 15.
- **April 1:** The model ships. Good work. But Marketing already hired a consultant because they lost confidence.

**What went wrong?** You made a date-based commitment for work with **inherent uncertainty**.

<!-- Talk track: Analytics work has inherent uncertainty — you do not know what you will find in the data until you look. You promised March 15, the data was messy, and by the time you delivered in April, Marketing had lost confidence and hired a consultant. This is the Gantt chart trap. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## The Roadmap Alternative

**Instead of the Gantt chart promise, say this:**

> "Churn modeling is our top priority this quarter. We expect to deliver within Q1. Biggest risk is data completeness."

When the timeline shifts, you are **updating an estimate**, not **breaking a promise**.

Executives can handle uncertainty. What they cannot handle is being surprised.

<!-- Talk track: Now contrast the Gantt chart approach with a roadmap-style commitment. Churn modeling is our top priority this quarter. We expect to deliver within Q1. Biggest risk is data completeness. This is honest. When the timeline shifts, you are updating an estimate, not breaking a promise. The trust dynamics are completely different. Executives can handle uncertainty. What they cannot handle is being surprised. -->

---

<!-- ⏱ Expected: 15:37 (min 7/100) -->
## The Analytics Roadmap Structure

## Now / Next / Later

| Horizon | Timeframe | Commitment |
|---------|-----------|------------|
| **Now** | This quarter | Committed — actively staffed |
| **Next** | Next quarter | Planned — scoped but flexible |
| **Later** | 6-12 months | Exploratory — directional only |

<!-- Talk track: The three-horizon model is the simplest roadmap structure that actually works. The Now column is what your team is actively building this quarter. These items are committed and staffed. The Next column is what you plan to do next quarter, scoped enough that you could start tomorrow if priorities shifted. The Later column is directional — it shows where you think the team is heading, but the details are intentionally vague. -->

---

<!-- ⏱ Expected: 15:37 (min 7/100) -->
## Horizons: Examples

| Horizon | Example |
|---------|---------|
| **Now** | Churn prediction model v1 |
| **Next** | Self-serve experimentation platform |
| **Later** | Real-time personalization engine |

Commitment decreases from Now to Later. This protects you from the Gantt chart trap.

<!-- Talk track: The key insight is that commitment level decreases as you move from Now to Later. You are making strong promises about Now, tentative plans for Next, and directional bets for Later. This is honest and it protects you from the Gantt chart trap we just discussed. -->

---

<!-- ⏱ Expected: 15:42 (min 12/100) -->
## What Each Roadmap Item Needs

**Every item on your roadmap must answer these questions:**

- **What it is** — a clear, jargon-free description
- **Why it matters to the business** (not to your team) — connect it to revenue, retention, risk, or strategic advantage
- **Rough size** (T-shirt: S/M/L/XL) — enough to understand trade-offs, not enough to be held to a date
- **Key dependencies** — what has to be true for this to succeed

**The test:** Can a VP read this item and understand why it matters without asking a follow-up question? If not, rewrite it.

<!-- Talk track: Each item must answer why it matters to the business — not to your team. T-shirt sizing gives enough info for trade-offs without false precision. Dependencies must be visible. The VP test: can someone two levels above you understand this without a follow-up question? -->

---

<!-- ⏱ Expected: 15:42 (min 12/100) -->
## RICE Prioritization

**A framework for comparing unlike things**

| Factor | Question | Scale |
|--------|----------|-------|
| **R**each | How many people/decisions affected? | # per quarter |
| **I**mpact | How much does it move the metric? | 0.25 / 0.5 / 1 / 2 / 3 |
| **C**onfidence | How sure are we about R, I, and E? | 100% / 80% / 50% |
| **E**ffort | How many person-months + compute costs? | Person-months (adjusted) |

$$\text{RICE Score} = \frac{R \times I \times C}{E}$$

<!-- Talk track: RICE comes from Intercom. Reach is how many people or dollars are affected. Impact is how much it moves the needle. Confidence is your honest assessment. Effort is person-months plus compute costs — GPU training and LLM API costs can dwarf labor. The real value is the conversation it forces: when you cannot estimate Reach, that tells you to do more discovery. -->

---

<!-- ⏱ Expected: 15:42 (min 12/100) -->
## RICE as a Conversation Starter

RICE is a **conversation starter**, not a calculator.

- If Project A scores higher but your gut disagrees — **explore that disagreement**
- Is your gut wrong, or is the scoring missing something?
- RICE makes hidden assumptions **explicit** and **debatable**

The score does not make the decision. **You** make the decision.

<!-- Talk track: Here is the important thing about RICE: the score is not the answer. The score is the starting point for a conversation. If the model says project A scores higher than project B but your gut says otherwise, that disagreement is the most valuable part of the exercise. Dig into it. Maybe your gut is picking up on a dependency the score does not capture. Maybe your confidence estimate is too generous. The point is not to let a formula make your decisions. The point is to make your reasoning visible so other people can challenge it. -->

---

<!-- ⏱ Expected: 15:42 (min 12/100) -->
## RICE in Practice

**Four initiatives scored head-to-head:**

| Initiative | Reach | Impact | Confidence | Effort | Score |
|-----------|-------|--------|------------|--------|-------|
| Churn Model v1 | 5,000 users/qtr | 2 (high) | 80% | 3 PM | **2,667** |
| Self-Serve Dashboard | 200 decisions/qtr | 1 (med) | 100% | 2 PM | **100** |
| Experimentation Platform | 10,000/qtr | 3 (massive) | 50% | 6 PM | **2,500** |
| Data Quality Audit | 50,000/qtr | 0.5 (low) | 100% | 1 PM | **25,000** |

**The Data Quality Audit wins?** Unsexy work scores highest — it touches everything and is cheap.

<!-- Talk track: Four initiatives head-to-head. The Data Quality Audit scores highest because it touches everything and costs one person-month. The unsexy work wins — that is RICE working as intended, challenging your assumptions about what is most valuable. -->

---

<!-- ⏱ Expected: 15:42 (min 12/100) -->
## RICE in Practice: Sensitivity

**Drop Experimentation Platform confidence to 30%:** score falls from 2,500 to **1,500**. Does that change your Q1 plan?

RICE tells you **where to argue**, not what to decide.

<!-- Talk track: Now watch what happens when you adjust confidence on the Experimentation Platform from fifty to thirty percent. The score drops from twenty-five hundred to fifteen hundred. Does that change your Q1 plan? These are the conversations RICE is designed to provoke. RICE tells you where to argue, not what to decide. -->

---

<!-- ⏱ Expected: 15:48 (min 18/100) -->
## North Star Metric

The ONE number that captures your team's value to the business.

```
  NORTH STAR
  ┌───┼───┐
  G1  G2  G3
```

**G1, G2, G3** = Guardrails that constrain how you pursue it.

<!-- Talk track: Every analytics team needs a North Star metric — the single number that best captures the value you deliver to the business. For a growth analytics team, it might be monthly active paying users. For a risk analytics team, it might be loss rate. The North Star gives your team focus. Below the North Star sit your guardrails. These are the metrics that must not get worse while you pursue your North Star. -->

---

<!-- ⏱ Expected: 15:48 (min 18/100) -->
## Guardrails Protect the North Star

**Guardrails** are the metrics that must NOT get worse while you optimize the North Star. Optimizing one metric without constraints is dangerous.

**Example — Growth Analytics Team:**
- **North Star:** Monthly Active Paying Users
- **Guardrails:** User satisfaction score, data quality SLA, model fairness metrics

Guardrails prevent you from gaming your own North Star.

<!-- Talk track: Guardrails are the metrics that must not get worse while you chase the North Star. If your North Star is revenue per user, your guardrails might be user satisfaction and data quality SLA adherence. Without guardrails, you optimize yourself into a corner. -->

---

<!-- ⏱ Expected: 15:48 (min 18/100) -->
## North Star, Guardrails, and Input Metrics

**Example — Growth Analytics Team:**
- **North Star:** Monthly Active Paying Users — the one metric that captures your team's value
- **Guardrails:** User satisfaction, data quality SLA, model fairness — must NOT get worse
- **Input Metrics:** Activation rate, 30-day retention, reactivation rate — levers you can pull

Without input metrics, you have a North Star you cannot steer toward.

<!-- Talk track: The North Star is the number your team rallies around. Guardrails constrain how you pursue it. Input metrics are the levers your team can actually pull — activation rate, retention rate. Without input metrics, you have a destination but no steering wheel. -->

---

<!-- ⏱ Expected: 15:48 (min 18/100) -->
## Choosing Your North Star: Common Mistakes

- **Vanity metric** — "Number of dashboards created" feels productive but drives no business outcome
- **Uninfluenceable metric** — "Total company revenue" is important but your 4-person team cannot move it
- **Slow-moving metric** — "Annual customer lifetime value" takes 12 months to know if you moved it
- **Unmeasurable metric** — "Quality of analytical insights" sounds great but how do you track it?

<!-- Talk track: Four common mistakes. Vanity metrics that feel productive but drive no outcome. Metrics you cannot influence. Metrics that move too slowly to steer by. And metrics you cannot actually measure. -->

---

<!-- ⏱ Expected: 15:48 (min 18/100) -->
## The North Star Test

Ask three questions:

1. **Can your team directly influence it?** If not, it is someone else's North Star.
2. **Does it move when you do good work?** If not, wrong metric.
3. **Does leadership care about it?** If your VP's eyes glaze over, pick a different one.

If you answer yes to all three, you have your North Star.

<!-- Talk track: The test is simple. Three questions. Can your team directly influence it? Does it move when you do good work? Does leadership care about it? If the answer to all three is yes, you have found your North Star. If any answer is no, keep looking. Do not settle for a metric that fails even one of these tests — it will steer your team in the wrong direction for an entire quarter before you realize the problem. -->

---

<!-- ⏱ Expected: 15:48 (min 18/100) -->
## The Metrics Tree

```
Revenue Growth
      │
Active Paying Users
   ╱       ╲
Activation  Retention
```

**Draw yours.** Start from the business outcome and work down.

<!-- Talk track: The metrics tree is the bridge between your team's daily work and the number the CEO reports to the board. Start at the top with the business outcome your executive sponsor cares about most. Then identify your North Star. Break that into input metrics, the levers your team can actually pull. -->

---

<!-- ⏱ Expected: ~15:48 (min 18/100) | SKIP — advance past -->
<!-- _class: skip -->

## The Metrics Tree

```
Activation         Retention
    │                  │
Onboarding         Churn modeling,
funnel analysis    cohort analysis
```

The tree answers: **"How does my work connect to the board number?"**

<!-- Talk track: At the bottom, list the specific activities that move those input metrics. When a stakeholder asks why you are spending three weeks on churn modeling, you point to the tree. If you cannot draw this tree, your roadmap is disconnected from the business. -->

---

<!-- ⏱ Expected: 15:52 (min 22/100) -->
<!-- _class: skip -->

## Communicating Trade-offs: Frame as Choices

| Instead of... | Say... |
|---------------|--------|
| "We don't have enough resources" | "We can do A or B this quarter — which creates more value?" |
| "That's not possible" | "Here's what it would cost: 6 weeks and we'd pause the churn model" |
| "The data isn't ready" | "We need 3 weeks of instrumentation before we can answer that reliably" |

**Quantify the cost of waiting.** Product and Eng are your **partners** — approach every trade-off as a joint problem-solving exercise.

<!-- Talk track: Frame trade-offs as choices, not complaints. Never say "we can't" — instead say "here's what it would cost." Quantify cost of delay. And remember: Product and Engineering are partners, not opponents. -->

---

<!-- ⏱ Expected: ~15:52 (min 22/100) | SKIP — advance past -->
<!-- _class: cut -->

## The Trade-off Conversation: Setup

**Scenario:** Your team is building a churn model (top Q1 priority). The VP of Product walks in: "We need a dashboard for the new feature launch this week."

**The wrong way:**
> "We don't have bandwidth right now."

*Why this fails:* The VP hears "no" and goes around you.

<!-- Talk track: Let me script out how this actually sounds in practice. Your VP of Product shows up wanting a dashboard for a feature launch. This happens every week in every analytics team. The wrong way is to say we do not have bandwidth. That is a wall. The VP hears no, gets frustrated, and either goes around you or escalates to your boss. Either way, you lose. -->

---

<!-- ⏱ Expected: ~15:52 (min 22/100) | SKIP — advance past -->
<!-- _class: skip -->

## The Trade-off Conversation: The Right Way

> "Absolutely — let me show you what that would involve. We have three options:
> 1. **Pause churn model for 1 week** — dashboard this week, churn model slips to mid-April.
> 2. **Quick version now, full version later** — basic Looker view today, covers 80% of what you need.
> 3. **Next sprint** — Churn model on schedule, dashboard starts March 24.
>
> Which works best for your launch timeline?"

*Why this works:* You said yes, presented costs, and made it their choice.

<!-- Talk track: Start with "absolutely" — that is a yes. Lay out options with real costs. You never said no. You made the trade-off visible and made it their decision. Nine times out of ten the VP picks option two or three, and you are a strategic partner, not a bottleneck. -->

---

<!-- ⏱ Expected: 15:55 (min 25/100) -->
## The 2-Page Executive Narrative

1. **Context** — Where we are (team, state, environment)
2. **What We Did** — Key wins and metrics moved
3. **What We Learned** — Insights and surprises
4. **What's Next** — Priorities and bets for next quarter
5. **What We Need** — Asks and blockers

**Written in prose, not bullet points.** This is the document that gets forwarded to the CEO's CEO.

> Executives read narratives; teams read dashboards.

<!-- Talk track: The two-page executive narrative is the most important document an analytics manager writes. Five sections, written in prose — not bullets. Prose forces clarity of thought. This is the document your VP forwards to the C-suite. Every word matters. -->

---

<!-- ⏱ Expected: 15:55 (min 25/100) -->
## Executive Narrative: Context

**A condensed example for a fictional analytics team at MarketBridge:**

**Context:** "The Analytics team (5 ICs, 1 manager) supports MarketBridge's two-sided marketplace connecting homeowners with service professionals across 12 metro areas. This quarter we operated at full capacity following the successful onboarding of two analysts hired in Q3."

*What makes this work: concrete numbers, no jargon, establishes scope in three sentences.*

<!-- Talk track: Let me show you what each section looks like when it is done well. This is a condensed example for a fictional analytics team at MarketBridge, the two-sided marketplace. Look at the Context section — three sentences, and you know the team size, what they support, and where they stand. No jargon. -->

---

<!-- ⏱ Expected: 15:55 (min 25/100) -->
## Executive Narrative: Results

**What We Did:** "We reduced 60-day logo churn from 8.2% to 6.1% by deploying a propensity model that flags at-risk accounts 30 days before renewal. Customer Success now reviews the top 50 at-risk accounts weekly — 34 of 41 flagged accounts renewed."

*What makes this work: one clear outcome, quantified before and after, shows who uses it and how.*

<!-- Talk track: The What We Did section has one clear outcome with before and after numbers, and it shows who actually uses the work. Customer Success reviews the top fifty at-risk accounts weekly — that shows your work is integrated into a real business process, not sitting on a shelf. -->

---

<!-- ⏱ Expected: 15:55 (min 25/100) -->
## Executive Narrative: Insights

**What We Learned:** "Our biggest surprise was that product usage intensity is a weaker churn predictor than support ticket sentiment. Accounts that file frustrated tickets — even if they use the product daily — churn at 3x the rate."

*What makes this work: a genuine insight that changes how leadership thinks about the business.*

<!-- Talk track: The What We Learned section is where most narratives fall flat. People write platitudes. This example shares a genuine surprise — product usage intensity is a weaker churn predictor than support ticket sentiment. That is the kind of insight that makes a VP lean forward. -->

---

<!-- ⏱ Expected: 15:55 (min 25/100) -->
## Executive Narrative: Plans

**What's Next:** "In Q2, we are investing in self-serve reporting for the Sales team. Currently, 40% of our ad hoc requests come from Sales asking the same five questions. Automating this frees ~1.5 analyst-months per quarter."

*What makes this work: clear priority, quantified opportunity cost, explains the why.*

<!-- Talk track: The What is Next section explains the priority, quantifies the opportunity cost in analyst-months, and explains why this is the highest-leverage investment. Every section earns the reader's attention by being specific, quantified, and connected to business outcomes. -->

---

<!-- ⏱ Expected: 15:55 (min 25/100) -->
## Executive Narrative: Asks

**What We Need:** "We need Engineering to prioritize the event schema migration by April 15. Without it, our experimentation platform — the top Q3 initiative — cannot reliably track treatment assignment."

*What makes this work: specific ask, specific date, explains the consequence of not getting it.*

<!-- Talk track: And What We Need is a specific, dated ask with a clear consequence. Not we need more resources, but we need the event schema migration by April fifteenth or our Q3 initiative is blocked. Notice the pattern: specific, quantified, and connected to business outcomes. -->

---

<!-- ⏱ Expected: 16:00 (min 30/100) -->
## Writing for Executives: BLUF

## Bottom Line Up Front

**Lead with the answer. Then provide the evidence.**

> **Bad:** "Our team conducted extensive analysis of user behavior patterns across multiple segments..."

> **Good:** "We reduced 30-day churn by 18%, saving $2.1M. Here's how."

<!-- Talk track: BLUF — Bottom Line Up Front — is a military communication concept that every analytics manager should internalize. Executives do not have time to read through your methodology to find the conclusion buried on page two. The bad example buries the lead under a pile of process description. The good example takes six seconds to read and communicates the most important information immediately. That is respect for your reader's time. -->

---

<!-- ⏱ Expected: 16:00 (min 30/100) -->
## Rules for Executive Writing

1. **No jargon.** "We improved model AUC by 0.12" means nothing to a CFO. Say: "Our model now correctly identifies 85% of at-risk accounts, up from 73%."
2. **Quantify everything.** Dollars, percentages, users affected. "Significant improvement" is not a number.
3. **One page = one main idea.** If you need more space, you need fewer ideas per page.
4. **Write for the person who has 3 minutes and 47 unread emails.** Every sentence must earn its place.

<!-- Talk track: Four rules. No jargon — if you write AUC in an executive narrative, you have failed. Quantify everything. One page, one main idea. And write for the person with three minutes between meetings. Every sentence must earn its place. -->

---

<!-- ⏱ Expected: 16:03 (min 33/100) -->
## Risk Registers

Every roadmap has risks. **Acknowledging them is not weakness — it is honest planning.**

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Key data engineer leaves | Medium | High | Cross-train, document pipelines |
| Privacy regulation change | Low | High | Monthly legal sync, flexible architecture |
| Stakeholder priority shift | High | Medium | Quarterly roadmap reviews with VP |

Your top 3 risks should be on slide 2 of every executive presentation. Executives trust leaders who name risks before they become surprises.

<!-- Talk track: A risk register forces you to name what could go wrong. Your top three risks should appear on slide two of every executive presentation — right after the summary. Executives trust leaders who name risks early. -->

---

<!-- ⏱ Expected: 16:05 (min 35/100) | Activity brief — Roadmap; activity starts at 16:06 -->
<!-- _class: divider -->

## Activity: 12-Month Roadmap

## 30 Minutes | `templates/roadmap-rice.md`

<!-- Talk track: Time for the big activity. You have 30 minutes to build a 12-month roadmap. Open the template — let's go. -->

---

<!-- ⏱ Expected: 16:05 (min 35/100) | Activity brief — Roadmap; activity starts at 16:06 -->
## Activity: 12-Month Roadmap

**30 minutes — Build a 12-month roadmap for your case context.**

1. Define your **North Star metric** and **3 guardrail metrics**
2. Brainstorm at least **8 initiatives**
3. **RICE score** each initiative
4. Place initiatives in **Now / Next / Later** based on scores and dependencies
5. Identify **top 3 dependencies** that could block your plan

**Use the `roadmap-rice.md` template.** Work individually, but talk to case-context peers if stuck.

<!-- Talk track: You have 30 minutes. Define your North Star and guardrails. Brainstorm at least eight initiatives — do not self-censor. RICE score each one. Place them into Now, Next, and Later. Use the template. I will circulate to help. -->

---

<!-- ⏱ Expected: 16:36 (min 66/100) | Activity brief — Exec Narrative; activity starts at 16:37 -->
<!-- _class: divider -->

## Activity: Executive Narrative Draft

## 20 Minutes | `templates/exec-narrative.md`

<!-- Talk track: Next activity. You'll write the first page of your executive narrative. Open the template. -->

---

<!-- ⏱ Expected: 16:36 (min 66/100) | Activity brief — Exec Narrative; activity starts at 16:37 -->
## Activity: Executive Narrative Draft

**20 minutes — Write the first page of your 2-page executive narrative.**

Focus on two sections:
1. **Context** — Team size, capabilities, business environment, key constraints.
2. **What's Next** — Top 3 priorities for next quarter and why they matter.

**Use the `exec-narrative.md` template.** Write in **complete sentences** — no bullet points. Imagine your reader is your VP's VP. Do not try to make it perfect — get the structure and key messages right.

<!-- Talk track: Twenty minutes. Focus on Context and What is Next. Write in complete sentences — bullets are tempting but resist. This draft feeds into your Day 2 QBR. Polish comes later. -->

---

<!-- ⏱ Expected: 16:57 (min 87/100) | Red-Team brief; exercise starts at 16:58 -->
<!-- _class: divider -->

## Activity: Red-Team Exercise

## 8 Minutes | Pair Up Cross-Context

<!-- Talk track: My favorite exercise of the day. Pair up with someone from a different case context. Your job: find the fatal flaw. -->

---

<!-- ⏱ Expected: 16:57 (min 87/100) | Red-Team brief; exercise starts at 16:58 -->
## Red-Team: Kill the Project

**8 minutes — Pair up with someone from a DIFFERENT case context.**

Your job: **find the fatal flaw** in their roadmap. Ask these questions:
- "What assumption, if wrong, kills this plan?"
- "What is the biggest risk you haven't identified?"
- "Which initiative has the lowest confidence — why is it there?"
- "If you lose one headcount, what falls apart?"

<!-- Talk track: Pair up with someone from a different case context. Eight minutes — four each direction. Find the fatal flaw. Be constructive but do not pull your punches. This simulates what happens when you present to your VP. Better to find the flaws now. -->

---

<!-- ⏱ Expected: 17:06 (min 96/100) | Debrief (1 min) -->
## Red-Team Debrief

**What survived? What didn't?**

- Which assumptions were most vulnerable?
- What risks did your partner identify that you missed?
- How did a different perspective change your thinking?

**Jot down at least one new risk or one initiative to modify before you forget.** Update your roadmap and risk register after class.

> "The best roadmaps get stronger through criticism."

<!-- Talk track: Raise your hand if your partner found a flaw you had not considered. Good — that is the point. Take thirty seconds to jot down the key insight. You will update your roadmap after class — this is exactly what happens in real quarterly planning. -->

---

<!-- ⏱ Expected: 17:07 (min 97/100) | Checkpoint upload + Close -->
## Day 1 Checkpoint

## Due by 17:10 — HARD DEADLINE

**Submit three artifacts (drafts — completeness, not polish):**

1. **Team Charter** (Block A)
2. **Stakeholder Map** (Block A)
3. **Roadmap Outline** with RICE scoring (Block C)

**This is 10% of your grade — pass/fail on completeness.** Upload to the LMS before you leave. Missing sections are okay. Empty templates are not.

<!-- Talk track: By 17:10 you need to submit three artifacts. These are drafts — I am grading on completeness, not polish. If a section is rough, fine. If it is empty, not fine. This checkpoint is worth 10 percent of your grade, pass-fail. Upload before you leave the room. -->

---

<!-- ⏱ Expected: 17:07 (min 97/100) | Checkpoint upload + Close -->
## What's Coming on Day 2

**Monday, March 23**

| Block | Topic | Activity |
|-------|-------|----------|
| **D** (11:00) | Growth & Performance | PGP + calibration |
| **E** (13:30) | Infrastructure & Cross-Functional Interfaces | Data stack + build vs. buy |
| **F** (15:30) | Leading Up & Executive Communication | Exec frameworks + async QBR |

**Before Day 2:** Continue your hiring packet, draft your PGP, and review your roadmap.

<!-- Talk track: Day 2 next Monday. Block D is growth and performance. Block E is infrastructure — data stacks, build versus buy, working with engineering and IT. Block F is executive communication — leading up, handling failure, and your async QBR. Before then: continue your hiring packet, draft your PGP, and review your roadmap. -->

---

<!-- ⏱ Expected: 17:07 (min 97/100) | Checkpoint upload + Close -->
<!-- _class: divider -->

## Day 1 Complete

## See You on March 23

<!-- Talk track: That wraps Day 1. Let's take a moment to look at what you've built. -->

---

<!-- ⏱ Expected: 17:07 (min 97/100) | Checkpoint upload + Close -->
## Close Day 1

**You now have the core of your Manager OS.**

- You have a **charter** that defines how your team operates
- You know your **stakeholders** and how to work with them
- You have a **hiring plan** to build the team you need
- You have a **roadmap** that connects your work to business outcomes

Day 2 is about **people, refinement, and presenting it all.**

> "Management is not about having all the answers. It's about building the system that finds them."

<!-- Talk track: You walked in this morning with a case context and an empty folder. You now have a team charter, a stakeholder map, a hiring plan, a roadmap, and an executive narrative. That is the core of a Manager OS. Day 2 adds the people dimension, infrastructure planning, and executive communication. Submit your checkpoint artifacts now. See you on March 23. -->
