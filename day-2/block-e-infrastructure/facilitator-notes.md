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
| 13:32 | 2 | 4 min | Why infrastructure matters |
| 13:36 | 6 | 6 min | XFN Universe + Failure Modes |
| 13:42 | 12 | 6 min | Bidirectional SLAs |
| 13:48 | 18 | 8 min | Blueprint + Architecture Diagrams |
| 13:56 | 26 | 8 min | Build vs. Buy + Hidden Costs |
| 14:04 | 34 | 2 min | **Pair discussion: build or buy one tool** |
| 14:06 | 36 | 10 min | Stack by Size (small/medium/large + migration trap) |
| 14:16 | 46 | 6 min | IT, Procurement, Privacy basics |
| 14:22 | 52 | 30 min | **Activity: Data Infra One-Pager** |
| 14:52 | 82 | 8 min | Debrief + portfolio connection |
| 15:00 | 90 | 10 min | Buffer / transition |

## Key Teaching Points

### Must Emphasize
- The blueprint is a **mental model**, not a prescription — students should adapt it to their case
- **Build vs. Buy default:** buy infrastructure, build business logic
- **IT is a partner, not a blocker** — involve them early
- **Procurement timelines are real** (2–6x longer than you expect)
- **Opportunity cost** is the hidden killer in build-vs-buy decisions

### Can Compress If Running Long
- IT, Procurement, Privacy (6 min → 3 min, focus on procurement timeline reality)
- With 10 minutes of buffer, you have significant flexibility

### Do Not Skip
- Build vs. Buy framework (students will face this immediately in their careers)
- Stack by Size progression (the story of how stacks evolve is the real lesson — not the specific tools)
- The activity (hands-on application is irreplaceable)

## Activity: Data Infra One-Pager (30 min)

Students sketch their case context's infrastructure stack on one page.

**What they produce:**
1. Current state — what exists, gaps, pain points
2. Target architecture — stack in 6 months, mapped to blueprint layers
3. Key tools — selection for each layer with rationale
4. Budget estimate — monthly and annual costs
5. Top risk — what could go wrong, what dependencies exist

**Circulate actively.** Common mistakes to coach away from:
- Drawing the "dream stack" instead of their actual case context constraints
- Forgetting to consider team size and skill when choosing tools
- Proposing migrations without considering the Migration Trap
- Over-engineering for small org contexts ("you don't need a data catalog for fifty tables")
- Under-scoping for large org contexts (not accounting for procurement and governance)

**The one-pager is NOT a graded artifact** but feeds into the optional Data Infrastructure Blueprint portfolio item.

**If students finish early:** Have them think about which tool choice would be hardest to explain to their CTO, and draft a one-sentence justification using the Build vs. Buy framework.

## Debrief (8 min)

**Key questions:**
- What surprised you about your case's infrastructure needs?
- Where did the Build vs. Buy framework change your initial instinct?
- What trade-offs did you make? What did you decide to skip?
- How does your infrastructure plan connect to your roadmap and executive narrative?

**Connection to Block F:** Infrastructure decisions are executive communication topics. "We need to migrate to Snowflake" is an ask that requires the Art of the Ask framework they'll learn in Block F. Plant this seed.

## Connection to Portfolio

- **Data Infrastructure Blueprint:** optional artifact, template at `resources/data-infra-blueprint-template.md`
- **RFP Scoring Matrix:** optional artifact, template at `resources/rfp-scoring-matrix-template.md`
- Neither is required but both demonstrate additional depth

## Lecture Teaching Notes

**Build vs. Buy (8 min, starts at 13:56):** Comes right after the blueprint. The key teaching moment is opportunity cost — "what your team doesn't build while maintaining infrastructure." The Airflow comparison table is designed to make this concrete. Let the numbers speak. This section is strong enough to carry post-lunch energy.

**Pair discussion (2 min, at 14:04):** This breaks the lecture at minute 34 — right when post-lunch drowsiness peaks. Students apply build-vs-buy to their own case context. It also primes them to evaluate the stack-by-size tables through the build-vs-buy lens rather than passively reading tool names.

**Stack by Size (10 min, starts at 14:06):** The story to tell is *progression*, not tools. Students now have the build-vs-buy framework, so they can evaluate each tool choice: "Notice that at the small org level, almost everything is 'buy.' At the medium level, you start making real build-vs-buy decisions. At large scale, the question shifts to build-vs-buy-vs-build-on-top-of." Linger on the *transitions* between sizes. Ask: "What changes when you go from 5 people to 50? What breaks?"

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
