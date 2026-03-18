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
| 13:56 | 26 | 10 min | Stack by Size (small/medium/large + migration trap) |
| 14:06 | 36 | 8 min | Build vs. Buy + Hidden Costs |
| 14:14 | 44 | 6 min | RFP Process + Scoring overview |
| 14:20 | 50 | 6 min | IT, Procurement, Privacy basics |
| 14:26 | 56 | 30 min | **Activity: Data Infra One-Pager** |
| 14:56 | 86 | 8 min | Debrief + portfolio connection |
| 15:04 | 94 | 6 min | Buffer / transition |

## Key Teaching Points

### Must Emphasize
- The blueprint is a **mental model**, not a prescription — students should adapt it to their case
- **Build vs. Buy default:** buy infrastructure, build business logic
- **IT is a partner, not a blocker** — involve them early
- **Procurement timelines are real** (2–6x longer than you expect)
- **Opportunity cost** is the hidden killer in build-vs-buy decisions

### Can Compress If Running Long
- RFP Process + Scoring (6 min → 3 min, just hit the highlights)
- IT, Procurement, Privacy (6 min → 3 min, focus on procurement timeline reality)
- These two sections are the **safety valve** — 12 min → 6 min if needed

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

## Vendor Neutrality

Maintain absolute vendor neutrality. Use specific tool names only as examples of categories, never as recommendations. Students will ask "should we use Snowflake or BigQuery?" — redirect to the Build vs. Buy framework and their specific case context constraints.

## Materials Checklist

- [ ] Infrastructure slides loaded and tested
- [ ] Data infrastructure blueprint template accessible
- [ ] RFP scoring matrix template accessible (for reference/homework)
- [ ] Timer visible for activity
- [ ] Blueprint anchor slide easily navigable during activity
