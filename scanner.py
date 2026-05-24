import yfinance as yf
import pandas as pd
import ta


# =========================
# TICKER LISTE
# =========================
def get_all_tickers():

    SP500 = ["AAPL","MSFT","NVDA","AMZN","META","TSLA","GOOGL","GOOG"]
    NASDAQ100 = ["AAPL","NVDA","MSFT","AMZN","META","TSLA","AMD","INTC"]
    DAX40 = ["SAP.DE","SIE.DE","BMW.DE","ALV.DE","BAS.DE"]

    all_tickers = list(set(SP500 + NASDAQ100 + DAX40))
    return all_tickers


# =========================
# INDICATORS
# =========================
def add_indicators(df):

    df["SMA20"] = ta.trend.sma_indicator(df["Close"], window=20)
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14)
    df["ADX"] = ta.trend.adx(df["High"], df["Low"], df["Close"], window=14)

    df["MACD"] = ta.trend.macd(df["Close"])
    df["MACD_SIGNAL"] = ta.trend.macd_signal(df["Close"])

    df["ATR"] = ta.volatility.average_true_range(
        df["High"], df["Low"], df["Close"], window=14
    )

    df["VOL_SMA"] = df["Volume"].rolling(20).mean()
    df["VOL_RATIO"] = df["Volume"] / df["VOL_SMA"]

    return df


# =========================
# SWING SCORE (0-100)
# =========================
def calculate_score(row):

    score = 0

    # Trend (SMA)
    if row["Close"] > row["SMA20"]:
        score += 20

    # RSI (neutral Zone = gut)
    if 45 <= row["RSI"] <= 65:
        score += 20
    elif 40 <= row["RSI"] <= 70:
        score += 10

    # ADX Trend Stärke
    if row["ADX"] > 30:
        score += 25
    elif row["ADX"] > 20:
        score += 15

    # Volume
    if row["VOL_RATIO"] > 1.5:
        score += 15
    elif row["VOL_RATIO"] > 1.2:
        score += 10

    # MACD Trend
    if row["MACD"] > row["MACD_SIGNAL"]:
        score += 20

    return min(score, 100)


# =========================
# SCAN TICKER
# =========================
def scan_ticker(ticker):

    try:
        df = yf.Ticker(ticker).history(period="6mo", interval="1d")

        if df.empty or len(df) < 30:
            return None

        df = add_indicators(df)
        latest = df.iloc[-1]

        score = calculate_score(latest)

        if score < 60:   # FILTER gegen Noise
            return None

        price = latest["Close"]
        atr_percent = (latest["ATR"] / price) * 100

        return {
            "Ticker": ticker,
            "Price": round(price, 2),
            "Score": score,
            "RSI": round(latest["RSI"], 1),
            "ADX": round(latest["ADX"], 1),
            "Vol Ratio": round(latest["VOL_RATIO"], 2),
            "ATR%": round(atr_percent, 2),
            "SMA20": "Above" if price > latest["SMA20"] else "Below",
            "MACD": "Bullish" if latest["MACD"] > latest["MACD_SIGNAL"] else "Bearish",
        }

    except:
        return None
