"""
First run: check our SMA-150 numbers against TradingView.

No AI here. The script downloads daily prices, computes the 150-day
simple moving average (SMA-150) for each stock, and writes a table to
the GitHub Actions run summary.

Research and education only. Not investment advice.
"""

import os
import sys

import yfinance as yf

# The stocks to check. SPY (the S&P 500 ETF) is the league benchmark.
TICKERS = ["NVDA", "AAPL", "MSFT", "PLTR", "TSLA", "AMZN",
           "JPM", "HOOD", "LLY", "SHOP", "SPY"]

WINDOW = 150  # number of trading days in the moving average


def analyze(ticker, close, adj_close):
    """Return one table row for a single stock."""
    close = close.dropna()
    adj_close = adj_close.dropna()

    if len(close) < WINDOW:
        return f"| {ticker} | not enough data ({len(close)} days) | | | | | | |"

    last_date = close.index[-1].date()
    price = close.iloc[-1]

    # SMA-150 on the regular close, the way TradingView draws it by default.
    sma = close.iloc[-WINDOW:].mean()

    # SMA-150 on the close adjusted for dividends too (our league's rule).
    sma_adj = adj_close.iloc[-WINDOW:].mean()

    distance = (price / sma - 1) * 100
    position = "Above" if price > sma else "Below" if price < sma else "At"

    # Touch price for the next session: tomorrow's SMA is the average of the
    # last 149 closes plus tomorrow's price. The price touches the SMA when
    # it equals that average, which works out to the mean of the last 149 closes.
    touch_next = close.iloc[-(WINDOW - 1):].mean()

    return (f"| {ticker} | {last_date} | {price:,.2f} | {sma:,.2f} | "
            f"{sma_adj:,.2f} | {distance:+.1f}% | {position} | {touch_next:,.2f} |")


def main():
    data = yf.download(TICKERS, period="1y", interval="1d",
                       auto_adjust=False, progress=False)
    if data.empty:
        sys.exit("No data came back from the price source.")

    lines = [
        "## SMA-150 check",
        "",
        "| Stock | Data date | Close | SMA-150 | SMA-150 (dividend-adjusted) "
        "| Distance | Position | Touch price next session |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for ticker in TICKERS:
        lines.append(analyze(ticker, data["Close"][ticker],
                             data["Adj Close"][ticker]))

    lines += [
        "",
        "Compare the SMA-150 column with TradingView (daily chart, SMA, length 150).",
        "",
        "_Research and education only. Not investment advice._",
    ]
    report = "\n".join(lines)
    print(report)

    # On GitHub Actions, also show the table on the run's summary page.
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(report + "\n")


if __name__ == "__main__":
    main()
