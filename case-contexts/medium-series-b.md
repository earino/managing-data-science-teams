# MarketBridge: Modernizing Analytics at a Growing Two-Sided Marketplace

## Company Profile

MarketBridge is a Series B two-sided marketplace connecting homeowners with vetted local service professionals — plumbers, electricians, house cleaners, landscapers, and handypeople. Think of it as a Thumbtack-like platform with a stronger emphasis on provider quality and verified reviews. The company was founded five years ago, has raised $30M across three rounds, and employs approximately 150 people across product, engineering, operations, sales, marketing, and customer support.

The platform currently processes around 500,000 transactions per month across 12 metro areas in the United States. Revenue comes from a blended model: service professionals pay a monthly subscription for premium placement plus a percentage-based booking fee on completed jobs. MarketBridge is cash-flow negative but approaching breakeven in its most mature markets.

The company is in the middle of an ambitious expansion plan. Three new metropolitan markets are slated to launch this year — one domestic (Atlanta) and two in the European Union (Berlin and Amsterdam). The EU expansion introduces significant complexity around data privacy, residency requirements, and regulatory compliance that the existing data infrastructure was never designed to handle.

MarketBridge's board is pushing for a clear path to profitability. Every dollar of spending is under scrutiny, and the analytics function is expected to demonstrate direct business impact — not just produce dashboards, but actively drive decisions that improve unit economics across both sides of the marketplace.

## Current Data State

MarketBridge's data stack has the archaeological quality common to companies that grew fast without a long-term data strategy. Layers of tooling were added to solve immediate problems, and now the team is left with a partially connected patchwork.

**Event collection** runs through Segment, which was implemented two years ago by an engineer who has since left. The Segment setup is functional but under-maintained. There are approximately 340 tracked events, but an internal audit six months ago estimated that 30% are either redundant, misconfigured, or no longer relevant. Nobody has had time to clean it up. Segment feeds data into multiple destinations, not all of which are still actively used.

**Product analytics** lives in Mixpanel, which was adopted early in the company's life. Product managers rely on it for funnel analysis, retention reporting, and feature adoption tracking. However, trust in Mixpanel has eroded significantly. Numbers pulled from Mixpanel dashboards frequently conflict with numbers pulled via SQL from the PostgreSQL read replica. The discrepancies stem from differences in event filtering logic, user identity resolution, and time zone handling, but nobody has invested the time to reconcile them. The Mixpanel contract is up for renewal in six weeks, and the decision of whether to renew, renegotiate, or migrate is now on your plate.

**Ad-hoc SQL analysis** happens against a PostgreSQL read replica that was set up by the backend team. Analysts connect to it using a mix of DataGrip, DBeaver, and psql. There are no shared query conventions, no version-controlled SQL, and no documentation of table schemas or known data quirks.

**The warehouse layer** is BigQuery, fed by Fivetran connectors that pull from PostgreSQL, Stripe, Salesforce, and a handful of SaaS tools. The Fivetran setup works but is lightly monitored — breakages sometimes go unnoticed for days. A dbt project was started six months ago by your predecessor to build a transformation layer on top of BigQuery. It contains roughly 20 models, most of which are staging tables. The project was abandoned when your predecessor left after eight months. The models have not been run in weeks, and several are broken due to upstream schema changes.

**Supply-side data** is particularly fragmented. Service professional profiles, lead pipelines, and account management notes live in Salesforce, managed by the sales operations team. This data is nominally synced to BigQuery via Fivetran, but the Salesforce data model is complex and poorly documented. Joining supply-side Salesforce data with demand-side product data requires manual mapping that only one analyst (who has been at the company for three years) knows how to do reliably.

**The analyst team** consists of three analysts embedded in different parts of the organization: one supports Product, one supports Growth/Marketing, and one supports Operations. They were hired at different times, have different skill levels, and have developed their own workflows independently. There are no shared coding standards, no peer review process, no shared metric definitions, and no centralized knowledge base. Each analyst maintains their own collection of SQL queries and Google Sheets.

## Key Stakeholders

**Diane Osei, VP of Product.** Diane oversees a team of eight product managers and is the most vocal advocate for analytics modernization. She wants two things: self-serve dashboards that PMs can use without filing analyst requests, and a rigorous experiment platform that lets the team run A/B tests with proper statistical controls. She is frustrated that her PMs spend more time debating whether numbers are correct than acting on insights. She has political capital and is willing to spend it to support the analytics team, but she expects rapid, visible progress in return.

**Marco Reyes, Head of Growth.** Marco runs paid acquisition, SEO, content marketing, and partnerships. His primary data need is a reliable attribution model that can tell him the true cost of acquiring a customer (CAC) by channel and the lifetime value (LTV) of customers acquired through each channel. The current attribution setup is rudimentary — last-touch attribution via UTM parameters — and Marco knows it is inadequate for a marketplace where customer journeys are long and multi-touch. He also needs data to support the three new market launches, including baseline metrics and early performance tracking.

**Anya Petrov, Legal and Privacy Officer.** Anya was hired a year ago as MarketBridge began planning its EU expansion. She is responsible for GDPR compliance, consent management, and data privacy across all markets. A formal GDPR audit is scheduled for Q3, and Anya has flagged several gaps in the current data infrastructure: consent records are incomplete, data deletion requests are handled manually and inconsistently, and there is no clear inventory of where personal data flows through the stack. Anya's reviews currently add 2-3 weeks to any feature launch that involves new data collection, a delay that frustrates the product team. She is not opposed to moving faster, but she needs confidence that privacy controls are systematic rather than ad hoc.

**Raj Malhotra, CTO.** Raj is your direct manager. He is an experienced engineering leader who cares about data but is increasingly alarmed by the cost trajectory of the data stack. Data infrastructure costs have roughly doubled year-over-year, driven by growing Segment event volumes, Fivetran sync frequency, BigQuery compute costs, and the Mixpanel license. Raj wants you to rationalize the stack — eliminate redundancy, control costs, and build something maintainable. He is supportive but will push back hard on any proposal that adds net-new tooling without a clear plan to sunset something else.

**Christine Park, CFO.** Christine is focused on the path to profitability and needs financial reporting that integrates product and operational data. She wants to understand unit economics at the market level, the per-transaction margin by service category, and how product changes affect financial outcomes. Her team currently operates in a parallel universe of Excel models and NetSuite exports that are disconnected from the product data in BigQuery. Bridging this gap is a recurring request that has never been prioritized.

## Pain Points

- **Analysts as ticket-takers.** The three embedded analysts spend the majority of their time responding to ad-hoc data requests from stakeholders. They have no time for proactive analysis, deep dives, or infrastructure improvements. Morale is declining, and the most senior analyst has hinted at looking for other opportunities.
- **Metric definition chaos.** There are at least three different definitions of "active user" in use across the company. Monthly transaction volume is calculated differently by Product (who counts initiated bookings) and Finance (who counts completed, paid transactions). These discrepancies surface in board meetings and executive reviews, causing confusion and eroding trust in data across the organization.
- **Dashboard distrust.** PMs have largely stopped using Mixpanel dashboards because the numbers do not match what they get when they ask an analyst to run a SQL query. The analysts, in turn, do not trust each other's SQL because there are no shared definitions or reviewed models.
- **Privacy as a bottleneck.** Anya's privacy reviews are thorough but slow, and the process is not well-integrated into the product development lifecycle. Feature teams treat privacy review as a gate to clear at the end rather than a constraint to design around from the start. This leads to last-minute delays and adversarial dynamics between Product and Legal.
- **Disconnected supply-side data.** The marketplace's supply-side data (service professional profiles, earnings, response rates, availability) lives in Salesforce and is poorly integrated with product analytics. Understanding the health of both sides of the marketplace requires manual data stitching that is fragile and time-consuming. Key marketplace health metrics — like supply-demand balance by category and metro — are not reliably tracked.
- **Abandoned infrastructure.** The half-built dbt project and the poorly maintained Fivetran connectors represent a trust deficit. The team has been burned by infrastructure projects that were started and not finished. Any new initiative will face skepticism about whether it will actually be completed and maintained.

## Constraints

Your operating environment is shaped by several hard constraints:

- **Budget:** $25,000 per month for all data tooling, including existing commitments. The Mixpanel renewal decision alone could consume a significant portion of this budget if you re-sign at current rates.
- **Headcount:** There is a company-wide hiring freeze, with an exception carved out for the analytics team. You can hire two additional people, but the roles need to be justified and approved by the CTO. Choose wisely — these hires will define your team's capabilities for the next 12-18 months.
- **EU data residency:** The Berlin and Amsterdam market launches require that EU user data be stored and processed within the EU. The current data stack is entirely US-based. This constraint affects warehouse architecture, event collection, and every downstream tool that touches personal data.
- **Mixpanel decision timeline:** The Mixpanel contract renewal is due in six weeks. You need to decide whether to renew (and at what tier), migrate to an alternative, or consolidate product analytics into the warehouse. This decision has downstream implications for the product team's workflow, analyst tooling, and budget allocation.
- **dbt project resurrection.** The abandoned dbt project represents both a liability and an opportunity. The models that exist are a starting point, but they need to be audited, fixed, and extended. Walking away from dbt entirely would mean starting over with a different transformation approach and losing the work that was done.
- **Inherited team dynamics.** The three analysts you inherit were hired by someone who left. They may be uncertain about their future, skeptical of new leadership, or set in workflows that you will want to change. Building trust with this team is as important as building infrastructure.

## Your Role

You are the new Head of Analytics at MarketBridge, reporting to CTO Raj Malhotra. You are replacing someone who left after eight months — a fact that is not lost on anyone. The team, the stakeholders, and the executive leadership are all watching to see whether this time will be different.

You inherit a team of three analysts, a messy but partially functional data stack, a set of impatient stakeholders with legitimate needs, and a ticking clock on several decisions (Mixpanel renewal, EU expansion data architecture, GDPR audit preparation). You have the authority to make tooling decisions, hire two people, and set the strategic direction for analytics at the company. You do not have the luxury of a six-month planning phase.

Your challenge is to simultaneously keep the lights on (the analysts need to keep serving stakeholders), modernize the infrastructure (the dbt project, the warehouse, the metric definitions), navigate politically sensitive decisions (Mixpanel renewal, privacy process reform, supply-side data integration), and build a team culture that attracts and retains talent. The previous Head of Analytics burned out trying to do all of this at once. Your task is to figure out how to sequence and prioritize so that you do not meet the same fate.
