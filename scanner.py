import yfinance as yf
from indicators import add_indicators

# MARKET REGIME
def get_market_regime():
    spy = yf.Ticker("SPY").history(period="6mo")

    spy["SMA200"] = spy["Close"].rolling(200).mean()
    spy["SMA50"] = spy["Close"].rolling(50).mean()

    last = spy.iloc[-1]

    if last["Close"] > last["SMA200"] and last["SMA50"] > last["SMA200"]:
        return "BULL"
    return "BEAR"


# FILTER LOGIC
def filter_signal(row):
    score = 0

    if row["VOL_RATIO"] > 1.3:
        score += 1
    if row["RSI"] > 45:
        score += 1
    if row["ADX"] > 20:
        score += 1
    if row["MACD"] > row["MACD_SIGNAL"]:
        score += 1
    if row["Close"] > row["SMA20"]:
        score += 1

    return score >= 3


# SWING SCORE
def swing_score(row):
    score = 0

    if row["Close"] > row["SMA20"]:
        score += 10

    if row["SMA20"] > row["SMA50"]:
        score += 10

    # RSI ZONE
    if 45 <= row["RSI"] <= 70:
        score += 20

    if row["ADX"] > 25:
        score += 20

    if row["VOL_RATIO"] > 1.5:
        score += 20

    if row["MACD"] > row["MACD_SIGNAL"]:
        score += 20

    return min(100, score)


# SCAN SINGLE STOCK
def scan_ticker(ticker):
    try:
        df = yf.Ticker(ticker).history(period="6mo")

        if df.empty:
            return None

        df = add_indicators(df)
        latest = df.iloc[-1]

        if not filter_signal(latest):
            return None

        score = swing_score(latest)

        return {
            "Ticker": ticker,
            "Price": round(latest["Close"], 2),
            "Score": score,
            "RSI": round(latest["RSI"], 1),
            "ADX": round(latest["ADX"], 1),
            "Volume Ratio": round(latest["VOL_RATIO"], 2)
        }

    except Exception as e:
        print(f"Error {ticker}: {e}")
        return None
