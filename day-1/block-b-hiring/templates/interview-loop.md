# Interview Loop Design Template

**Student Name:** _______________
**Date:** _______________
**Case Context:** [ ] Small (Seed-Stage) / [ ] Medium (Series B) / [ ] Large (Enterprise)
**Target Role:** _______________
**Target Level:** _______________

---

## Interview Stages

*Design the full interview process from first contact to final decision. Each stage should have a clear purpose — if you cannot articulate what signal a stage provides, cut it.*

### Stage Overview

| Stage | Interviewer Role | Focus Area | Duration | Format | Signal Being Tested |
|:---|:---|:---|:---|:---|:---|
| 1. Recruiter Screen | Recruiter / Hiring Manager | Basic qualifications, motivation, logistics | 30 min | Phone/Video | Baseline fit, compensation alignment, availability |
| 2. Work Sample | N/A (asynchronous) | Technical skill, judgment, communication | 3 hours (candidate time) | Take-home | Core job capability (see Work Sample template) |
| 3. Work Sample Review | Technical Peer | Depth of craft, methodology, code quality | 45 min | Video/In-person | Can they explain and defend their work? |
| 4. Hiring Manager Interview | Hiring Manager | Role fit, 90-day plan, team dynamics | 45 min | Video/In-person | Will they thrive in this specific role and team? |
| 5. Cross-Functional Interview | PM / Eng Lead / Stakeholder | Collaboration, communication, business sense | 45 min | Video/In-person | Can they partner effectively across functions? |
| 6. Skip-Level / Values | Skip-level Manager or Founder | Judgment, growth potential, culture add | 30 min | Video/In-person | Long-term trajectory, alignment with org values |

**Customize this table for your case context.** A seed-stage startup may collapse stages 4–6 into one conversation. A large enterprise may add additional stages. The minimum viable loop is: Screen + Work Sample + One Interview.

### Your Interview Stages

| Stage | Interviewer Role | Focus Area | Duration | Format | Signal Being Tested |
|:---|:---|:---|:---|:---|:---|
| 1. | | | | | |
| 2. | | | | | |
| 3. | | | | | |
| 4. | | | | | |
| 5. | | | | | |

---

## Debrief Protocol

*Define exactly how the hiring decision is made. The debrief is where most hiring processes break down — unclear ownership, anchoring to the loudest voice, and consensus-seeking produce bad outcomes.*

### Before the Debrief

1. **All interviewers submit scorecards independently** within 24 hours of their interview
2. No discussion of the candidate between interviewers before scorecards are submitted
3. Hiring manager collects all scorecards and reviews for patterns before the meeting

### During the Debrief (30 minutes)

| Step | Duration | What Happens |
|:---|:---|:---|
| 1. Score Share | 5 min | Hiring manager displays all scores (no names attached initially). Team sees the pattern. |
| 2. Round Robin | 15 min | Each interviewer shares their recommendation and top 2 observations. No interruptions. Start with the most junior interviewer to prevent anchoring. |
| 3. Discussion | 5 min | Open discussion focused on areas of disagreement. What did different interviewers see? |
| 4. Decision | 5 min | Hiring manager states the decision and reasoning. This is NOT a vote. |

### Decision Options

- **Strong Hire:** Move to offer immediately. At least one "strong hire" and no "strong no hire" scores.
- **Hire:** Move to offer. Majority positive, concerns are addressable with onboarding/coaching.
- **No Hire:** Reject with specific, kind feedback. Concerns outweigh strengths for this role at this time.
- **Strong No Hire:** Reject. Fundamental mismatch on a critical dimension.

### Your Debrief Protocol Notes

> [Customize for your context: Who runs the debrief? How quickly after the final interview? What if the hiring manager is overruled by data?]

---

## Candidate Communication Plan

*Map every touchpoint with the candidate. Silence is the enemy of candidate experience. Define who sends what, when.*

### Communication Timeline

| Trigger | Action | Owner | Channel | Timeline |
|:---|:---|:---|:---|:---|
| Application received | Acknowledgment email | Recruiter / ATS | Email | Within 48 hours |
| After recruiter screen | Next steps or rejection | Recruiter | Email | Within 3 business days |
| Work sample sent | Instructions + timeline + contact for questions | Hiring Manager | Email | Same day as screen pass |
| Work sample received | Confirmation of receipt | Recruiter / ATS | Email | Within 24 hours |
| Interview scheduled | Calendar invite + interview guide (who they will meet, what to expect) | Recruiter | Email + Calendar | 3+ business days before |
| After final interview | Status update (even if "still deciding") | Hiring Manager | Email | Within 48 hours |
| Offer | Verbal offer call, followed by written offer | Hiring Manager | Phone + Email | Within 3 business days of debrief |
| Rejection (after interviews) | Personalized rejection with brief, specific feedback | Hiring Manager | Email | Within 3 business days of debrief |

### Template: Rejection After Work Sample

> Subject: Update on your application for [Role] at [Company]
>
> Hi [Name],
>
> Thank you for completing the work sample exercise for the [Role] position. We appreciate the time and thought you put into it.
>
> After careful review, we have decided to move forward with other candidates whose experience more closely aligns with [specific area — e.g., "our need for deep SQL optimization experience" or "experience communicating analytical findings to executive stakeholders"].
>
> This is not a reflection of your overall ability — your [specific strength] stood out to our team. We would welcome the opportunity to consider you for future roles that might be a better match.
>
> Thank you again for your interest in [Company].

### Template: Rejection After Interviews

> Subject: Update on your application for [Role] at [Company]
>
> Hi [Name],
>
> Thank you for taking the time to interview with our team for the [Role] position. We enjoyed learning about your experience with [specific thing they discussed].
>
> After thoughtful deliberation, we have decided to move forward with another candidate. The decision was close, and we particularly valued your [specific strength]. Ultimately, we prioritized [specific factor — e.g., "hands-on experience with our specific data stack" or "experience operating in an early-stage environment with high ambiguity"].
>
> We would be glad to stay in touch, and we encourage you to apply for future openings that align with your strengths.

### Your Communication Plan Notes

> [Customize: Who owns candidate communication at your company? What tools do you use? What is your response time commitment?]

---

## Decision Framework

*Define how final decisions are made, especially in edge cases. This prevents post-hoc rationalization and ensures consistency across candidates.*

### Decision Authority

- **Final decision maker:** Hiring Manager
- **Veto power:** Any interviewer can raise a "strong no hire" that must be discussed, but the hiring manager retains final authority
- **Escalation:** If the hiring manager and skip-level disagree, [define your escalation path]

### Handling Split Decisions

| Scenario | Action |
|:---|:---|
| All interviewers agree (hire or no-hire) | Proceed with the consensus |
| Majority hire, one dissent | Hiring manager evaluates the dissent. If the concern is on a critical dimension, investigate further (e.g., additional reference check). Otherwise, proceed with hire. |
| Majority no-hire, one strong advocate | Default to no-hire. One enthusiastic voice does not overcome multiple concerns. |
| Even split | Hiring manager makes the call based on role priorities. Document reasoning. Consider whether additional signal is needed (e.g., a brief follow-up conversation). |
| Concerns about a coachable skill | Hire with a 90-day development plan for the specific gap. Document the gap and the plan. |
| Concerns about judgment or integrity | Do not hire. These are not coachable in the short term. |

### Reference Checks

- Conduct **after** the interview loop, **before** the offer
- Ask references: "What does this person need from their manager to be successful?"
- Ask references: "If you were hiring for [your specific role], would you hire this person? Why or why not?"
- Use references to **confirm** signals from interviews, not to generate new ones

### Your Decision Framework Notes

> [Customize: What is unique about decision-making at your case context company? What tradeoffs matter most?]

---

## Evaluation Criteria

This interview loop design will be assessed on the following dimensions:

| Criterion | What We Are Looking For |
|:---|:---|
| **Stage Design** | Does each stage have a clear, distinct purpose? Is there redundancy? Is the total process respectful of candidate time? |
| **Signal Coverage** | Across all stages, are you evaluating technical skill, communication, collaboration, judgment, and culture add? No gaps? |
| **Debrief Rigor** | Is the debrief protocol designed to prevent anchoring and groupthink? Are scores collected independently? |
| **Candidate Communication** | Is the communication plan specific and timely? Would a candidate feel respected throughout the process? |
| **Decision Framework** | Is it clear how decisions are made, especially in ambiguous cases? Is the hiring manager empowered to decide? |
