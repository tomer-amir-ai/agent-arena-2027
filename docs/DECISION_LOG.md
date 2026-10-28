# Decision Log

Every product and technical decision in Agent Arena 2027, with the options considered and the reason. Newest decisions are added at the bottom. A decision that replaces an earlier one says so.

**Status:** ✅ Decided · 🟡 Proposed, waiting for confirmation

---

## Concept and league rules

### D-001 · The project is a league, and I compete in it ✅
**Date:** 2026-10-18
**Decision:** AI agent teams compete in a public league, and I take part with my own portfolio (human vs. agents).
**Why:** A league gives something to show every week and a clear, interesting question: which method wins, and can a human beat the agents.

### D-002 · The core question is "does the AI add value?" ✅
**Date:** 2026-10-18
**Decision:** Every agent team gets a "dumb twin": plain code that applies the same method with no language model. The twin is the control group.
**Options considered:** Agents compete only against each other and the S&P 500.
**Why:** "AI investing agents" is a crowded idea. Comparing each team with its own twin turns the project into an experiment and answers a question every company adding AI faces. If the twin wins, that is a valid result.

### D-003 · Active league instead of frozen portfolios ✅ (replaces the original frozen-portfolio decision)
**Date:** 2026-10-18
**Decision:** Competitors buy and sell throughout the season. All trading is simulated (paper trading).
**Options considered:** 10 stocks bought on Dec 31 and held all year with no sales.
**Why:** An active league gives more events to follow, more for the commentator to cover, and lets agents learn over time.

### D-004 · $10,000 simulated per competitor, in US dollars ✅
**Date:** 2026-10-18
**Why:** Simple for any viewer to follow. Dollars, not shekels, because the stocks and the benchmark are in dollars and a currency conversion would add noise unrelated to any method.

### D-005 · Season starts Dec 31, 2026, with quarterly standings ✅
**Date:** 2026-10-18
**Decision:** Dec 31, 2026 is the official start, when everyone resets to $10,000. The season runs through 2027, with standings at the end of each quarter. The date does not move.

### D-006 · US stocks only, benchmark S&P 500 ✅
**Date:** 2026-10-18

### D-007 · Competitor lineup ✅
**Date:** 2026-10-18
**Decision:**
- **Agent teams (AI):** SMA-150, Fundamental, Technical, Trader.
- **Twins (code only):** one per agent team.
- **Bots (code only):** S&P 500 bought once; S&P 500 bought monthly; Magnificent 7 in equal weight, bought once.
- **Human:** me.
**Options considered:** 9 managers, including a separate short-term trader, a trade seeker, and a short seller.
**Why:** Bots cost nothing to run and act as the "bosses" every agent team must beat.

### D-008 · Merge the short-term trader and the trade seeker into one Trader ✅
**Date:** 2026-10-18
**Decision:** One Trader agent team that holds positions for days to weeks, on daily data.
**Why:** The two overlapped. Very short trades need intraday data and many more AI calls, which the free tiers don't support.

### D-009 · Remove the short-selling agent ✅
**Date:** 2026-10-18
**Why:** Short selling needs its own rules (unlimited loss, borrowing costs, scoring against long-only teams). Cut to keep the scope manageable.

### D-010 · Magnificent 7 bot: equal weight, bought once, no rebalancing ✅
**Date:** 2026-10-18

### D-011 · SMA-150 method rules ✅
**Date:** 2026-10-18
**Decision:** Simple 150-day moving average on adjusted close. Entry when the price is above the average or touching it. No slope condition. This is my interpretation of the method, not an official version.

---

## Features and scope

### D-012 · Weekly AI commentator ✅
**Date:** 2026-10-18
**Decision:** An agent writes a weekly recap in a sports-commentator style.
**Why:** Turns numbers into a story people want to read. Costs one or two AI calls a week. It describes what happened and never recommends stocks.

### D-013 · Behind-the-scenes page for the agents ✅
**Date:** 2026-10-18
**Decision:** A dashboard page showing AI calls, tokens used, the share of agent claims backed by data, and how often the critic rejected a claim.
**Why:** Measuring AI systems (evals and observability) is the skill this project should show.

### D-014 · No external users in version 1 ✅
**Date:** 2026-10-18
**Decision:** I am user number one and use the product daily. Interviews with investors stay an option.

### D-015 · Removed: weekly predictions ✅
**Date:** 2026-10-18

### D-016 · Go/no-go checkpoint at the end of week 2 ✅
**Date:** 2026-10-18
**Decision:** At the end of week 2, decide honestly whether to continue: am I enjoying it, am I learning?

### D-017 · Agent teams learn weekly, within a locked philosophy ✅
**Date:** 2026-10-28
**Decision:** Once a week each agent team writes a "lessons notebook" from its results. The philosophy is locked in code (the SMA-150 team can never drop the average). Every notebook version is kept, like patch notes.
**Options considered:** Monthly (recommended, 12 updates a season) or quarterly (too few updates to see a trend).
**Why:** Faster feedback and more learning moments to show during the season.
**Known risk:** One week of market moves is mostly noise, so a team may "learn" from luck. Mitigations: every lesson must cite data, and the twin, which never learns, shows whether learning helps at all.

### D-018 · Preseason before the official start ✅
**Date:** 2026-10-28
**Decision:** Bots and twins start running in November, once the data is ready. Each agent team joins as soon as it is ready. Everyone resets on Dec 31.
**Why:** Something live to show long before the season starts, and time to test the system before results count.

---

## Architecture

### D-019 · Code runs daily, agents wake up on triggers ✅
**Date:** 2026-10-18
**Decision:** Indicators, filtering, bots and twins run as plain code every day. Agent teams run only when a trigger fires (for example, a touch of the 150-day average) plus a weekly review.
**Options considered:** Run every agent team daily.
**Why:** A planning estimate put one agent-team run at about 75K tokens, and the free tier of one LLM provider allows about 200K tokens a day. Running every team daily does not fit. The estimate will be replaced by a real measurement in week 2.

### D-020 · Two layers: live experience, league on daily closes ✅
**Date:** 2026-10-22
**Decision:**
- **Live layer:** charts and touch alerts in real time.
- **League engine:** trades, scoring and backtests use daily closing prices. A signal at the close executes at the next day's open.
**Why:** Every competitor sees the same price at the same moment, there is no look-ahead, results can be reproduced, and daily data is free.

### D-021 · A "touch" is intraday, in real time, from either direction ✅
**Date:** 2026-10-22, updated 2026-10-26
**Decision:** An alert fires the moment the live price reaches the 150-day average, at any time during trading, whether the price comes from above or from below. Alerts are for information only, not orders.
**Note:** The touch price for each session can be computed once before the open: it is the average of the last 149 closes. Live scanning then becomes a simple price comparison.

### D-022 · Alerts in extended hours, with a separate label ✅
**Date:** 2026-10-28
**Decision:** Touch alerts also fire in pre-market and after-hours trading, labeled as extended-hours and less reliable. The 150-day average itself always uses regular-session closes.
**Options considered:** Regular hours only.
**Why:** Earnings usually come out outside regular hours, and big moves happen then. Thin trading can cause false alerts, so the label makes the difference clear. The data source still has to be checked for extended-hours coverage.

### D-023 · GitHub Actions only for short scheduled jobs ✅
**Date:** 2026-10-22
**Decision:** GitHub Actions runs daily data jobs and dashboard updates, not the live monitor.
**Why:** GitHub's terms limit Actions to developing, testing, deploying and publishing the project, and a job can run for at most 6 hours. A live market monitor needs to run through the whole 6.5-hour session.

### D-024 · The live monitor runs on a free cloud server, not my computer ✅
**Date:** 2026-10-28
**Requirements:** Free, no ongoing maintenance burden on me, and able to handle the full load (live portfolio alerts plus the market scanner).
**Decision:** Google Cloud's free e2-micro server, set up carefully with a $1 budget alert. Oracle Cloud's free tier as the backup.
**Options considered:** My personal computer; GitHub Actions; Oracle Cloud.
**Why:** Oracle may reclaim free servers that look idle, and a lightweight monitor would look idle. GitHub Actions terms and its 6-hour job limit rule it out. Both cloud options need a credit card for verification. Setup and a load test happen in week 3.

---

## Data

### D-025 · First test list: 10 stocks plus SPY ✅
**Date:** 2026-10-22
**Decision:** NVDA, AAPL, MSFT, PLTR, TSLA, AMZN, JPM, HOOD, LLY, SHOP, plus SPY as the benchmark.
**Why:** Stocks I follow, across several sectors, so I can spot wrong numbers.

### D-026 · yfinance only for the first run ✅
**Date:** 2026-10-26
**Decision:** The first run uses yfinance, an unofficial library that reads Yahoo data. The permanent source is still open.
**Why:** No API key needed, enough for a one-off check. Not reliable enough for the league itself.

---

## Results

### R-001 · Our SMA-150 matches TradingView
**Date:** 2026-10-28
The first run computed the 150-day average for 11 symbols. NVDA and AAPL were checked against TradingView and matched. Stocks without dividends show the same value in both average columns; stocks with dividends (JPM, MSFT, SPY) show a small difference, as expected.

---

## Open questions

- Permanent price source (Alpaca is the lead candidate).
- How each agent team ranks and picks stocks, and sector limits.
- League scoring: return only, or risk-adjusted as well.
- Backtesting the twins and bots on historical data.
- Alert channel (email, Telegram, other).
- Where the dashboard is hosted.
- Language of reports and commentary.
- Final project name.
