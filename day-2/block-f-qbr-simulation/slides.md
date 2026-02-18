---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 2 – Block F"
---

# Leading Up & Across; QBR Simulation

**Day 2 — Block F | 15:30–17:10**

**Learning Outcome**
By the end of this block you will be able to:
- Align leadership and collaborate cross-functionally using clear interfaces

This is the capstone. You will present your roadmap and executive narrative in a QBR simulation to a mock executive panel.

<!-- Talk track: Welcome to the final block. Everything you've built over these two days — the Manager OS, the hiring packet, the roadmap, the growth plans, the infrastructure blueprint — it all converges here. This block is about leading up and across. Leading up means communicating with executives who have limited time and broad scope. Leading across means working with peers in other functions who have different priorities. The QBR simulation is your chance to practice both. You'll present your roadmap to a mock executive panel, and your peers will play the executives asking hard questions. Let's start with the framework for executive communication. -->

---

## Executive Communication

> "If you can't explain it simply, you don't understand it well enough."

Executives operate in a different context than you:
- **Limited time** — They have 30 minutes between meetings, not 30 minutes for your meeting
- **Broad scope** — Your team is one of twenty things they're tracking
- **High stakes** — They're making resource allocation decisions based on what you tell them

**The Pyramid Principle:** Conclusion first, then supporting arguments, then data.

**BLUF (Bottom Line Up Front):** Always lead with the answer. "We're on track, but I need to flag two risks" is better than a 10-minute buildup.

<!-- Talk track: Let me be blunt about something. The way you communicate with your team is not the way you communicate with executives. Your team wants context, nuance, caveats. Executives want the answer first. The Pyramid Principle, from Barbara Minto at McKinsey, says: start with the conclusion, then give supporting arguments, then provide data if asked. BLUF — Bottom Line Up Front — is the military version of the same idea. Here's a test: if an executive read only your first sentence, would they know your main message? If not, restructure. This is not about dumbing things down. It's about respecting someone's time and cognitive bandwidth. The best analytics leaders I've worked with can switch between deep technical discussions with their team and crisp executive summaries in the same hour. -->

---

## What Executives Actually Want to Know

Every executive presentation should answer **three questions:**

1. **Are we on track?**
   Status against goals, metrics, timeline

2. **What are the risks?**
   What could go wrong, what's already going wrong, what are you doing about it

3. **What do you need from me?**
   Decisions, resources, air cover, nothing (and "nothing" is a valid answer)

**Everything else is context.** If your presentation doesn't answer these three questions, it's not ready.

**Pro tip:** Put these three answers on your first slide or in your first paragraph. Everything after that is supporting evidence.

<!-- Talk track: I want to simplify executive communication down to its essence. There are exactly three things executives want to know. First: are we on track? Give me the status. Green, yellow, red — don't make me guess. Second: what are the risks? Don't hide bad news. Executives hate surprises more than they hate bad news. If your model is underperforming, say so and say what you're doing about it. Third: what do you need from me? This is the one people forget. Executives want to help. They want to unblock you. But you have to ask. If you don't need anything, say "no asks this quarter" — that's actually reassuring. Everything else in your presentation is context and evidence supporting these three answers. -->

---

## Decisions & Escalation

**When to escalate:**
- When the decision is **irreversible** (Type 1)
- When it **affects other teams** you don't control
- When you need **resources you don't have**
- When it has **legal, compliance, or reputational** implications

**How to escalate:**
1. Present the **decision** clearly — what needs to be decided
2. Give your **recommendation** — what you think we should do
3. Lay out the **trade-offs** — what we gain and lose with each option

**"Disagree and commit"** — Once the decision is made, execute fully. Undermining a decision you lost is a career-ending move.

**The escalation anti-pattern:** Escalating everything (decision avoidance) is as bad as escalating nothing (cowboy behavior).

<!-- Talk track: Knowing when and how to escalate is one of the hardest skills for new managers. Here's the framework. Escalate when the decision is irreversible — remember Type 1 from Day 1. Escalate when it affects teams you don't control — if your decision will change the engineering team's roadmap, that's not your call alone. Escalate when you need resources — budget, headcount, executive sponsorship. And always escalate legal or compliance issues. How you escalate matters as much as when. Never escalate a problem without a recommendation. "I don't know what to do" is not an escalation — it's an abdication. Say "Here's the situation, here are the options, here's what I recommend, and here's the trade-off." Disagree and commit is an Amazon principle but it's universal. You can argue hard for your position in the room. But once the decision is made, you execute it fully. Passive-aggressive non-compliance — doing the thing you were told to do but doing it badly — is worse than open disagreement. -->

---

## Incident Postmortems for Analytics

When things go wrong — and they will:
- The **dashboard was wrong** and a VP made a bad decision based on it
- The **A/B test had a bug** and you shipped a losing variant
- The **model made a bad prediction** and it cost real money

**Blameless culture:** Focus on **systems**, not people.

**The 5 Whys:**
1. Why was the dashboard wrong? → The metric definition changed
2. Why wasn't it updated? → No process for propagating definition changes
3. Why no process? → We've never formalized metric ownership
4. Why not? → We grew too fast and skipped governance
5. Why? → No one owned data quality as a function

**Action items must have:** An owner, a deadline, and a verification method.

<!-- Talk track: Let's talk about what happens when analytics fails. And it will fail. Your dashboard will show the wrong number. Your A/B test will have a bug. Your model will make a prediction that costs the company money. What matters is how you respond. The best teams run blameless postmortems. Blameless doesn't mean no accountability — it means you focus on the system that allowed the failure, not the person who happened to trigger it. The 5 Whys is a simple technique from Toyota. You keep asking "why" until you get to a root cause that's systemic, not individual. Look at this example. The root cause isn't "Sarah forgot to update the dashboard." The root cause is "we have no process for metric ownership." That's a system fix. Every postmortem should produce action items, and every action item needs an owner, a deadline, and a way to verify it was done. A postmortem without action items is just group therapy. -->

---

## Adapting Your Manager OS by Org Size

| Dimension | Small (Seed/Series A) | Medium (Series B/C) | Large (Enterprise) |
|---|---|---|---|
| **Communication** | Informal, verbal, fast | Written becomes critical | Formal docs, alignment decks |
| **Decision-making** | You decide, then do | You delegate and review | You lead through others |
| **Cross-functional** | Walk to their desk | Scheduled syncs, shared docs | RACI, SLAs, steering committees |
| **Your main job** | Ship | Build process | Ensure alignment |
| **Biggest risk** | Burnout (you do everything) | Bottleneck (everything goes through you) | Drift (teams misalign silently) |

**The transition trap:** What made you successful at one size will actively hurt you at the next size. The scrappy startup founder who won't delegate kills the Series B company. The process-builder who won't let go of process kills innovation at the startup.

<!-- Talk track: Your Manager OS is not static. It has to evolve as the organization grows. At a small startup, you do everything. You're the analyst, the data engineer, the dashboard builder, and the manager. Communication is informal — you just yell across the room. Decisions are fast. That's fine for 5 people. At medium scale, say 20 to 100 people, you have to start building process. Written communication becomes critical because you can't be in every room. You start delegating real decisions. Cross-functional work gets formalized. At large scale, your main job is alignment. You lead through other managers. You spend most of your time in meetings ensuring that teams are moving in the same direction. The dangerous moment is the transition. The skills that made you successful at one stage can actively hurt you at the next. The founder who won't stop coding. The director who won't stop approving every PR. Adaptation is the meta-skill. -->

---

## QBR Simulation Brief

**Format:**
- **5-minute presentation** + **5-minute Q&A** from the "executive panel"
- Groups of 3–4 students

**How it works:**
1. One student presents their roadmap and executive narrative as if in a real QBR
2. The other students play executive roles (using the role cards on the next slide)
3. Rotate until everyone has presented

**While you present:** Be concise, be confident, lead with BLUF. Use your QBR outline template.

**While you're on the panel:** Stay in character. Ask real questions. Be respectful but challenging. Don't softball it — that doesn't help anyone learn.

<!-- Talk track: All right, let's set up the simulation. This is the capstone of the entire course. Here's how it works. You'll form groups of 3 to 4. One person presents their roadmap and executive narrative — the same one you've been building since Day 1. You have exactly 5 minutes to present. Then the other members of your group become the executive panel and ask questions for 5 minutes. Then you rotate. Everyone presents. Everyone plays an executive. I want this to feel as real as possible. When you're presenting, pretend this is your actual quarterly business review. When you're on the panel, pretend you're actually the CEO or CTO or CFO. Ask the hard questions. Don't be mean, but don't be easy either. The whole point is to practice handling pressure with grace. -->

---

## QBR Evaluation Criteria

| Criterion | What "Good" Looks Like |
|---|---|
| **Clarity of narrative** | BLUF structure, no jargon without explanation, logical flow |
| **Business alignment** | Roadmap connects to company goals, not just technical goals |
| **Realism** | Achievable with stated resources, timeline is credible |
| **Risk awareness** | Risks acknowledged, mitigations concrete, no "everything is fine" |
| **Q&A handling** | Composed under pressure, direct answers, honest about unknowns |

**What "great" looks like:** The presenter makes the exec panel feel confident that the analytics team is well-managed, strategically aligned, and worth investing in.

**What "needs work" looks like:** The presenter drowns in technical details, can't articulate business impact, or gets defensive when challenged.

<!-- Talk track: Let me be transparent about how I'll evaluate these presentations. There are five criteria. Clarity — is it BLUF? Can I follow your logic? Business alignment — does your roadmap connect to what the company actually needs, or is it a wish list of cool technical projects? Realism — if you say you're going to do 15 things with 3 people in one quarter, I'm going to push back. Risk awareness — every plan has risks. If you tell me there are no risks, I don't trust your judgment. And Q&A handling — this is where it gets real. Can you stay composed when someone challenges your assumptions? Can you say "I don't know, but here's how I'd find out"? That takes practice, which is why we're practicing now. -->

---

## Exec Panel Role Cards

Play one of these roles during Q&A. Stay in character.

**CEO:**
> "Show me the business impact. Why should I invest in this team over other priorities? What's the 3-year vision?"

**CTO:**
> "How does this integrate with our engineering roadmap? What are the technical risks? Are we building tech debt?"

**CFO:**
> "What's the ROI? Can we do this with fewer people? What happens if I cut your budget by 20%?"

**VP Product:**
> "How will this help my team ship faster? When will my PMs stop waiting 2 weeks for a dashboard? What's your SLA?"

**Tip for panelists:** Ask one hard question, then one follow-up. Don't pile on — give the presenter space to respond.

<!-- Talk track: Here are your role cards. When you're playing an executive, pick one of these four roles and commit to it. The CEO cares about strategic impact and resource allocation. The CTO cares about technical integration and risk. The CFO cares about money — ROI, efficiency, headcount. The VP Product cares about speed and service to their teams. Each role has a signature question. Ask it. Then ask one follow-up based on what you hear. The goal is not to stump the presenter — it's to simulate what a real QBR feels like. In real life, these executives are usually supportive. They want you to succeed. But they also need to make decisions with limited information, so they'll push you to be crisp. -->

---

## QBR Simulation

### In Progress

**Time: 40–50 minutes**

Presenting order: rotate within your group. Everyone presents once.

**Remember:**
- Presenters: 5 minutes max, then 5 minutes Q&A
- Panelists: stay in your exec role, ask real questions
- Timer is running — respect the clock

<!-- Talk track: All right, form your groups. Pick your first presenter. I'm starting the timer. Five minutes to present, five minutes for Q&A. I'll call time. Let's go. -->

---

## Simulation Debrief

**Reflect and discuss:**

- What **surprised you** about presenting to executives?
- What question were you **least prepared** for?
- What would you **do differently** next time?
- What did you learn from **playing an executive** that changes how you'll present?

**Key insight:** The gap between "I know my material" and "I can communicate it under pressure to a skeptical audience" is enormous. That gap closes only with practice.

<!-- Talk track: Let's debrief. I want to hear from the room. What surprised you? Raise your hand. What question caught you off guard? Here's what I usually see: people are surprised by how hard it is to be concise under pressure. You know your material deeply, but when someone asks a pointed question, your instinct is to give context, explain the nuance, add caveats. Executives don't want that. They want the answer first. Also, I want to hear from people who played executives. What did you notice from the other side of the table? Usually people say: "I realized how impatient I was. I just wanted them to get to the point." That's the insight. You now know what it feels like to be on both sides. Carry that with you. -->

---

## Portfolio Checklist

**Due: One week from today (23:59 Vienna time)**

| Artifact | Source Block |
|---|---|
| Team Charter | Block A |
| Stakeholder Map | Block A |
| Manager OS (2–4 pages) | Block A |
| Hiring Packet (JD, work sample, rubric, interview loop) | Block B |
| Roadmap + RICE Scoring | Block C |
| Executive Narrative (2 pages) | Block C |
| Risk Register | Block C |
| Personal Growth Plan (PGP) | Block D |
| Performance Summary | Block D |
| Data Infrastructure Blueprint | Block E |
| RFP Scoring Matrix | Block E |
| QBR Outline | Block F |

**Format:** Single PDF or a structured repository. Use the portfolio checklist template.

<!-- Talk track: Let's talk about what's due. The portfolio is everything you've built across both days, refined into final form. Here's the complete list. Team Charter, Stakeholder Map, and Manager OS from Block A. Hiring Packet from Block B — that's the JD, work sample, rubric, and interview loop. Roadmap with RICE scoring, executive narrative, and risk register from Block C. PGP and performance summary from Block D. Data infrastructure blueprint and RFP scoring matrix from Block E. And the QBR outline from today. Submit it as a single PDF or a structured repo. The portfolio checklist template will help you track your progress. You have one week. The drafts you built in class are your starting point — refine them, don't start over. -->

---

## Your Next 90 Days

Real talk: **what are you going to do with this?**

Write down **3 specific actions** for the next 90 days. Not aspirations — actions.

| Bad | Good |
|---|---|
| "Be a better manager" | "Start weekly 1:1s with each report by March 30" |
| "Improve data quality" | "Implement metric ownership doc for top 10 metrics by April 15" |
| "Communicate better" | "Write a BLUF summary for every exec update starting next week" |

**Specific. Measurable. Time-bound.**

Take 2 minutes now. Write them down. These are yours — you don't have to share them.

<!-- Talk track: I want to do something different for a moment. Take out a piece of paper or open a blank doc. Write down three specific actions you will take in the next 90 days based on what you've learned. Not "be a better manager" — that's a wish, not an action. I want things like "Start weekly 1:1s with my two direct reports by the end of March." "Write a team charter for my analytics team and share it with my VP by April." "Create a metric ownership document for our top 10 dashboards." Specific, measurable, time-bound. Take 2 minutes. Write them down. These are for you — I'm not going to collect them. But research shows that writing down intentions dramatically increases follow-through. Go. -->

---

## Peer Feedback Reminder

**Due: 48 hours from now**

- Written feedback for **2 peers**
- Use the **peer feedback form** (on LMS)
- **5% of your grade** — take it seriously

**How to give good feedback:**
- Be **specific** — "Your risk register was thorough" beats "Good job"
- Be **kind** — You're helping a colleague improve, not scoring points
- Be **useful** — What's one thing they could do to make their artifact stronger?

The best feedback is something the recipient can act on before the portfolio deadline.

<!-- Talk track: Before I close, a reminder about peer feedback. It's due 48 hours from now. You'll provide written feedback for two of your peers using the peer feedback form on the LMS. This is worth 5% of your grade, so take it seriously. Here's what good peer feedback looks like. It's specific — not "nice work" but "your risk register identified technical debt as a risk but didn't include a mitigation strategy, which would make it stronger." It's kind — remember, you're helping a colleague improve. And it's useful — the best feedback gives someone something concrete they can act on before the portfolio deadline. Think of it as a gift: you're giving someone an outside perspective they can't get on their own. -->

---

## Close

You've built a **Manager Operating System**.

Over two days, you've practiced how to:
- **Define** your team's purpose, scope, and operating principles
- **Hire** with structure, fairness, and signal
- **Roadmap** with business alignment and executive clarity
- **Grow** your people through PGPs and honest performance conversations
- **Build** infrastructure pragmatically and evaluate vendors rigorously
- **Present** to executives under pressure and handle hard questions

The **portfolio is the proof**. Refine your drafts. Submit with pride.

**Office hours are available** — reach out if you need help.

Thank you. Now go build great teams.

<!-- Talk track: Let me close by telling you what you've accomplished. In two days, you've built more management artifacts than most new managers create in their first six months. You have a team charter, a stakeholder map, a hiring packet, a roadmap, a growth plan, an infrastructure blueprint, and you just presented to a mock executive panel. That's not theory — that's practice. The portfolio is your chance to refine all of this into something you're proud of. Take the drafts you built in class, improve them, and submit them. If you're stuck on anything, office hours are available. I genuinely hope this course changes how you think about management. It's not about authority — it's about building systems that let talented people do their best work. Thank you for your energy, your engagement, and your willingness to practice something hard. Now go build great teams. -->
