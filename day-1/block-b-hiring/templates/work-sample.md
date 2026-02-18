# Work Sample Exercise Template

**Student Name:** _______________
**Date:** _______________
**Case Context:** [ ] Small (Seed-Stage) / [ ] Medium (Series B) / [ ] Large (Enterprise)
**Target Role:** _______________
**Target Level:** _______________

---

## Exercise Description

*Describe what the candidate will do in 2–3 sentences. The exercise should simulate a realistic task from the actual role. Be specific about the deliverable.*

**Example:**
> You will receive a dataset of user activity logs from a B2C mobile app. The VP of Product has asked: "Should we invest engineering resources in improving our onboarding flow, or focus on retention of existing users?" Analyze the data, form a recommendation, and present your findings in a brief written memo (1–2 pages) and a supporting analysis notebook or spreadsheet.

Your Exercise Description:

> [Write here]

---

## Business Context

*Provide the scenario the candidate will work within. Tie this directly to your case context. Give enough detail that the candidate understands the stakes and constraints, but not so much that you eliminate the need for judgment.*

**Example:**
> FitTrack is a seed-stage fitness app with 15,000 monthly active users. The company has raised a $3M seed round and has 18 months of runway. The founding team (2 engineers, 1 designer, 1 CEO) has been making product decisions based on intuition and user interviews. They recently implemented basic event tracking using Segment, but the data is messy: some events are duplicated, timestamps are inconsistent, and there are gaps during a migration in Month 3.
>
> The CEO believes onboarding is the bottleneck — only 30% of signups complete the initial workout. The Head of Product thinks retention is the real problem — users who complete onboarding still churn at 60% within 30 days. They need an analytics-driven recommendation to allocate their next sprint.

Your Business Context:

> [Write here]

---

## Dataset Description

*Describe what data the candidate will receive. Include known issues — messy data is realistic and tests how candidates handle imperfection.*

**Example:**
> The candidate will receive three CSV files:
>
> 1. **users.csv** — 15,000 rows: user_id, signup_date, signup_source (organic, paid, referral), plan_type (free, premium)
> 2. **events.csv** — ~500,000 rows: user_id, event_name, event_timestamp, event_properties (JSON)
> 3. **sessions.csv** — ~200,000 rows: user_id, session_start, session_end, pages_viewed
>
> **Known data issues (do not share with candidate):**
> - ~5% of events have duplicate entries (same user_id, event_name, timestamp)
> - Event timestamps in Month 3 are offset by 2 hours due to a timezone migration
> - Some users in events.csv do not appear in users.csv (test accounts)
> - The "onboarding_complete" event was renamed to "setup_finished" midway through the period
>
> **Note:** You may provide a real or synthetic dataset. If synthetic, ensure it is realistic enough to support multiple valid analytical approaches.

Your Dataset Description:

> [Write here]

---

## Questions to Answer

*Provide 3–5 specific questions, escalating in difficulty. Start with descriptive analysis, move to diagnostic, and end with a judgment call.*

**Example:**
> 1. **Descriptive:** What is the current onboarding completion rate? How has it trended over the past 6 months? (Straightforward data exploration)
>
> 2. **Diagnostic:** What are the key differences between users who complete onboarding and those who don't? Which signup sources produce the highest-quality users? (Requires segmentation and comparison)
>
> 3. **Analytical:** Among users who complete onboarding, what predicts 30-day retention? Is there a specific engagement threshold that matters? (Requires more sophisticated analysis)
>
> 4. **Strategic:** Given your findings, should FitTrack prioritize improving onboarding or investing in retention? What would you recommend and why? What data would you want that you don't have? (Tests judgment and communication)
>
> 5. **Meta:** If you had one week and access to the engineering team, what would you instrument next to make this analysis more robust? (Tests analytical maturity and planning)

Your Questions:

1. [Descriptive question]
2. [Diagnostic question]
3. [Analytical question]
4. [Strategic/judgment question]
5. [Meta/planning question — optional]

---

## Time Limit & Submission Format

*Be explicit about time expectations and what you want delivered. Respecting candidate time is non-negotiable.*

**Recommended defaults:**
> - **Time limit:** 3 hours (do not exceed 4 hours)
> - **Submission format:** A written memo (1–2 pages, PDF) summarizing findings and recommendations, plus a supporting analysis file (notebook, spreadsheet, or SQL file)
> - **Due:** 5 business days after receiving the exercise
> - **Questions:** Candidates may email [contact] with clarifying questions (responses within 24 hours)
>
> **Important:** We value clear thinking over exhaustive analysis. A focused, well-communicated analysis of Questions 1–3 is better than a rushed attempt at all 5. Show your work and explain your reasoning.

Your Time Limit & Format:

> [Write here]

---

## Evaluation Rubric for This Exercise

*Define how each question/dimension will be scored. Use the same 1–4 scale as your main rubric.*

| Dimension | 1 — Novice | 2 — Developing | 3 — Proficient | 4 — Expert |
|:---|:---|:---|:---|:---|
| **Problem Framing** | Jumps to analysis without understanding the business question | Acknowledges the business question but does not clarify scope or assumptions | Frames the problem clearly, states assumptions, identifies what is in/out of scope | Reframes the question productively, identifies what the stakeholder really needs to know |
| **Data Quality Handling** | Ignores data issues | Notices issues but does not address them | Identifies and handles major data quality issues appropriately | Proactively documents issues, explains impact on analysis, and adjusts methodology |
| **Analytical Rigor** | Analysis contains errors or uses inappropriate methods | Analysis is correct but surface-level | Sound methodology, appropriate techniques, handles edge cases | Sophisticated approach, considers alternatives, validates assumptions |
| **Communication** | Findings are unclear or buried in technical detail | Findings are stated but not connected to the business question | Clear narrative connecting analysis to business recommendation | Compelling, concise memo that a non-technical executive could act on |
| **Judgment** | No recommendation or recommendation unsupported by analysis | Recommendation present but weakly supported | Clear recommendation with supporting evidence and acknowledged limitations | Nuanced recommendation with tradeoffs, next steps, and what additional data would change the answer |

---

## Evaluation Criteria

This work sample exercise will be assessed on the following dimensions:

| Criterion | What We Are Looking For |
|:---|:---|
| **Realism** | Does the exercise reflect tasks the candidate would actually perform in the role? Is the business context believable? |
| **Respect for Time** | Is the exercise completable in 2–4 hours? Are expectations about scope clearly communicated? |
| **Escalating Difficulty** | Do the questions move from descriptive to diagnostic to strategic? Can you distinguish strong from weak candidates? |
| **Rubric Alignment** | Does the evaluation rubric cover the dimensions that matter? Could a different evaluator use it and reach similar conclusions? |
| **Case Context Fit** | Is the exercise tailored to your specific company scenario, not generic? |
