# Block E: Infrastructure & Cross-Functional Interfaces — Facilitator Notes

**Day 2 | Block E | 13:30–15:10 (100 minutes)**

---

## Pre-Class Setup

- **Energy context:** Post-lunch. This block is intellectually engaging but not emotionally heavy — concrete, practical content works well for post-lunch energy. The shift from Block D's intensity to practical infrastructure topics is welcome.
- Have the data infrastructure blueprint template accessible for reference during the activity (`resources/data-infra-blueprint-template.md`)
- Keep anchor slides (Blueprint + Architecture Diagrams) visible/accessible as reference during the activity
- Timer visible for the one-pager activity (30 minutes)
- No special room arrangement needed

## Opening: Post-Lunch Reset (2 min)

The 90-second breathing exercise acknowledges the shift from Block D's emotional intensity to practical content. Frame it: "We're moving from the emotional work of growing people to the practical work of infrastructure and cross-functional relationships."

## Timing Breakdown

| Clock | Min | Duration | Content |
|-------|-----|----------|---------|
| 13:30 | 0 | 2 min | Post-lunch reset |
| 13:32 | 2 | 3 min | Why infrastructure matters |
| 13:35 | 5 | 6 min | XFN Universe + Failure Modes |
| 13:41 | 11 | 6 min | Bidirectional SLAs (template + example on one slide) |
| 13:47 | 17 | 6 min | Blueprint + Architecture Diagrams |
| 13:53 | 23 | 8 min | Build vs. Buy + Hidden Costs |
| 14:01 | 31 | 2 min | **Pair discussion: build or buy one tool** |
| 14:03 | 33 | 3 min | Stack progression story (how stacks evolve) |
| 14:06 | 36 | 3 min | Small Org Stack |
| 14:09 | 39 | 3 min | Medium + Large Org Stacks |
| 14:12 | 42 | 2 min | Migration Trap |
| 14:14 | 44 | 3 min | What You Inherit (first-month audit) |
| 14:17 | 47 | 3 min | Privacy & Governance Basics (GDPR, classification) |
| 14:19 | 49 | 20 min | **Activity: Data Infra Decision Brief** |
| 14:39 | 69 | 15 min | Debrief + Share-Out |
| 14:54 | 84 | 16 min | Buffer / transition |

## Key Teaching Points

### Must Emphasize
- The blueprint is a **mental model**, not a prescription — students should adapt it to their case
- **Build vs. Buy default:** buy infrastructure, build business logic
- **Procurement timelines are real** (2–6x longer than you expect) — folded into the build-vs-buy talk track
- **Opportunity cost** is the hidden killer in build-vs-buy decisions

### Can Compress If Running Long
- Stack sections (11 min → 6 min, hit the progression story, skip tool details in Medium/Large)
- Privacy slide can be compressed to one sentence if truly behind
- With 13 minutes of buffer, you have comfortable flexibility

### Do Not Skip
- Build vs. Buy framework (students will face this immediately in their careers)
- Stack by Size progression (the story of how stacks evolve is the real lesson — not the specific tools)
- The activity (hands-on application is irreplaceable)

## Activity: Data Infra Decision Brief (20 min)

Students write a focused decision brief with 3 items.

**What they produce:**
1. **Current state** (5 min) — what exists, biggest pain point
2. **AI impact** (8 min) — pick one lens (infrastructure, people, or governance) and be specific about how AI changes their case context
3. **VP proposal** (7 min) — one paragraph in BLUF format: what they need, why, cost, consequence of no

**Circulate actively.** Common mistakes to coach:
- Item 1: Describing the dream state instead of the current pain point
- Item 2: Being vague about AI ("we should use AI more"). Push for specifics: which tool, what cost, what risk, what policy
- Item 3: Burying the ask. First sentence should be what they need. If it starts with context, redirect: "BLUF — what do you need?"

**If a student freezes on AI lens:** Ask "what scares you most about AI in your case?" That usually points to the right lens — scared of cost = infrastructure, scared of quality = people, scared of compliance = governance.

**If students finish early:** Have them write a second VP proposal from a different AI lens.

**The decision brief is NOT a graded artifact** but feeds into the optional Data Infrastructure Blueprint portfolio item and practices BLUF for Block F.

## Debrief + Share-Out (15 min)

**Share-out (8 min):**
- Ask for 2-3 volunteers to read their VP proposal aloud (60 seconds each)
- After each: "Class — is the BLUF clear? Can you tell what they need in the first sentence? Would you fund it?"
- If nobody volunteers: pick someone from each case context and ask them to share just item 3

**Discussion (7 min):**
- "What AI lens did you pick? What made you choose it?"
- "Did anyone pick a different lens than they expected?"
- Surface the pattern: case context drives AI strategy

**Connection to Block F:** The VP proposals students just wrote are exactly the skill Block F formalizes. "You just practiced the Art of the Ask — in Block F we'll give it a name and a framework."

## Connection to Portfolio

- **Data Infrastructure Blueprint:** optional artifact, template at `resources/data-infra-blueprint-template.md`
- **RFP Scoring Matrix:** optional artifact, template at `resources/rfp-scoring-matrix-template.md`
- Neither is required but both demonstrate additional depth

## Lecture Teaching Notes

**Build vs. Buy (8 min, starts at 13:54):** Comes right after the blueprint. The key teaching moment is opportunity cost — "what your team doesn't build while maintaining infrastructure." The Airflow comparison table is designed to make this concrete. Let the numbers speak. End this section with the procurement reality: "When you buy, involve IT from day one. Procurement takes 2-6x longer than you expect." This folds in the essential IT/procurement lesson without a separate slide.

**Pair discussion (2 min, at 14:02):** This breaks the lecture at minute 34 — right when post-lunch drowsiness peaks. Students apply build-vs-buy to their own case context. It also primes them to evaluate the stack-by-size tables through the build-vs-buy lens rather than passively reading tool names.

**Stack by Size (10 min, starts at 14:04):** The story to tell is *progression*, not tools. Students now have the build-vs-buy framework, so they can evaluate each tool choice: "Notice that at the small org level, almost everything is 'buy.' At the medium level, you start making real build-vs-buy decisions. At large scale, the question shifts to build-vs-buy-vs-build-on-top-of." Linger on the *transitions* between sizes. Ask: "What changes when you go from 5 people to 50? What breaks?"

## Common Questions and How to Handle Them

**"Should we use Snowflake or BigQuery?"**
Redirect: "Great question — let's apply the framework. Is this a core differentiator? No. Do you have the team to self-host? Apply the four questions to your case context." Do not recommend specific vendors.

**"What about AI/LLM infrastructure?"**
Acknowledge: "The stack is evolving fast. Model serving, vector databases, and LLM API costs are becoming a real layer. For this exercise, focus on the data stack foundations — but if you're in a case context where ML is core, note where model infrastructure fits."

**"This seems like a lot of tools. Do we really need all of them?"**
Redirect: "That's exactly the right instinct. The small org stack has 4-5 tools. The answer to 'do we need this?' is always 'what pain does it solve, and do we feel that pain yet?'"

**"How do I convince my CTO/VP to approve a tool purchase?"**
Bridge to Block F: "That's an executive communication problem — exactly what we'll cover in Block F. You'll learn the Art of the Ask framework in about an hour."

## Vendor Neutrality

Maintain absolute vendor neutrality. Use specific tool names only as examples of categories, never as recommendations.

## Materials Checklist

- [ ] Infrastructure slides loaded and tested
- [ ] Data infrastructure blueprint template accessible
- [ ] RFP scoring matrix template accessible (for reference/homework)
- [ ] Timer visible for activity
- [ ] Blueprint anchor slide easily navigable during activity
