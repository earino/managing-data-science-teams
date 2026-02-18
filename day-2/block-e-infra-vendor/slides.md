---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 2 – Block E"
---

# XFN, Vendor, IT & Data Infrastructure

**Day 2 — Block E | 13:30–15:10**

**Learning Outcomes**
By the end of this block you will be able to:
- Map cross-functional interfaces and document bidirectional SLAs
- Plan small-org data infrastructure across the canonical data stack layers
- Apply a build-vs-buy framework grounded in Total Cost of Ownership
- Evaluate vendors using a structured RFP scoring matrix

<!-- Talk track: Welcome back from lunch. This is the most technical block of the course, but I want to be clear — it's technical in the way a manager needs to be technical. You don't need to configure a Snowflake instance. You need to know what questions to ask, what trade-offs exist, and how to work with IT, Legal, and Engineering to make infrastructure decisions that your team can live with for the next two years. By the end of this session, you'll have two artifacts: a data infrastructure blueprint and a vendor scoring matrix. Both anchored to your case context. Let's go. -->

---

## Your Cross-Functional Universe

Analytics doesn't exist in a vacuum. Your key interfaces:

| Interface | What they care about |
|---|---|
| **Product** | What to measure, experiment results |
| **Engineering** | How to collect data, system reliability |
| **Design** | What to surface to users |
| **Legal / Privacy** | What you can store, for how long |
| **Finance** | What it all costs |
| **IT / Infra** | Where it runs, who has access |

**Mental model:** Analytics sits at the center of a hub-and-spoke. Every spoke is a relationship you must actively manage.

<!-- Talk track: Let's start with context. In Block A, you built a stakeholder map. Now we're going to zoom in on the cross-functional relationships that matter most for infrastructure and data decisions. Analytics sits at the center of this universe — not because we're the most important team, but because data touches everything. Product needs you to measure their features. Engineering needs you to not break their systems with heavy queries. Design needs you to surface insights in the product. Legal needs you to not get the company sued. Finance needs to understand what this all costs. And IT needs to make sure it's secure and compliant. Every one of these relationships is bidirectional, and every one of them will shape your infrastructure choices. -->

---

## What Each Team Needs From You

| Team | They need from you |
|---|---|
| **Product** | Metrics definitions, experiment results, self-serve dashboards |
| **Engineering** | Data contracts, SLAs for pipeline load, schema documentation |
| **Legal / Privacy** | Data inventories, consent tracking, retention schedules |
| **Finance** | Cost attribution by team/project, ROI analysis on data tools |
| **IT** | Security compliance docs, vendor onboarding paperwork |
| **Design** | User behavior data, funnel analysis, UX metrics |

The pattern: every team needs **clarity** and **documentation** from you. Not just insights — operating agreements.

<!-- Talk track: Let's get specific about what each team needs from analytics. Product needs metrics definitions — and they need those definitions to be stable, documented, and trustworthy. Engineering needs data contracts — agreements about what data you'll produce, what schema it follows, and what the SLAs are. Legal needs a data inventory — what PII do you have, where does it live, who can access it, and when does it get deleted? Finance needs to know what your stack costs and whether it's worth it. IT needs to know that every vendor you onboard meets their security requirements. Notice the pattern: everyone needs documentation and agreements from you. This is why we spent time on artifacts in Block A. Your Manager OS produces the documents that make these relationships work. -->

---

## What You Need From Them

| Team | You need from them |
|---|---|
| **Product** | Clear business questions, prioritized. Not "can you look into this?" |
| **Engineering** | Reliable event instrumentation, schema changes communicated in advance |
| **Legal** | Timely privacy reviews, clear guidance on data usage |
| **Finance** | Reasonable budget cycles, approval velocity |
| **IT** | Procurement timelines, cloud access, SSO provisioning |

**The key insight:** These relationships are **bidirectional contracts**. Document them as SLAs.

*"Engineering will notify analytics 2 sprints before any schema change to tracked events."*

That's not bureaucracy. That's how you stop your pipelines from breaking at 2 AM.

<!-- Talk track: Now flip it around. What do you need from them? Product needs to give you clear, prioritized business questions — not vague "can you look at the data?" requests. Engineering needs to tell you when they change schemas — because if they rename a field and your pipeline breaks, that's on both of you. Legal needs to be responsive on privacy reviews, not a 6-week black hole. IT needs to provision cloud access in days, not months. Here's the big idea: document these as bidirectional SLAs. Literally write them down. "Engineering will notify analytics 2 sprints before any schema change to tracked events. Analytics will provide a data impact assessment within 3 business days of any privacy review request." That's not bureaucracy. That's how adults collaborate. Who has been burned by a surprise schema change? -->

---

## The Data Infrastructure Blueprint

The canonical flow — every modern data stack follows this pattern:

**Sources** --> **Ingestion** --> **Storage** --> **Transform** --> **Semantic Layer** --> **Visualization**

With cross-cutting concerns at every layer:

- **Governance:** Who owns what? Who can access what?
- **Observability:** Is it working? How do you know?
- **Cost management:** What does each layer cost?

This is the map. Your case context determines the territory.

**Anchor this slide.** We'll come back to it throughout the block.

<!-- Talk track: Here's the big picture. Every modern data stack follows this flow: you have sources of data — your product database, event streams, third-party APIs. You ingest that data into a central store. You store it — in a warehouse or lakehouse. You transform it — clean it, model it, make it trustworthy. You build a semantic layer — agreed-upon definitions of your metrics. And you visualize it — dashboards, reports, self-serve exploration. Across all of these layers, you have three cross-cutting concerns: governance, observability, and cost. This diagram is the anchor for the rest of this block. When we talk about specific tools, I want you to always ask: where does this fit in the flow? Print this mental model. Tattoo it on your arm. Whatever it takes. -->

---

## Small Org Stack (0 to 1)

**Goal:** Trusted numbers, fast. Don't over-engineer.

| Layer | Tool | Why |
|---|---|---|
| **Sources** | Product DB + basic events | Start with what you have |
| **Ingestion** | Fivetran or Airbyte | Managed connectors; don't build this |
| **Storage** | BigQuery or Snowflake (free tier) | Start small, scale later |
| **Transform** | dbt (Core or Cloud) | SQL-based; version-controlled; testable |
| **Viz** | Metabase or Preset | Open-source options exist; low cost |
| **Governance** | Naming conventions + a spreadsheet | Seriously. This is enough to start. |

**Monthly cost:** $500–2,000

**What to skip:** Data catalog, ML platform, feature store, semantic layer tooling. You're not there yet.

<!-- Talk track: If you're in the small startup case context, this is your stack. I want to be very direct: your goal is trusted numbers, fast. Not a beautiful architecture diagram. Not a resume-driven stack. You need to get data from your product database into a warehouse, transform it so it's trustworthy, and put it in a dashboard that your CEO can look at every Monday. Fivetran or Airbyte for ingestion — don't build your own connectors, that's a waste of your time. BigQuery or Snowflake for storage — both have generous free tiers. dbt for transformation — it's SQL, it's version-controlled, it's testable. Metabase or Preset for visualization. And governance? At this stage, governance is a naming convention document and a spreadsheet that says who owns each table. That's it. Don't let anyone tell you that you need a data catalog at this stage. You don't. Total cost: under two thousand a month. -->

---

## Medium Org Stack (1 to N)

**Goal:** Self-serve metrics, experimentation, data trust at scale.

Add to the small stack:

| Layer | Addition | Why now |
|---|---|---|
| **Event platform** | Segment or RudderStack | Structured event collection; identity resolution |
| **Experimentation** | Statsig or Eppo | Rigorous A/B testing, not spreadsheet math |
| **Semantic layer** | dbt metrics or Cube | Single source of truth for metric definitions |
| **Catalog** | DataHub or Atlan | Discovery; lineage; tribal knowledge captured |
| **Observability** | Monte Carlo or Elementary | Know when data breaks before your stakeholders do |

**Governance:** Formal data owners. Published SLAs. Access controls.

**Monthly cost:** $10,000–30,000

<!-- Talk track: Now you're a Series B company. You have product-market fit, you're scaling, and PMs are asking for self-serve analytics and real experimentation. The small stack isn't enough anymore. You add an event platform — Segment or RudderStack — because you need structured event collection and identity resolution across platforms. You add experimentation tooling because your growth team needs real A/B tests, not eyeballing a chart. You add a semantic layer so there's one agreed-upon definition of "active user" and "revenue." You add a data catalog because there are now enough tables that people can't find what they need. And critically, you add observability — Monte Carlo or Elementary — so that you know when data is broken before the CEO messages you on Slack at 8 AM asking why the dashboard looks weird. Governance gets real here: formal data owners, published SLAs, access controls. Monthly cost: ten to thirty thousand. -->

---

## Large Org Stack (N to Scale)

**Goal:** Domain autonomy, ML at scale, regulatory compliance.

Add to the medium stack:

| Layer | Addition | Why now |
|---|---|---|
| **Architecture** | Data mesh / domain ownership | Decentralized ownership, centralized standards |
| **ML platform** | MLflow, SageMaker, or Vertex | Model training, versioning, deployment |
| **Feature store** | Feast or Tecton | Shared features across models |
| **Model governance** | Model cards, bias audits, monitoring | Regulatory and ethical requirements |
| **Cost management** | Kubecost, cloud billing dashboards | Because $100K+/mo demands accountability |
| **Data marketplace** | Internal data products catalog | Treat data as a product, not a byproduct |

**Governance:** Access controls, lineage, regulatory compliance, audit trails, data classification.

**Monthly cost:** $100,000+

<!-- Talk track: At enterprise scale, the challenges are fundamentally different. You're not trying to get trusted numbers — you're trying to maintain trust across dozens of teams, petabytes of data, and strict regulatory requirements. Data mesh becomes relevant — decentralized ownership with centralized standards. You need an ML platform because you have multiple models in production. You need a feature store because different teams keep re-deriving the same features. You need model governance — model cards, bias audits, monitoring — because regulators and your own ethics demand it. And you absolutely need cost management because at a hundred thousand a month, someone is going to ask where the money goes. For those of you in the large enterprise case context: your challenge isn't choosing tools. It's navigating procurement, proving ROI, and managing the politics of a data mesh transition. -->

---

## Build vs. Buy

**The framework — four questions in order:**

1. **Is this a core differentiator?** If yes: build.
   - Your recommendation algorithm? Build. Your data warehouse? Buy.

2. **Is this commodity infrastructure?** If yes: buy.
   - Ingestion, storage, BI tooling — these are solved problems.

3. **Do you have the team to maintain it?** If no: buy.
   - "Free" open source has a hidden cost: your engineers' time. Forever.

4. **What's the Total Cost of Ownership?**
   - License + implementation + training + maintenance + **opportunity cost**
   - The biggest hidden cost: what your team *doesn't* build while maintaining infra.

**Default to buy** for infrastructure. Default to build for business logic.

<!-- Talk track: Build versus buy is one of the most consequential decisions you'll make as an analytics leader. Here's a framework. Question one: is this a core differentiator? If your company's competitive advantage depends on a proprietary recommendation engine, build it. But your data warehouse is not a differentiator. Nobody ever won a market because they had a better warehouse. Question two: is this commodity infrastructure? Ingestion, storage, BI tools — these are solved problems. Buy them. Question three: do you have the team to maintain it? Open source is not free. Airflow is not free. It requires engineers to keep it running, upgrade it, fix it when it breaks. If you don't have those engineers, buy a managed service. Question four: what's the total cost of ownership? Add up the license, implementation, training, maintenance, and — this is the one people forget — opportunity cost. Every hour your data engineer spends maintaining Airflow is an hour they're not building the pipeline your PM needs. Default to buy for infrastructure. Default to build for business logic. -->

---

## The RFP Process

**When to RFP:** Spending >$10K/year or handling PII.

**Steps:**

1. **Define requirements** — Must-have vs. Should-have vs. Nice-to-have
2. **Weight criteria** — Not all requirements are equal
3. **Score vendors** — Structured, not vibes-based
4. **Negotiate** — Always negotiate. Always.
5. **Pilot** — 2-4 week proof of concept before committing

**Scoring dimensions:**

| Criterion | What to evaluate |
|---|---|
| **Functionality** | Does it solve the core problem? |
| **Integration** | Does it work with our existing stack? |
| **Security** | SOC 2, encryption, access controls |
| **Cost** | Total cost of ownership over 3 years |
| **Support** | Response times, dedicated CSM, community |
| **Scalability** | Will it grow with us? |

<!-- Talk track: When you're spending more than ten thousand a year or when PII is involved, you need a structured process. This is the RFP — request for proposal. Step one: define your requirements. Separate them into must-have, should-have, and nice-to-have. This is critical because vendors will try to dazzle you with features you don't need. Step two: weight the criteria. Security might be worth 25% of the score for one org and 10% for another. Step three: score each vendor on each criterion. Use a 1-to-5 scale and do it as a team so you get multiple perspectives. Step four: negotiate. I cannot stress this enough — always negotiate. SaaS pricing is almost never firm. Step five: pilot. Never commit to an annual contract without a proof of concept. Two to four weeks, real data, real users. If the vendor won't let you pilot, that tells you something. -->

---

## Working with IT & Procurement

**Speak their language:**
- Security posture, SOC 2 Type II, penetration testing
- Data residency (EU data stays in EU — GDPR requirement)
- SSO / SAML integration (no separate passwords)
- Audit logs (who accessed what, when)
- Vendor risk assessment questionnaire

**Procurement realities:**
- Budget cycle alignment — miss the window, wait a year
- Procurement takes **2–6x longer** than you think
- Legal review of contracts adds weeks
- Security review adds more weeks

**The golden rule:** Involve IT early. Not as a blocker — as a partner. Build the relationship before you need something.

<!-- Talk track: Here's where most analytics managers fail: they find a tool, fall in love with it, start a trial, build dependencies on it, and then discover that IT won't approve it because it doesn't support SSO, or it stores data outside the EU, or it hasn't completed a SOC 2 audit. Now you've wasted three months. Instead, learn to speak IT's language. SOC 2 Type II means the vendor has been independently audited for security practices — over time, not just at a point in time. Data residency means where the bits physically live — and under GDPR, EU personal data generally needs to stay in the EU. SSO means your team logs in with their company credentials, not a separate password. Audit logs mean you can prove who accessed what data and when. And here's the timeline reality: procurement takes two to six times longer than you expect. Start the conversation with IT in month one, not month six. -->

---

## Privacy & Governance Basics

**GDPR essentials for analytics managers:**

| Concept | What it means for you |
|---|---|
| **Lawful basis** | You need a legal reason to process personal data (consent, legitimate interest, etc.) |
| **Data minimization** | Collect only what you need. "We might need it someday" is not a reason. |
| **Right to erasure** | Users can ask you to delete their data. Your pipeline must support this. |
| **Consent management** | Track what users consented to. Don't use data beyond that scope. |

**Data classification — know your tiers:**
- **Public** — Can share openly (blog metrics, public benchmarks)
- **Internal** — Company-wide access (aggregate dashboards)
- **Confidential** — Need-to-know (user-level data, financial details)
- **Restricted** — Highest sensitivity (PII, health data, payment data)

**Retention:** Don't keep what you don't need. Set policies. Enforce them.

<!-- Talk track: Privacy is not optional and it's not someone else's problem. As an analytics manager, you are directly responsible for how your team collects, stores, and uses personal data. GDPR gives us four concepts you need to internalize. Lawful basis — you need a legal reason to process personal data. "We want to analyze it" is not automatically sufficient. Data minimization — collect only what you need for a specific purpose. I've seen teams logging every click, every scroll position, every mouse movement "just in case." That's a liability, not an asset. Right to erasure — if a user asks to be deleted, your pipeline needs to handle it. If your analytics warehouse can't delete a specific user's data, you have a compliance problem. And consent management — track what users agreed to and don't exceed that scope. Finally, classify your data into tiers and set retention policies. Don't keep data forever. It's a risk with no upside. -->

---

## Activity: Data Infrastructure One-Pager

**Time: 25 minutes** | Use the template provided

For your case context, write a one-page **"Our Next 6 Months of Data Infrastructure"** plan.

**Your one-pager must include:**
1. **Current state** — What exists today? What are the gaps and pain points?
2. **Target architecture** — What does the stack look like in 6 months? Map to the blueprint layers.
3. **Key tools** — What are you selecting for each layer and why?
4. **Implementation plan** — Phased: Month 1-2, Month 3-4, Month 5-6
5. **Budget estimate** — Monthly and annual costs
6. **Risks & dependencies** — What could go wrong? What do you depend on?

**Tip:** Refer back to the blueprint slide. Small context students: resist the urge to over-engineer. Large context students: focus on what's achievable in 6 months, not the 5-year vision.

<!-- Talk track: Time for hands-on work. Open the data infrastructure blueprint template. You have 25 minutes. I want you to write a one-page plan for your case context's data infrastructure over the next six months. This is a real deliverable — something you could hand to a VP of Engineering or a CTO and say "here's what we need, here's what it costs, here's the plan." Be specific about tools. Don't write "we need a warehouse" — write "we'll use BigQuery because it has a generous free tier and our team already knows SQL." Use the cost estimates from the slides as a starting point. Small context people: your one-pager should be simple. Three or four tools, under two thousand a month. Large context people: your challenge is scoping down to what's achievable in six months. Go. I'll circulate. -->

---

## Activity: RFP Scoring Matrix

**Time: 20 minutes** | Use the template provided

Pick **one tool category** for your case context:
- Warehouse (BigQuery vs. Snowflake vs. Databricks)
- BI / Visualization (Metabase vs. Preset vs. Looker)
- Experimentation (Statsig vs. Eppo vs. LaunchDarkly)
- Ingestion (Fivetran vs. Airbyte vs. Stitch)

**Your scoring matrix must include:**
1. **Requirements** — At least 8, prioritized as Must / Should / Nice
2. **Three real vendors** — Scored 1-5 on each criterion
3. **Weighted total** — Not all criteria are equal
4. **Total Cost of Ownership** — 3-year view per vendor
5. **Recommendation** — Which vendor and why?

**Tip:** You can use real pricing from vendor websites. Approximate is fine.

<!-- Talk track: Second activity. Keep your one-pager open — now pick one tool category from your infrastructure plan and do a real vendor evaluation. Pick a category where you have a genuine choice to make. If you're in the small context, maybe it's warehouse or BI tool. If you're in the medium context, maybe it's experimentation or event platform. If you're in the large context, maybe it's data catalog or ML platform. Use real vendors, real criteria, real-ish pricing. The point of this exercise is to practice the discipline of structured evaluation. It's incredibly tempting to just pick the tool you've heard of or the one your friend uses. The scoring matrix forces you to be rigorous. Twenty minutes. Go. -->

---

## Debrief

**Let's hear from the room:**

- What trade-offs did you make in your infrastructure plan?
- Where did build-vs-buy get hard? What made the decision ambiguous?
- What would IT push back on in your plan? What's the procurement risk?
- Did the scoring matrix change your initial instinct about which vendor to pick?

**Key insight:** The "right" stack depends on your constraints — team size, budget, timeline, regulatory environment. There is no universal answer. The framework is the answer.

<!-- Talk track: Let's come back together. I want to hear from a few people. First — what trade-offs did you make? Someone in the small context: what did you decide to skip, and did it feel uncomfortable? Good. That discomfort means you understand what you're giving up. Now — where did build-vs-buy get hard? Who found a case where the answer wasn't obvious? That's the real world. The framework helps, but it doesn't make the decision for you. Finally — look at your infrastructure plan through IT's eyes. What would they push back on? If you picked a tool without SOC 2, they'll push back. If you picked a tool that stores data outside the EU, they'll push back. If you can't answer these questions, you're not ready to start procurement. The scoring matrix is your tool for having that conversation with evidence, not opinions. -->

---

## Your Infrastructure Toolkit

After this block, you have:

- [x] **Cross-functional map** — Who you depend on and what they need from you
- [x] **The canonical blueprint** — Sources through visualization with governance overlay
- [x] **Build-vs-buy framework** — Four questions to cut through the noise
- [x] **RFP scoring matrix** — Structured vendor evaluation, not vibes
- [x] **Privacy & governance basics** — GDPR, data classification, retention
- [x] **A 6-month infrastructure plan** — Specific to your case context

These feed directly into your **Manager Portfolio** — the data infrastructure blueprint and vendor scoring matrix are portfolio deliverables.

<!-- Talk track: Let's take stock. You now have a practical toolkit for infrastructure decisions. You have a cross-functional map that documents your dependencies. You have the canonical blueprint that organizes any data stack. You have a build-vs-buy framework and a vendor scoring process. You have a privacy and governance foundation. And you have a six-month plan specific to your case context. Both the infrastructure blueprint and the vendor scoring matrix are deliverables in your final portfolio. Refine them this week using the feedback you got today. -->

---

## Transition to Block F

**Next: QBR Simulation (15:30–17:10)**

You're about to present your roadmap and narrative to a mock executive panel.

**Use the next 10 minutes to:**
1. Review your roadmap from Day 1 Block C
2. Incorporate your infrastructure plan from today
3. Prepare a 5-minute presentation: What are you building? Why? What does it cost?
4. Anticipate hard questions: "Why this vendor?" "What's the ROI?" "When do we see results?"

**The QBR format:** 5 min present, 5 min Q&A, 5 min peer feedback.

Think like an executive is listening. Because in Block F, they will be.

<!-- Talk track: Final block is coming up — the QBR simulation. This is where everything comes together. You're going to present your roadmap and narrative to a mock executive panel. Take the next ten minutes — before we start Block F — to prep. Pull up your roadmap from Day 1. Incorporate the infrastructure plan you just wrote. Think about the story you're telling: what are we building, why does it matter, what does it cost, and when will we see results. Anticipate the hard questions. If you recommend Snowflake, be ready for "why not BigQuery — it's cheaper." If you recommend building something in-house, be ready for "do we have the team for that?" Think like your audience. See you at 3:30. -->
