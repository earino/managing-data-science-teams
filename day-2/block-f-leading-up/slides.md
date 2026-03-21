---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 2 – Block F"
---
<!-- ⏱ Expected: 15:30 (min 0/100) -->
<!-- _class: title -->

# Leading Up & Executive Communication

## Day 2 — Block F | 15:30–17:10

<!-- Talk track: Welcome to the final block. Everything you've built over these two days — the Manager OS, the hiring packet, the roadmap, the growth plans, the infrastructure plan — it all converges here. This block is about leading up: communicating with executives who have limited time and broad scope, handling failure honestly, and practicing the opening of your capstone QBR. -->

---

<!-- ⏱ Expected: 15:30 (min 0/100) -->
## The Final Block

Over two days, you have:

- **Built a Manager OS** — cadences, rituals, decision hygiene
- **Hired a team** — structured interviews and work samples
- **Planned a roadmap** — RICE scoring and executive alignment
- **Grown your people** — PGPs, SBI feedback, calibration
- **Assessed your infrastructure** — build vs. buy, XFN SLAs, data stack planning

Now you learn to **communicate it all to leadership**. This skill separates analytics managers who **get funded** from those who **get cut**.

<!-- Talk track: Take a breath and look at how far you've come. You've built more management artifacts in two days than most new managers create in their first six months. But none of it matters if you can't communicate it to the people who control your budget, your headcount, and your team's survival. This block is where you learn that skill. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) | IC-to-Manager Shift + Exec Communication (12 min) -->
## The Shift: IC Communication → Manager Communication

You just got promoted. Everything about how you communicate upward changes.

<!-- _class: compact -->

| | Senior IC | Manager |
|---|---|---|
| **You present** | Your own analysis | Your team's impact |
| **You're judged on** | Quality of your work | Outcomes your team produces |
| **Your audience cares about** | Methodology, rigor | Business impact, risk, cost |
| **Your ask is** | "Here's what I found" | "Here's what my team needs" |
| **When it goes wrong** | You fix it | You explain it and own it |

<!-- Talk track: Before we get into frameworks, let me name the shift that nobody talks about. As a senior IC, you communicated up by presenting your analysis. Your audience cared about your methodology, your rigor, your findings. You were judged on the quality of YOUR work. As a manager, everything changes. You're presenting your team's impact, not your own analysis. Your audience cares about business outcomes, not methodology. Your ask is no longer "here's what I found" but "here's what my team needs." And when something goes wrong — when the dashboard is broken, when the model fails — you don't fix it yourself. You explain it and own it. That shift is why every framework in this block exists. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## Why Executive Communication Is a Survival Skill

Analytics teams that can't communicate their value **get cut**. The work **does not speak for itself** — you speak for the work.

Every budget cycle, every reorg, someone asks:

> "What does the analytics team actually do?"

Your answer determines your team's future.

<!-- Talk track: I want to be direct about why this matters. Analytics teams get cut. It happens all the time. Not because the work isn't valuable — but because the team couldn't articulate its value in terms the business understood. Every budget cycle, someone asks "what does analytics actually do?" Your answer to that question determines whether your team grows or gets absorbed into engineering. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## Executive Communication: Frameworks

**The Pyramid Principle:** Conclusion first, then supporting arguments, then data.

**BLUF (Bottom Line Up Front):** Always lead with the answer. "We're on track, but I need to flag two risks" is better than a 10-minute buildup.

Here's a test: if an executive read **only your first sentence**, would they know your main message? If not, restructure.

<!-- Talk track: The Pyramid Principle comes from Barbara Minto at McKinsey. Start with the conclusion, then supporting arguments, then data if asked. BLUF is the military version of the same idea. Here's why this is hard for you specifically: your academic training taught you to build from methodology to conclusion. Executives want the opposite — conclusion first, evidence on request. Unlearning the academic structure is the single hardest communication habit to break. You practiced BLUF in Day 1 for your executive narrative, and in Block E when you wrote your VP proposal. Now we're going deeper. -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## The Executive Attention Budget

Executives make **30–50 decisions per day**. Your QBR is one of many.

- If you **front-load** the most important information, you're respecting their cognitive load
- If you **build up slowly**, you'll lose them by slide 3
- If you **bury the ask**, they'll move on before they get to it

**The 5-minute version of your presentation should be just as compelling as the 15-minute version.** Your first two slides carry the entire narrative. Everything after that is supporting evidence you can skip.

<!-- Talk track: They make 30 to 50 decisions a day. By the time they get to your QBR, they've already made twenty decisions. They're not being rude when they check their phone — they're cognitively depleted. Your job is to make it easy for them. Front-load everything. Plan for five minutes — if you get fifteen, great, use it for depth. But if someone says "can you do it in five?" your answer has to be "yes." -->

---

<!-- ⏱ Expected: 15:32 (min 2/100) -->
## What Executives Actually Want to Know

Every executive presentation should answer **three questions:**

1. **Are we on track?**
   Status against goals, metrics, timeline
2. **What are the risks?**
   What could go wrong, what's already going wrong, what you're doing about it
3. **What do you need from me?**
   Decisions, resources, air cover, or nothing ("nothing" is a valid answer)

**Everything else is context.** Put these three answers on your first slide.

<!-- Talk track: There are exactly three things executives want to know. First: are we on track? Give me a color — green, yellow, red. Don't make me guess. Second: what are the risks? Don't hide bad news. Executives hate surprises more than they hate bad news. If your model is underperforming, say so and say what you're doing about it. Third: what do you need from me? This is the one people forget. Executives want to help — they want to unblock you. But you have to ask. If you don't need anything, say "no asks this quarter" — that's actually reassuring. -->

---

<!-- ⏱ Expected: 15:40 (min 10/100) | Anti-Patterns + Managing Up (6 min) -->
<!-- _class: compact -->
## The Anti-Patterns of Exec Presentations

Common failure modes — you will see all of these:

- **"Data Dump"** — 50 slides of metrics with no narrative. Executives don't want data; they want judgment.
- **"Everything Is Fine"** — No risks acknowledged = no trust earned.
- **"Ask Buried on Slide 47"** — If you need something, say it upfront.
- **"Jargon Wall"** — Every unexplained acronym is a moment the executive checks out.
- **"But First, Methodology"** — No one in the C-suite cares about your SQL. They care what it means for the business.

<!-- Talk track: Let me show you the failure modes. The data dump is the most common — someone pastes fifty charts into a deck and calls it a QBR. There's no narrative, no "so what." The "everything is fine" deck destroys trust — every team has risks, and if you don't acknowledge yours, the exec assumes you're hiding them. The buried ask — someone spends forty-five minutes on status and then rushes their one critical request. The jargon wall — if your VP has to Google an acronym, you've lost them. And "but first, methodology" — this is the one that will trip YOU up specifically, because you were trained to show your work. Fight that instinct. Methodology goes in the appendix. Business impact goes on slide one. -->

---

<!-- ⏱ Expected: 15:40 (min 10/100) -->
## Managing Up: The Art of the Ask + When to Escalate

**The Art of the Ask — be specific and quantify the cost of no:**
- Not: "We need more resources"
- Instead: "We need one senior data engineer by Q2 — without them, self-serve slips to Q4, costing 40 analyst-hours/month"
- **Frame as a trade-off:** "We can do both with one hire, or I deprioritize the churn model. Which do you prefer?"
- **One ask per meeting.** Get one yes. Come back next month for the next one.

**When to escalate** (not ask — escalate):
- When the decision is **irreversible**, **affects other teams**, requires **resources you don't have**, or has **legal/compliance implications**
- Always escalate with a **recommendation**, not just a problem

**"Disagree and commit"** — argue in the room, then execute fully. Quiet sabotage is career-ending.

<!-- Talk track: I watched a brilliant analytics lead walk into a budget meeting and say "we need more resources." The CFO said "doesn't everyone?" and moved on. Three months later, the same person came back with a specific ask, a cost, and a consequence. She got the hire approved in that meeting. The difference was specificity. Frame your ask as a trade-off — give the exec a choice between two concrete options. And one ask per meeting. If you bring five, you get zero. Now — there's a difference between asking for resources and escalating problems. You ask when you need something. You escalate when there's a decision you can't make alone — irreversible, cross-functional, legal. Always escalate with a recommendation. "I don't know what to do" is not an escalation — it's an abdication. And once the decision is made, disagree and commit. Argue hard in the room. Then execute fully. -->

---

<!-- ⏱ Expected: 15:46 (min 16/100) | Communicating Failure (10 min) -->
## Incident Postmortems for Analytics: When Things Go Wrong

When things go wrong — and they will:
- The **dashboard was wrong** and a VP made a bad decision based on it
- The **A/B test had a bug** and you shipped a losing variant
- The **model made a bad prediction** and it cost real money

What matters is not the failure. It's **how you respond**.

<!-- Talk track: Let's talk about what happens when analytics fails. And it will fail. Your dashboard will show the wrong number. Your A/B test will have a bug. Your model will make a prediction that costs the company money. What matters is how you respond. This is where the IC-to-manager shift hits hardest — as an IC, you'd fix it quietly. As a manager, you have to explain it upward while your team fixes it. -->

---

<!-- ⏱ Expected: 15:46 (min 16/100) -->
## Blameless Postmortems

**Blameless culture:** Focus on **systems**, not people.

"Sarah forgot to update the dashboard" is not a root cause. "We have no process for propagating metric definition changes" is a root cause.

**The 5 Whys:**
1. Why was the dashboard wrong? → The metric definition changed
2. Why wasn't it updated? → No process for propagating definition changes
3. Why no process? → We've never formalized metric ownership
4. Why not? → We grew too fast and skipped governance
5. Why? → No one owned data quality as a function

**Action items must have:** An owner, a deadline, and a verification method. A postmortem without action items is just group therapy.

<!-- Talk track: The best teams run blameless postmortems. Blameless doesn't mean no accountability — it means you focus on the system that allowed the failure, not the person who happened to trigger it. Use the 5 Whys to get to a systemic root cause. And every postmortem must produce action items with an owner — a specific human being, not a team — a deadline, and a verification method. Without those three things, your action items are wishes. -->

---

<!-- ⏱ Expected: 15:46 (min 16/100) -->
## Communicating Failure Upward

How to tell your VP that the dashboard was wrong, the model failed, or the project is behind.

**The framework:**
1. **Lead with impact** — "A revenue dashboard had incorrect data for 3 days; two decisions were made using it"
2. **Explain what happened** — brief, factual, no finger-pointing
3. **Describe what you're doing about it** — immediate remediation
4. **Share the systemic fix** — what changes so this never happens again

<!-- Talk track: This is the conversation nobody wants to have. Here's the framework: lead with impact, not with methodology. Don't start with "so there was a join condition in the ETL that..." Start with "the revenue dashboard showed incorrect data for three days, and two pricing decisions were made using it." That's the difference between an IC explanation and a manager explanation. The IC wants to explain the technical cause. The manager leads with the business impact. Then what happened — brief, factual. Then what you're doing about it right now. Then the systemic fix — what changes so this can't happen again. -->

---

<!-- ⏱ Expected: 15:46 (min 16/100) -->
## Communicating Failure Upward

**The worst thing you can do:** Hide it. It always comes out, and now you have two problems — the incident and the cover-up.

**The second worst thing:** Bury it in a long email. Your VP reads the first two lines.

**Subject line format:** "[Impact level] — [What happened] — [Status]"
Example: "P1 — Revenue dashboard showed incorrect data for 3 days — Resolved, postmortem scheduled"

<!-- Talk track: The absolute worst thing you can do is hide it. It always comes out. And now you have two problems: the incident and the fact that you tried to cover it up. The second worst thing is burying it in a long, defensive email. Your VP reads the first two lines. Use this subject line format — impact level, what happened, status. All in the subject line so they know what they're dealing with before they even open the email. Lead with impact. Be direct. Your VP will respect you more for it, not less. -->

---

<!-- ⏱ Expected: 15:56 (min 26/100) | Discussion: delivering worst news (15 min) -->
<!-- _class: divider -->

## Discussion: Delivering Your Worst News

## 15 Minutes

---

<!-- ⏱ Expected: 15:56 (min 26/100) -->
## Discussion: Delivering Your Worst News

Think about the worst thing happening in your case context right now. You have a meeting with your VP in one hour.

- What do you say **first**?
- How do you frame the **impact**?
- What's your **remediation plan**?
- What **systemic fix** do you propose?

Use the framework: **Lead with impact → What happened → What you're doing → Systemic fix.**

*2 minutes: think silently. 3 minutes: share with a partner. Then we'll open it to the room.*

<!-- Talk track: Let's put this into practice. Think about the worst thing happening in your case context right now. Maybe a key dashboard is unreliable. Maybe a project is behind schedule. Maybe a hire fell through. Whatever it is — you have a meeting with your VP in one hour. What do you say first? Remember the IC-to-manager shift: your instinct is to explain the technical cause. Fight it. Lead with impact. Take two minutes to think silently. Then turn to the person next to you and practice saying it out loud — that's three minutes. Then I'll open it to the room. -->

---

<!-- ⏱ Expected: 16:11 (min 41/100) | BLUF Rehearsal — expanded (15 min) -->
<!-- _class: divider -->

## Practice: Your QBR Opening

## 15 Minutes — Two Rounds

---

<!-- ⏱ Expected: 16:11 (min 41/100) -->
## Practice: Your QBR Opening

**Round 1 — Write and deliver (8 min):**

1. **Write** your QBR opening in 4 sentences (3 min):
   - Are we on track?
   - What's the headline result?
   - What's the top risk?
   - What do you need from leadership?

2. **Deliver** it to your partner in 60 seconds. Partner gives **one SBI feedback point.**

**Round 2 — Revise and deliver again (5 min):**

3. **Revise** based on the feedback (2 min)
4. **Deliver again.** Notice the difference.

<!-- Talk track: This is the capstone practice moment. You're going to write the opening of your async QBR and deliver it twice. Round 1: write four sentences — the three executive questions plus your ask. Three minutes to write. Then deliver to your partner in 60 seconds. Partner gives one piece of SBI feedback — what landed, what didn't. Round 2: take that feedback, revise, and deliver again. The second delivery is always dramatically better than the first. That improvement is the learning. Go. -->

---

<!-- ⏱ Expected: 16:26 (min 56/100) | AI and the Changing Manager Role (3 min) -->
## Managing in the Age of AI

Your team in 2026 is a **hybrid human/AI team** — whether you've formalized it or not.

What changes for you as a manager:
- **Velocity shifts** — AI-augmented ICs produce more. Your roadmap and planning assumptions change.
- **Quality review shifts** — You're reviewing AI-assisted output. Different failure modes (remember Liam's unverified stats from the SBI exercise?).
- **Skill mix shifts** — "Can evaluate AI output critically" is now a senior-level skill. Your hiring rubric needs to reflect this.
- **Team dynamics shifts** — High AI users may produce volume but create reviewability problems (remember Kevin's calibration profile?).

Every artifact you've built — Manager OS, hiring rubric, roadmap, infrastructure plan — needs to account for AI. It's not a future problem.

<!-- Talk track: One more thing before the QBR briefing. Think back to this morning. If you drew Scenario 9 — Liam's AI-generated report with fabricated stats — you practiced giving feedback for an AI-specific failure mode. If you calibrated Kevin, you debated whether AI-augmented volume with lower reviewability counts as high performance. In Block E, you wrote about how AI changes your infrastructure or governance. These aren't hypothetical scenarios — they're happening right now in analytics teams. When you record your QBR, your roadmap should reflect the reality that your team includes AI. -->

---

<!-- ⏱ Expected: 16:29 (min 59/100) | Async QBR briefing (8 min) -->
## Async QBR: Your Capstone Deliverable

**What you submit** (as part of your final portfolio):
1. **QBR Outline** — written document using `templates/qbr-outline.md`
2. **QBR Video** — 5-minute recording, as if presenting to your exec team on Zoom

**The scenario:** You are the analytics team lead. You have a quarterly business review with your CEO, CTO, CFO, and VP Product. Present your team's status, wins, risks, and asks.

Apply everything from today: **Pyramid Principle, Art of the Ask, the Three Executive Questions.**

<!-- Talk track: Now let me brief you on your capstone deliverable. You'll submit two things: a written QBR outline and a five-minute video. In the video, you're presenting to your executive team on Zoom. You already practiced the opening — the four sentences you just delivered to your partner. In Block E, you practiced writing a VP proposal in BLUF format. The async QBR is both of those at higher stakes, for 25% of your grade. Use everything you learned today. Lead with BLUF. Answer the three questions. Make your ask specific. Anticipate pushback. -->

---

<!-- ⏱ Expected: 16:29 (min 59/100) -->
## Async QBR: How You'll Be Evaluated

Five dimensions (part of Roadmap + Executive Narrative, 25%):

1. **Clarity of narrative** — BLUF structure, no jargon, logical flow
2. **Business alignment** — roadmap tied to company goals, not just tech
3. **Realism** — achievable timeline with stated resources
4. **Risk awareness** — risks acknowledged with concrete mitigations
5. **Anticipates pushback** — preemptively address the hardest question an executive would ask

Don't wait for them to ask it. In your video, address the hardest question **before they would**.

<!-- Talk track: You'll be evaluated on five dimensions. The fifth one — anticipates pushback — is where you show you can think from the executive's perspective, not just your own. Imagine your CFO watching your video. What would they interrupt to ask? "Can we do this with fewer people?" "What's the ROI?" Address that question in your video before they would ask it. That's the difference between a presentation and a conversation — even when it's a recording. -->

---

<!-- ⏱ Expected: 16:37 (min 67/100) | Portfolio checklist + logistics (3 min) -->
<!-- _class: compact -->
## Portfolio Checklist

**Due: One week from today (23:59 Vienna time)**

| Component | Weight |
|---|---|
| **1. Manager OS Document** (2–4 pp) | 15% |
| **2. Hiring Packet** (JD + work sample + rubric + loop) | 20% |
| **3. Roadmap + Exec Narrative + QBR Outline + QBR Video** | 25% |
| **4. Personal Growth Plan** | 7.5% |
| **5. Performance Summary** | 7.5% |
| Participation & Preparedness | 15% |
| Day 1 Checkpoint | 10% |

**Format:** Single PDF or repo. **The portfolio is one integrated system** — same team, same case context, coherent story across all artifacts.

_Optional: Data Infrastructure Blueprint, RFP Scoring Matrix (see `resources/`)._

<!-- Talk track: Five portfolio artifacts plus participation and the Day 1 checkpoint. The biggest component is Roadmap plus Executive Narrative plus QBR at 25% — that includes everything: your RICE-scored roadmap, your two-page narrative, your QBR outline, and your five-minute video. The most common mistake: treating the portfolio as five separate documents. It's one system. Your roadmap should reference the same team from your charter. Your QBR should synthesize everything into a coherent story. If an executive could read your portfolio and understand your team, your plan, and your priorities — you've done it right. -->

---

<!-- ⏱ Expected: 16:40 (min 70/100) | Reflection (2 min) -->
## Your Next 90 Days — Write It Down

**2 minutes.** Write down **3 specific actions** you will take in the next 90 days.

Not aspirations — **actions with dates.**

| Instead of... | Write... |
|---|---|
| "Be a better manager" | "Start weekly 1:1s with each report within 2 weeks" |
| "Improve data quality" | "Implement metric ownership doc for top 10 metrics by April 15" |
| "Communicate better" | "Write a BLUF summary for every exec update starting next week" |

These are yours. You don't have to share them.

<!-- Talk track: Before I close — take out a piece of paper or open a blank doc. Write down three specific actions you will take in the next 90 days. Not "be a better manager." I want dates and specifics. "Start weekly 1:1s within two weeks." "Write a BLUF summary for every exec update starting next week." "Audit my team's data infrastructure in my first month." Two minutes. These are for you — I won't collect them. But research shows that writing down intentions dramatically increases follow-through. Go. -->

---

<!-- ⏱ Expected: 16:42 (min 72/100) | Course close (8 min) -->
<!-- _class: divider -->

## Course Complete

## Go Build Great Teams

<!-- Talk track: And that brings us to the close. Let me tell you what you've accomplished. -->

---

<!-- ⏱ Expected: 16:42 (min 72/100) -->
## Close: What You've Built

You've built a **Manager Operating System**.

Over two days, you've practiced how to:
- **Define** your team's purpose, scope, and operating principles
- **Hire** with structure, fairness, and signal
- **Roadmap** with business alignment and executive clarity
- **Grow** your people through PGPs and honest performance conversations
- **Assess** your infrastructure and cross-functional dependencies
- **Communicate** to executives with impact and clarity

The **portfolio is the proof**. Refine your drafts. Submit with pride.

<!-- Talk track: In two days, you've built more management artifacts than most new managers create in their first six months. You have a team charter, a hiring packet, a roadmap, growth plans, an infrastructure assessment, and you've learned to communicate all of it to executives. That's not theory — that's practice. -->

---

<!-- ⏱ Expected: 16:42 (min 72/100) -->
## Close: Go Build Great Teams

**Office hours are available** — reach out if you need help with the portfolio or the async QBR.

The best analytics managers I know share three traits:
- They **care deeply** about their people — you practiced this in Block D when you gave real feedback
- They **communicate clearly** with leadership — you practiced this today when you delivered your worst news and your QBR opening
- They **never stop learning** the craft of management — you showed this by spending two days building something real

Managing people is hard, and you've been willing to practice it in public. That takes courage.

You now have the frameworks. The rest is practice.

**Now go build great teams.**

<!-- Talk track: The best analytics managers I know care deeply about their people — you practiced that this morning when you gave SBI feedback to a partner and wrote a development area for someone you calibrated. They communicate clearly with leadership — you practiced that this afternoon when you delivered your worst news to a partner, wrote a VP proposal in Block E, and just delivered your QBR opening twice. And they never stop learning — you showed that by spending two days building real management artifacts from scratch. I want to acknowledge something: managing people is hard, and you've been willing to practice it in a room full of your peers. That takes real courage. You now have the frameworks. You have the artifacts. You have the practice. Now go build great teams. -->
