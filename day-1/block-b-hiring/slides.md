---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 1 – Block B"
---
<!-- Talk track: Block B — Hiring and Team Formation. This is the post-lunch block, so bring energy and start with the provocative cost-of-bad-hire framing. -->

<!-- _class: title -->

# Hiring & Team Formation

## Day 1 — Block B | 13:30–15:10

**LO: Produce a structured hiring packet that improves signal and fairness**

<!-- Talk track: Welcome back from lunch. This block is about the single highest-leverage activity you will do as a manager — hiring. A great hire compounds for years; a bad hire compounds damage for months. By the end of this block, you will have a complete hiring packet: job description, work sample exercise, scoring rubric, and interview loop design. Let's get into it. -->

---

# The Cost of a Bad Hire

- Average cost of a mis-hire: **1.5–2x annual salary** (SHRM, Bradford Smart)
- In analytics specifically, a wrong hire means:
  - **6 months of bad dashboards** that erode stakeholder trust
  - Broken credibility with the business — "analytics never delivers"
  - Team morale damage — good people leave when surrounded by poor performers
- The **"brilliant jerk"** problem: technical skill without collaboration destroys team culture faster than incompetence

> "The best thing a manager does is hire well. The second best thing is fire fast when they don't."
> — Ben Horowitz

<!-- Talk track: Let's start with stakes. Why does hiring matter so much in analytics? Because analytics is a trust business. If your first hire ships bad dashboards for six months, the VP of Product stops asking your team for help. They go hire a contractor or build their own spreadsheet. You lose your seat at the table. And the brilliant jerk — the person who is technically excellent but impossible to work with — they will drive away every collaborative person on your team. The cost is not just salary. It is organizational trust. -->

---

# Role Design Before Recruiting

**Don't start with a job description. Start with outcomes.**

### The Role Scorecard Approach

1. **What does this person need to accomplish in their first 90 days?**
2. Define 3–5 concrete outcomes, not a laundry list of skills
3. Work backward from outcomes to required capabilities

### Example — First Analytics Hire at a Seed-Stage Startup

| 90-Day Outcome | Capability Needed |
|:---|:---|
| Instrumented top-3 user flows with event tracking | SQL + analytics engineering |
| Delivered weekly KPI dashboard to founders | Visualization + communication |
| Scoped first A/B test for onboarding | Experimental design basics |

<!-- Talk track: Most hiring processes start wrong. Someone says "we need a data scientist" and the hiring manager opens a Google Doc and starts listing skills — Python, SQL, Tableau, machine learning, PhD preferred. That is a shopping list, not a role design. Instead, start with the question: what does this person need to accomplish in their first 90 days? Three to five concrete outcomes. Then work backward to what capabilities are actually required. You will be shocked at how different the resulting job description looks. -->

---

# What Level Do You Actually Need?

| Level | What They Do | Autonomy | Scope |
|:---|:---|:---|:---|
| **Junior** | Executes well-defined analyses | Needs clear specs | Single tasks |
| **Mid** | Scopes own work, communicates findings | Self-directed on known problems | Projects |
| **Senior** | Influences strategy, mentors others | Navigates ambiguity | Team-wide |
| **Staff/Principal** | Org-wide impact, shapes practice | Sets direction | Cross-team |

### Common Mistakes

- Hiring **senior** when you need **mid** — you pay for strategy but need execution
- Hiring **mid** when you need **senior** — they cannot navigate the ambiguity you are drowning in
- Writing "senior" in the title but paying mid-level comp

<!-- Talk track: Before you write the job description, get honest about what level you actually need. This is where a lot of managers get it wrong. A seed-stage startup does not need a Staff Data Scientist. They need someone who can write SQL, build dashboards, and communicate clearly — that is a strong mid-level hire. Conversely, if you are at a Series B and your entire analytics function is one person embedded with a product team, you probably need a senior who can navigate ambiguity and influence without authority. Leveling mistakes are expensive because the wrong-level hire will either be bored or overwhelmed, and both lead to attrition. -->

---

# The Research on Structured Interviews

### Predictive Validity of Selection Methods

| Method | Correlation with Job Performance |
|:---|:---|
| Unstructured interviews | **~0.20** |
| Structured interviews | **~0.51** |
| Work samples | **~0.54** |
| Cognitive ability tests | **~0.51** |
| Reference checks | **~0.26** |
| Years of experience | **~0.18** |

<small>Source: Schmidt & Hunter (1998), updated meta-analyses</small>

**Key insight: Your gut feeling is mostly noise. Structure = fairness + signal.**

<!-- Talk track: This is the most important slide in the deck. These numbers come from decades of industrial-organizational psychology research, primarily Schmidt and Hunter's landmark 1998 meta-analysis and subsequent updates. An unstructured interview — the "let's just chat and see if they are smart" approach — predicts job performance at a 0.20 correlation. That is barely better than flipping a coin. A structured interview, where every candidate gets the same questions evaluated against a rubric, jumps to 0.51. Work samples — give them a realistic task and evaluate the output — hit 0.54. Notice that years of experience is at the bottom. Your gut feeling, your "I just know a good hire when I see one" — that is noise dressed up as intuition. Structure is not bureaucracy. Structure is how you find signal in a process riddled with bias. -->

---

# Designing Work Samples

### What Makes a Good Work Sample?

- **Reflects actual job tasks** — not LeetCode puzzles for analytics roles
- **Has clear evaluation criteria** — defined before candidates see the exercise
- **Respects candidate time** — 2–4 hours maximum, clearly communicated
- **Tests judgment, not just technique** — "What would you do next?" matters more than "Can you write a LEFT JOIN?"

### Analytics Work Sample Example

> *"Here is a messy dataset of user activity logs and a business question from the VP of Product: 'Should we invest in improving our onboarding flow?' Walk us through your approach, your analysis, and your recommendation."*

### What You Are Really Evaluating

How they **frame** the problem > How they **execute** the analysis > How they **communicate** the findings

<!-- Talk track: The work sample is the centerpiece of your hiring process. For analytics roles, this is not a coding test. It is a simulation of the actual job. You give candidates a realistic dataset — messy, with some known issues — and a business question. Then you evaluate three things in order of importance: first, how they frame the problem. Do they ask clarifying questions? Do they identify what is out of scope? Second, how they execute. Is the analysis sound? Do they handle missing data thoughtfully? Third, how they communicate. Can they explain their findings to a non-technical stakeholder? The framing question is the most diagnostic because it reveals whether someone can operate independently or needs everything spelled out for them. -->

---

# Building a Rubric

### Why a Rubric?

- Score on **predefined dimensions**, not overall impression
- Prevents: halo effect, anchoring, recency bias, "culture fit" as a catch-all
- Forces interviewers to articulate *what* they are evaluating

### Dimensions for Analytics Roles

| Dimension | What You Are Looking For |
|:---|:---|
| **Technical Execution** | Sound methodology, clean analysis, handles edge cases |
| **Communication Clarity** | Explains findings to non-technical audience |
| **Business Context Awareness** | Connects analysis to decisions and outcomes |
| **Intellectual Curiosity** | Asks good questions, explores beyond the obvious |

### Scale: 1–4 (no fence-sitting)

Use a 4-point scale. A 3-point scale lets everyone hide in the middle. Force a call.

<!-- Talk track: A rubric is what turns a subjective conversation into a structured evaluation. Here is the key: you define the dimensions and the scoring criteria before you see any candidates. Not after. Before. For analytics hires, I recommend four dimensions: technical execution, communication clarity, business context awareness, and intellectual curiosity. Use a four-point scale, not three, not five. Three-point scales let everyone pick the middle and avoid a real evaluation. Five-point scales create the illusion of precision you do not have. Four forces a meaningful distinction: this person is below the bar, approaching the bar, meeting the bar, or exceeding the bar. -->

---

# Calibrating Scorers

### The Problem

Without calibration, interviewers anchor to different standards:
- Interviewer A thinks "3" means "could do the job"
- Interviewer B thinks "3" means "among the best I have seen"

### The Fix: Norming Session

**Before the interview loop begins:**
1. Score a **practice candidate** together (use a past work sample or a fabricated one)
2. Discuss every disagreement — "Why did you give a 2 on communication?"
3. Align on what each score means for each dimension
4. Document calibration notes for reference

### Biases Norming Prevents

- **Anchoring** to the first interviewer's opinion
- **Halo effect** — one strong dimension inflates all scores
- **Recency bias** — the last candidate always seems freshest

<!-- Talk track: Calibration is the step everyone skips and then wonders why their debrief sessions are arguments instead of decisions. Before your interview loop begins, get all interviewers in a room. Show them a work sample — either from a past candidate, anonymized, or one you fabricated. Have everyone score it independently. Then discuss. You will be amazed at how different the scores are. One person gave a 4 on communication, another gave a 2, and they were looking at the same work. That is what you need to resolve before real candidates show up. Twenty minutes of calibration saves hours of circular debrief arguments. -->

---

# The Interview Loop

### Who Interviews for What

| Interviewer | Focus Area | Why This Person |
|:---|:---|:---|
| **Hiring Manager** | Role fit + team dynamics | Owns the decision |
| **Technical Peer** | Depth of craft | Can evaluate real skill |
| **Cross-Functional Partner** | Collaboration + communication | Will work with this person daily |
| **Skip-Level Manager** | Judgment + growth potential | Longer-term perspective |

### The Critical Rule: Independent Scores Before Discussion

1. Each interviewer submits scores **before** the debrief meeting
2. No peeking at others' scores
3. Debrief starts with a round-robin: each person shares their scores and top observations
4. Hiring manager makes the final call — this is **not** a consensus vote

<!-- Talk track: The interview loop is the structure around who evaluates what. Four interviewers, each with a distinct focus. The hiring manager looks at role fit and team dynamics. A technical peer evaluates depth — can this person actually do the work? A cross-functional partner, say a product manager, tests collaboration and communication. And a skip-level manager assesses judgment and growth potential over a longer horizon. The critical rule: everyone submits their scores independently before the debrief. No hallway conversations. No "what did you think?" before scores are in. Why? Because the first strong opinion in a debrief anchors everyone else. Independent scoring, then discussion. The hiring manager makes the final call. This is not a democracy. Consensus-based hiring produces mediocrity because it selects for "no one objected" rather than "someone was enthusiastic." -->

---

# Candidate Experience

### Your Employer Brand Is Built in Rejection Emails

- **Timeline:** < 1 week between stages. Silence is a decision — the decision to lose good candidates.
- **Communication:** Proactive updates even when there is no update. "We are still reviewing" beats silence.
- **Rejection:** Specific, kind, and fast.

### The Math

- You will interview ~20 candidates for each hire
- 19 of them will tell their network about the experience
- **19 negative stories vs. 1 hire** — the ratio matters

### Non-Negotiables

- Acknowledge every application within 48 hours
- Provide a clear timeline at every stage
- Give feedback with rejections (even brief: "We went with a candidate with deeper SQL experience for this specific role")
- Never ghost a candidate who completed a work sample

<!-- Talk track: Let me give you a number that changes how you think about hiring. For every person you hire, you reject about 19. Those 19 people will tell their friends, their colleagues, their Twitter followers about their experience with your company. If you ghosted them, or made them wait three weeks for a response, or gave them a take-home that took 20 hours — they will tell everyone. Your employer brand is not built in the offer letter. It is built in the rejection email. The non-negotiables: acknowledge every application within 48 hours, provide a clear timeline, give feedback with rejections, and never ghost someone who invested time in a work sample. This is not just kindness. This is strategy. The data science community is small. Your reputation precedes you. -->

---

<!-- _class: divider -->

# Activity: Build Your Hiring Packet

## 35 Minutes | Use the Templates

<!-- Talk track: Time to put this into practice. For the next 35 minutes, you will build a complete hiring packet for your first or next analytics hire within your chosen case context. You have four templates to complete: a job description built around 90-day outcomes, a work sample exercise, a scoring rubric, and an interview loop design. Use the templates provided. Work individually but feel free to ask questions. I will circulate. At the end, you will pair up for a role-play exercise using what you have built. -->

---

# Activity Brief: Build Your Hiring Packet

### Your Case Context

Use the company scenario you chose in Block A (small / medium / large)

### Deliverables (35 min)

1. **Job Description** — Role summary, 90-day outcomes, responsibilities, qualifications
2. **Work Sample Exercise** — Realistic task, dataset description, evaluation criteria
3. **Scoring Rubric** — Dimensions, 1–4 scale with behavioral anchors
4. **Interview Loop Design** — Stages, interviewers, focus areas, debrief protocol

### Tips

- Start with the 90-day outcomes — everything else follows
- Be honest about "required" vs. "preferred" qualifications
- Your work sample should take a candidate 2–4 hours, not 20
- Design the rubric so a stranger could use it and reach similar conclusions

<!-- Talk track: Here is the specific breakdown. Start with the job description template and fill in the 90-day outcomes first. That is your anchor. Then design a work sample that tests whether a candidate can actually accomplish those outcomes. Build your rubric next — make sure every dimension on the rubric maps to something you are testing in the work sample or interviews. Finally, design the interview loop. Who interviews, what they evaluate, and how you debrief. A tip: if you are stuck, start with the question "what would make me confident this person can succeed in their first 90 days?" and work backward from there. You have 35 minutes. Go. -->

---

# Role-Play Setup

### In 15 minutes, you will pair up

**Round 1 (10 min):** Person A plays the candidate. Person B runs a structured interview using their rubric.

**Round 2 (10 min):** Swap roles.

### How It Works

1. You will receive a **Candidate Profile Card** — play this person authentically, including their weaknesses
2. The interviewer uses their rubric and asks questions from their interview loop
3. After each round, the interviewer shares scores and explains their reasoning
4. The "candidate" gives feedback: "Here is what felt fair, here is what felt unclear"

### The Goal

Experience both sides of a structured interview. Find where your rubric works and where it breaks down.

<!-- Talk track: After the 35 minutes of building, we are going to do something uncomfortable and valuable. You are going to pair up and run actual structured interviews. One person plays the candidate using a profile card I will give you. The other person runs the interview using the rubric they just built. Then you swap. This is where the rubber meets the road. You will discover whether your rubric actually helps you evaluate someone or whether it falls apart when a real human being is sitting across from you. Play the candidate authentically — do not make it easy for the interviewer. If your profile says you are weak on communication, be weak on communication. The goal is to stress-test the rubric, not to practice being impressive. -->

---

# Candidate Profile Cards

### You Will Receive One of Four Profiles

| Profile | Archetype | Key Trait |
|:---|:---|:---|
| **Profile A** | The Strong Candidate | Solid all-around; might be slightly overqualified |
| **Profile B** | The Borderline | Good technical skills but communication gaps |
| **Profile C** | The Wrong Level | Impressive resume, but too senior/junior for the role |
| **Profile D** | The Culture Fit Trap | Likable and articulate but shallow technical depth |

Each card includes: background, strengths, weaknesses, a "tell" that the interviewer should catch, and suggested responses to common questions.

**Play the profile, not yourself.**

<!-- Talk track: I am going to hand out candidate profile cards. Each profile is a different archetype you will encounter in real hiring. Profile A is the strong candidate — solid all around, maybe a little overqualified. Profile B is the borderline — good technically but struggles to communicate findings. Profile C is the wrong-level candidate — their resume is impressive but they are either too senior or too junior for what you actually need. Profile D is the culture-fit trap — charming, articulate, says all the right things, but if you probe technically, the depth is not there. Each card has suggested responses and a tell — something the interviewer should catch if their rubric and questions are well-designed. Play the profile, not yourself. -->

---

# Debrief

### Reflection Questions

- **What signals were hardest to evaluate?**
  - Where did your rubric give you clear answers? Where did it fail?

- **Where did your rubric break down?**
  - Missing dimensions? Ambiguous score definitions? Too many dimensions?

- **What would you change?**
  - About your questions, your rubric, your scoring process?

- **What surprised you about being the candidate?**
  - What felt fair? What felt arbitrary?

### Key Takeaway

A rubric is a living document. Your first version will be wrong. The goal is to **iterate** after every interview loop.

<!-- Talk track: Let's debrief. I want to hear from both sides. Interviewers first: what was the hardest signal to evaluate? Where did your rubric give you a clear answer and where did it leave you guessing? Now candidates: what felt fair about the process? What felt arbitrary or unclear? This is the most important insight from the exercise — your first rubric will be wrong. Every rubric is wrong the first time. The goal is not perfection, it is iteration. After every real interview loop, you should update your rubric based on what you learned. Add a dimension you were missing. Sharpen a vague score definition. Remove a dimension that was not actually diagnostic. The rubric is a living document, not a form you fill out once and file away. -->

---

# Hiring Anti-Patterns

### Quick Hits — What Not to Do

- **"Culture fit" as a criterion** — This is how you hire clones of yourself. Replace with "culture add" or specific collaboration behaviors.

- **The 20-hour take-home** — Disrespects candidate time, biases toward people with free time, and the best candidates will drop out.

- **The "rockstar/ninja" JD** — Signals immaturity. Senior candidates run from these.

- **Ghosting candidates** — Especially after a work sample. This is how you build a reputation that kills your pipeline.

- **Consensus-based decisions** — "Everyone needs to agree" selects for inoffensive mediocrity. The hiring manager decides.

- **Hiring for potential without structure** — "I see myself in them" is bias, not signal.

<!-- Talk track: Before we close, let me rattle off the hiring anti-patterns I see most often in analytics. Culture fit as a criterion — this almost always means "this person is like me" and it is how you build a homogeneous team that has blind spots. Replace it with culture add, or better yet, define specific collaboration behaviors you are evaluating. The 20-hour take-home — the best candidates have options. They will not spend a weekend on your exercise. Two to four hours, clearly scoped. The rockstar-ninja job description — if your JD says "we are looking for a rockstar data scientist," every experienced person reading it assumes your org is chaotic and your management is absent. Ghosting candidates after a work sample is reputation destruction. And consensus-based decisions — if everyone has to agree, you will hire the person nobody objects to, which is not the same as the person someone is excited about. The hiring manager makes the call. -->

---

# Key Takeaways

1. **Start with outcomes**, not skills — the 90-day scorecard drives everything
2. **Structure beats intuition** — 0.51 vs. 0.20, every time
3. **Work samples are your best tool** — test real judgment, not trivia
4. **Calibrate before you interview** — 20 minutes of norming prevents hours of debate
5. **Candidate experience is employer brand** — 19 rejections for every 1 hire

### Deliverable Reminder

**Hiring Packet DRAFT due Thursday (23:59 Vienna)** for instructor feedback.
It will be used in Day 2 role-plays.

Components: JD + Work Sample + Rubric + Interview Loop

<!-- Talk track: Let me leave you with the five things I want you to remember from this block. First, start with outcomes, not skills. The 90-day scorecard is your anchor. Second, structure beats intuition — the research is unambiguous. Third, work samples are your best tool for analytics hiring because they test real judgment. Fourth, calibrate your scorers before you start interviewing. And fifth, candidate experience is employer brand — treat every candidate like they might be your next hire's best friend, because in data science, they probably are. Your hiring packet draft is due Thursday by midnight Vienna time. I will give written feedback, and you will use the polished version in Day 2 role-plays. -->

---

<!-- _class: divider -->

# Up Next: Block C

## Roadmaps, Bets, and Alignment
### 15:30–17:10

<!-- Talk track: We will take a 20-minute break. When you come back, Block C is about roadmaps, bets, and alignment — how you decide what your analytics team works on, how you communicate priorities to leadership, and how you say no to the 80 percent of requests that do not make the cut. See you at 15:30. -->
