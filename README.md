# Agent Arena 2027

**A public league where AI agent teams with different investing philosophies compete against simple rule-based twins, index bots, and a human.**

> ⚠️ **Disclaimer:** This is a research and education project. All portfolios are simulated (paper trading) and no real money is involved. Nothing here is investment advice or a recommendation to buy or sell any security. The author is not a licensed investment advisor.

---

## Status

🚧 **Planning phase (October 2026).** No code yet. The official season starts on **December 31, 2026**.

## The question

Does an AI agent layer actually add value over a simple rule-based formula?

To test this, every AI agent team has a **"dumb twin"**: plain code that applies the same method with no language model at all. If the agents can't beat their own twin, the AI isn't earning its place.

## How the league works

- Every competitor starts with **$10,000** in simulated cash.
- US stocks only. The benchmark is the **S&P 500**.
- Competitors buy and sell throughout 2027, with **quarterly standings**.
- A public dashboard shows the live leaderboard, portfolios, agent debate transcripts, and a weekly AI commentator recap.

## Competitors (planned)

| Type | Competitor | Uses AI? |
|---|---|---|
| Agent team | SMA-150 manager (my interpretation of a 150-day moving average method) | Yes |
| Agent team | Fundamental manager | Yes |
| Agent team | Technical manager | Yes |
| Agent team | Trader (holds positions for days to weeks) | Yes |
| Twin | One rule-based twin per agent team | No |
| Bot | S&P 500, bought once | No |
| Bot | S&P 500, bought monthly | No |
| Bot | Magnificent 7, equal weight, bought once | No |
| Human | Me | Only my own brain |

Each agent team includes analysts, a bull-vs-bear debate, a critic that checks every claim is backed by data, and a manager that makes the final call.

## Design principles

- **Code first.** Data, indicators, filtering, scoring, and backtesting are deterministic code. Language models are used only for judgment.
- **Every claim is backed by data.** A critic agent checks, and the accuracy rate is published.
- **No look-ahead.** Signals use the close; simulated trades execute at the next day's open.
- **$0 budget.** Daily runs on GitHub Actions and free LLM tiers. Agents wake up on triggers plus a weekly review, not continuously.
- **Honest about luck.** One year with a handful of competitors is a small sample. A win in 2027 may be luck, and the dashboard says so.

## Roadmap

- [ ] Week 0: Product decisions, PRD, Decision Log
- [ ] Week 1: Price data and database
- [ ] Week 2: SMA-150 team, its twin, and the bots
- [ ] Week 3: Critic agent, daily monitoring, and alerts
- [ ] Week 4: Dashboard, leaderboard, and the weekly commentator
- [ ] Week 5: Deployment and v1.0
- [ ] December 31, 2026: Season starts

## License

MIT. See [LICENSE](LICENSE).
