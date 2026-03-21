# Block E: Infrastructure & Cross-Functional Interfaces — Facilitator Notes

**Day 2 | Block E | 13:30–15:10 (100 minutes)**

---

## Pre-Class Setup

- **Energy context:** Post-lunch after an emotionally intense Block D. Students practiced giving hard feedback and debated performance ratings this morning. They may still be processing. This block's concrete, practical content is a welcome shift — but don't assume they've fully reset.
- Have the data infrastructure blueprint template accessible for reference (`resources/data-infra-blueprint-template.md`)
- Keep the blueprint slide easily navigable — students will refer back to it during the activity
- Timer visible for the activity (20 minutes)
- No special room arrangement needed

## Opening: Post-Lunch Reset (2 min)

**What to do:** Ask students to take out a piece of paper (or open a blank doc). "Write down one thing from this morning you want to remember. It can be a framework, a feeling, a moment from the role-play. Take 90 seconds. Then set it aside — we're shifting gears."

**Why this works:** It acknowledges the emotional weight of Block D without rehashing it. Students externalize what they're carrying so they can engage with new content.

**Don't skip this** even if you're running late. It takes 90 seconds and it's the difference between students who are present and students who are still replaying their SBI role-play in their heads.

## Timing Breakdown

| Clock | Min | Duration | Content |
|-------|-----|----------|---------|
| 13:30 | 0 | 2 min | Post-lunch reset |
| 13:32 | 2 | 3 min | Why infrastructure matters |
| 13:35 | 5 | 6 min | XFN Universe + Failure Modes |
| 13:41 | 11 | 6 min | Bidirectional SLAs (template + example) |
| 13:47 | 17 | 6 min | Blueprint + Architecture Diagrams |
| 13:53 | 23 | 8 min | Build vs. Buy + Hidden Costs |
| 14:01 | 31 | 2 min | **Pair discussion: build or buy one tool** |
| 14:03 | 33 | 3 min | Stack progression story |
| 14:06 | 36 | 3 min | Small Org Stack |
| 14:09 | 39 | 3 min | Medium Org Stack |
| 14:12 | 42 | 3 min | Large Org Stack |
| 14:15 | 45 | 2 min | Migration Trap |
| 14:17 | 47 | 3 min | What You Inherit |
| 14:20 | 50 | 3 min | Privacy & Governance Basics |
| 14:23 | 53 | 20 min | **Activity: Data Infra Decision Brief** |
| 14:43 | 73 | 15 min | Debrief + Share-Out |
| 14:58 | 88 | 12 min | Buffer / transition |

## Key Teaching Points

### Must Emphasize
- The blueprint is a **mental model**, not a prescription — students should adapt it to their case
- **Build vs. Buy default:** buy infrastructure, build business logic
- **Procurement timelines are real** (2–6x longer than you expect) — folded into the build-vs-buy talk track
- **Opportunity cost** is the hidden killer in build-vs-buy decisions
- **You will inherit, not build** — audit before you propose

### Can Compress If Running Long
- Stack sections (11 min → 6 min, hit the progression story, skip tool details in Medium/Large)
- Privacy slide can be compressed to one sentence if truly behind
- With 12 minutes of buffer, you have comfortable flexibility

### Do Not Skip
- Build vs. Buy framework (students will face this immediately in their careers)
- Stack progression story (the narrative of how stacks evolve is the real lesson)
- The activity (hands-on application is irreplaceable)
- The share-out (the VP proposals bridge directly to Block F)

## Lecture Teaching Notes

### Why Infrastructure Matters (3 min)
Hit the business case fast: "These are 2-3 year commitments. Migrations are brutal." The pipeline-broke-over-the-weekend story in the talk track is your hook — tell it like it happened to you (or someone you know). Don't linger. This slide motivates the block; the substance comes next.

### XFN Universe + Failure Modes (6 min)
The failure modes slide is the most vivid content in the block — lean into it. Tell the schema change / CEO dashboard story with energy. Ask: "Has anyone here experienced something like this? Even as an IC?" Hands will go up. That validates the content and wakes the room up post-lunch.

**Key move:** After the failure modes, say: "Each of these is preventable. The tool is an SLA." That sets up the next section.

### Bidirectional SLAs (6 min, 2 slides)
The template slide is abstract. The example slide makes it real. Don't rush the example — read it aloud. "Analytics will review schema change impacts within three business days. Engineering will notify analytics two sprints before any schema change." Then ask: "What does each side get from this?" The answer — mutual predictability — is the insight.

**Common student reaction:** "This feels bureaucratic." Response: "SLAs feel bureaucratic until your pipeline breaks at 2 AM because nobody told you about a schema change. Then they feel like insurance you should have bought."

### Blueprint + Architecture Diagrams (6 min)
The talk track walks through a concrete data flow (click event → Fivetran → BigQuery → dbt → semantic layer → Looker). **Actually walk through it slowly** — point at each layer as you describe it. Students who've never thought about infrastructure need to see the flow animated by your voice and gestures, not just read it.

The architecture table on the next slide translates each layer into plain English with a manager's key question. The key questions column is the most important — "you don't need to know how ingestion works, you need to know how fresh the data is."

### Build vs. Buy + Hidden Costs (8 min)
The four-question framework is the intellectual core of the block. Take time with each question. The Airflow comparison table is the slide that changes minds — let the numbers speak. "$30K-50K in engineer salary to run a 'free' tool. Versus $4K-14K for managed."

End with the procurement and AI additions in the talk track. These are one sentence each — don't expand them into mini-lectures.

### Pair Discussion (2 min)
"Turn to your neighbor. Name one tool your case context needs. Build or buy? Use the four questions."

This breaks the lecture at minute 31. Keep it to 2 minutes — it's an energy break, not a deep exercise. Don't do a share-out here; save that for the main activity debrief.

### Stack Progression Story (3 min)
This is the narrative frame for the next three slides. "You start scrappy. You add observability when you get burned. You add governance when you get audited." Tell it as a story, not a list. The three stack slides that follow illustrate this story — without this framing, they're just tool catalogs.

### Small / Medium / Large Org Stacks (9 min total)
These slides are reference material presented as lecture — the weakest format in the block. To make them work:
- **Small org:** "Notice almost everything is 'buy.'" Point out the governance row: "A spreadsheet. Seriously."
- **Medium org:** "The critical addition is observability. Everything else is important, but observability is what stops you from getting paged at 2 AM."
- **Large org:** "Your challenge isn't the tools — it's organizational alignment." Don't read the table; hit the governance point.

If energy dips during these slides, that's expected. The migration trap slide wakes them back up.

### Migration Trap (2 min)
"The custom pipeline one engineer built, who then left." Every analytics professional has seen this. It's a 2-minute slide that plants a seed. Don't expand it.

### What You Inherit (3 min)
This is one of the most practical slides in the block. "You will almost never build from scratch. You will inherit." Read the four audit questions aloud. The "who owns each pipeline?" question usually gets a knowing reaction.

**Connect to Block D:** "This is the First 90 Days framework applied to infrastructure — spend 30 days understanding before spending 30 minutes proposing."

### Privacy & Governance (3 min)
Frame for CEU Vienna students: "This isn't optional knowledge — it's your legal reality." Hit the three GDPR concepts fast. The data classification tiers (Public/Internal/Confidential/Restricted) are the most actionable takeaway — "every table in your warehouse should have a classification."

Don't expand this into a privacy lecture. Three minutes. The self-study guide has the details.

## Activity: Data Infra Decision Brief (20 min)

Students write a focused decision brief with 3 items.

**What they produce:**
1. **Current state** (5 min) — what exists, biggest pain point
2. **AI impact** (8 min) — pick one lens (infrastructure, people, or governance) and be specific about how AI changes their case context
3. **VP proposal** (7 min) — one paragraph in BLUF format: what they need, why, cost, consequence of no

**Show the example slide** before students start writing. Walk through it briefly: "Notice the current state is one sentence. The AI impact picks a specific lens and names a specific incident. The VP proposal leads with what's needed. Aim for this level of specificity."

**Circulate actively.** Common mistakes to coach:
- Item 1: Describing the dream state instead of the current pain point. Redirect: "What's broken right now?"
- Item 2: Being vague about AI ("we should use AI more"). Push for specifics: which tool, what cost, what risk, what policy
- Item 3: Burying the ask. First sentence should be what they need. If it starts with context, redirect: "BLUF — what do you need?"

**If a student freezes on AI lens:** Ask "what scares you most about AI in your case?" That usually points to the right lens — scared of cost = infrastructure, scared of quality = people, scared of compliance = governance.

**If students finish early:** Have them write a second VP proposal from a different AI lens.

**The decision brief is NOT a graded artifact** but practices BLUF for Block F and feeds into the optional Data Infrastructure Blueprint portfolio item.

## Debrief + Share-Out (15 min)

**Share-out (8 min):**
- Ask for 2-3 volunteers to read their VP proposal aloud (60 seconds each)
- After each: "Class — is the BLUF clear? Can you tell what they need in the first sentence? Would you fund it?"
- If nobody volunteers: pick one student from each case context size and ask them to share just item 3. "Just read me your VP paragraph."
- Don't critique harshly — this is practice, not grading. "Good BLUF" or "I'd want to know the cost before I said yes" is the right level.

**Discussion (7 min):**
- "What AI lens did you pick? What made you choose it?"
- "Did anyone pick a different lens than they expected?"
- Surface the pattern: case context drives AI strategy — startups worry about cost, enterprises worry about compliance
- "How does your infrastructure plan connect to your roadmap from Day 1?"

**Closing the block:** "The VP proposals you just wrote are exactly the skill Block F formalizes. You just practiced the Art of the Ask — in Block F we'll give it a name and a framework."

## Connection to Portfolio

- **Data Infrastructure Blueprint:** optional artifact, template at `resources/data-infra-blueprint-template.md`
- **RFP Scoring Matrix:** optional artifact, template at `resources/rfp-scoring-matrix-template.md`
- Neither is required but both demonstrate additional depth

## Common Questions and How to Handle Them

**"Should we use Snowflake or BigQuery?"**
Redirect: "Great question — let's apply the framework. Is this a core differentiator? No. Do you have the team to self-host? Apply the four questions to your case context." Do not recommend specific vendors.

**"What about AI/LLM infrastructure?"**
Acknowledge: "The stack is evolving fast. Model serving, vector databases, and LLM API costs are becoming a real layer. The activity asks you to think about this directly — pick the AI lens that matters most for your case."

**"This seems like a lot of tools. Do we really need all of them?"**
Redirect: "That's exactly the right instinct. The small org stack has 4-5 tools. The answer to 'do we need this?' is always 'what pain does it solve, and do we feel that pain yet?'"

**"How do I convince my CTO/VP to approve a tool purchase?"**
Bridge to Block F: "That's an executive communication problem — exactly what we'll cover in Block F. You'll learn the Art of the Ask framework in about an hour. In fact, you're about to practice it in the activity."

**"What do you mean by AI lens?"**
"Think about it this way: AI affects your infrastructure (what tools you buy), your people (how they work and what you hire for), and your governance (what policies you need). Pick whichever dimension feels most urgent or risky for your specific case context."

**"Can I write about something not related to AI?"**
"The AI impact item is specifically about AI because it's the biggest change in analytics management right now. But if your case context genuinely doesn't have an AI angle, write about the infrastructure or people challenge that IS most urgent — just be specific about why."

## Vendor Neutrality

Maintain absolute vendor neutrality. Use specific tool names only as examples of categories, never as recommendations. When students ask "should we use X or Y?" redirect to the framework.

## Materials Checklist

- [ ] Infrastructure slides loaded and tested
- [ ] Data infrastructure blueprint template accessible
- [ ] RFP scoring matrix template accessible (for reference/homework)
- [ ] Timer visible for activity (20 minutes)
- [ ] Blueprint anchor slide easily navigable during activity
- [ ] Example decision brief slide ready (students see it before starting)
