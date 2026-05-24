import streamlit as st
import pandas as pd
from scanner import scan_ticker, get_market_regime

st.set_page_config(page_title="TradeScanner V2", layout="wide")

st.title("📊 TradeScanner V2")

tickers_input = st.text_input("Tickers (kommagetrennt)", "AAPL,TSLA,NVDA")
tickers = [t.strip().upper() for t in tickers_input.split(",")]

if st.button("🚀 SCAN STARTEN"):

    regime = get_market_regime()

    if regime != "BULL":
        st.warning("⚠️ Markt ist NICHT bullish → weniger gute Chancen")

    results = []

    with st.spinner("Scanne Aktien..."):
        for t in tickers:
            res = scan_ticker(t)
            if res:
                results.append(res)

    if len(results) == 0:
        st.error("Keine Signale gefunden")
    else:
        df = pd.DataFrame(results)
        df = df.sort_values("Score", ascending=False)

        st.success(f"{len(df)} Signale gefunden")
        st.dataframe(df, use_container_width=True)
