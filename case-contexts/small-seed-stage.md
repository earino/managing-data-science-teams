# DataPulse: Building Analytics from Zero at a Seed-Stage Fitness App

## Company Profile

DataPulse is a seed-stage B2C fitness app that combines AI-generated workout plans with social accountability features. The company was founded 18 months ago by two former Peloton product managers who saw an opportunity in the "casual fitness" segment — people who want to stay active but find existing apps intimidating or overly structured. The team has grown to 12 employees: the two co-founders (CEO and CTO), a Head of Product, one backend engineer, two mobile developers, a designer, three customer support reps, and a part-time marketing contractor.

DataPulse closed a $2M seed round six months ago led by a mid-tier consumer VC fund. The app currently has approximately 50,000 monthly active users and is growing at roughly 15% month-over-month, driven primarily by organic TikTok content and word of mouth. Revenue comes from a $9.99/month premium subscription with a 3.2% conversion rate from free users. The founders believe they are 4-6 months away from needing to raise a Series A, and every conversation with potential investors circles back to the same questions: What does your retention curve look like? What is your LTV:CAC ratio? How do you know your product has real engagement and not just download curiosity?

The founders cannot answer these questions with confidence. That is why they are hiring you.

## Current Data State

The data infrastructure at DataPulse was never designed — it accumulated. The React Native app sends events to Firebase Analytics, but the implementation was done piecemeal by whichever mobile developer happened to be building a feature at the time. There is no event taxonomy document. One developer uses camelCase event names (`workoutStarted`), the other uses snake_case (`workout_completed`). Some events carry rich properties; others carry none. There are also scattered `console.log` statements throughout the codebase that were added during debugging sessions and never removed, occasionally producing misleading signals in the Firebase console.

Six months ago, the Head of Product signed up for Amplitude's free tier to build basic funnel analyses. She built a handful of funnels and a retention chart, but quickly discovered that the numbers did not match what the CEO was pulling from the production PostgreSQL database using direct SQL queries. The discrepancy eroded trust in both systems. Today, nobody on the team fully trusts any single number, and most product decisions are made based on qualitative user feedback from the support team or gut instinct from the founders.

The production PostgreSQL database is the closest thing DataPulse has to a source of truth. It contains user accounts, subscription records, workout completion logs, and social interaction data. The CEO queries it directly using a SQL client, usually running queries during off-peak hours to avoid performance issues. However, on at least two occasions, a long-running analytical query coincided with a traffic spike and caused noticeable latency for end users. The backend engineer has raised this as a serious concern but has not had time to set up a read replica.

There is no data warehouse. There is no ETL pipeline. There is no documentation of what events mean, how metrics should be calculated, or what "active user" even means in the context of DataPulse.

## Key Stakeholders

**Mira Chen, CEO and Co-founder.** Mira is laser-focused on the Series A fundraise. She needs a clean, credible set of growth metrics — retention cohorts, LTV projections, and engagement depth — that she can present to investors without hedging. She is technically competent (she can write basic SQL) but does not have time to maintain dashboards or investigate data discrepancies. She is your direct manager and your strongest internal sponsor, but her patience has limits. If she does not see tangible results within your first quarter, she will question whether the hire was premature.

**Jake Oduya, Head of Product.** Jake wants to move from opinion-driven to data-driven product development. He wants to understand which features drive retention, where users drop off in onboarding, and whether the social features are actually working. He has tried to self-serve with Amplitude but found the data unreliable and the tool limiting. He will be your most frequent internal customer and has strong opinions about what metrics matter.

**Sara Kim, Backend Engineer.** Sara is the sole backend engineer and is already stretched thin across API development, infrastructure, and on-call responsibilities. She is protective of the production database and rightfully nervous about anyone running unoptimized queries against it. She is a potential ally — she cares about doing things right — but she has no bandwidth to help with data infrastructure projects. Any solution you propose must not add to her workload.

**Luis Herrera and Priya Nair, Mobile Developers.** Luis and Priya built the app's event tracking independently and inconsistently. They are aware that the event taxonomy is messy but view cleaning it up as low-priority compared to shipping features. They will need to implement any new tracking instrumentation you design, so their buy-in is critical. Neither has experience with structured analytics engineering or event design.

## Pain Points

The core problem at DataPulse is not a lack of data — it is a lack of trust, structure, and literacy around data. Specific pain points include:

- **No trusted metrics.** The CEO, Head of Product, and Amplitude all produce different numbers for the same questions. Board meetings involve awkward hedging ("we think retention is around 30-35% at day 30, but we're still nailing down the exact number").
- **A/B testing by intuition.** The team has run several "experiments" on features like push notification timing and onboarding flows, but none had proper control groups, sample size calculations, or statistical analysis. Decisions were made based on whether a metric "looked better" in a two-day window.
- **Investor-readiness gap.** The Series A fundraise depends on presenting credible unit economics and engagement data. Right now, DataPulse cannot produce a reliable retention curve, a defensible LTV estimate, or a clear picture of CAC by channel.
- **Event taxonomy chaos.** The mobile event data is inconsistent in naming, property structure, and coverage. Some critical user actions (like completing the onboarding survey) are not tracked at all. Others are tracked with different names on iOS and Android.
- **Production database risk.** The founder's habit of running analytical queries against the production PostgreSQL database is a ticking time bomb. One bad query during peak hours could cause a user-facing outage.

## Constraints

You are operating under significant resource constraints that will shape every decision you make:

- **Budget:** $5,000 per month is the total budget allocated for data tools and infrastructure. This must cover any new platforms, warehouse hosting, ETL tooling, and visualization software. There is no room for enterprise-grade solutions.
- **Headcount:** You are the first and only data hire. There is no budget approved for a second data person in the near term. Everything you build must be maintainable by one person.
- **Time pressure:** You have approximately 90 days to demonstrate enough value to justify your continued employment and, ideally, to produce the metrics the CEO needs for the fundraise. Quick wins matter as much as long-term architecture.
- **Data literacy:** Nobody on the team has worked with a data professional before. Concepts like event taxonomies, dimensional modeling, statistical significance, and metric definitions will need to be introduced gently and with context. You will need to be a teacher as much as a builder.
- **Technical debt:** Any solution must work with the existing React Native app, Firebase setup, and PostgreSQL database. A rip-and-replace approach is not feasible given the team's bandwidth and the fundraise timeline.

## Your Role

You are the first analytics hire at DataPulse, reporting directly to CEO Mira Chen. Your title is intentionally broad — "Head of Data" — which reflects both the ambiguity of the role and the expectation that you will define it yourself. In practice, you are simultaneously an analytics engineer, a product analyst, a data engineer, and a data strategist.

Your immediate mandate is to bring order to the chaos: establish a single source of truth for key metrics, give the product team reliable data for decision-making, and produce the investor-grade analytics the CEO needs for the Series A process. Your longer-term challenge is to build a data foundation that can scale with the company — one that will not need to be torn down and rebuilt when DataPulse reaches 500K users and hires a real data team.

You must establish credibility quickly. The team has never had a data person before and is not entirely sure they need one. If your first month is spent building infrastructure nobody can see, you will lose stakeholder trust before you have a chance to deliver value. Conversely, if you only produce quick-and-dirty analyses without fixing the underlying data problems, you will be stuck in a cycle of one-off requests and unreliable numbers indefinitely. Balancing these tensions — speed versus rigor, visible impact versus foundational work — is the central challenge of your first 90 days.
