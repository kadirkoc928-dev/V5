import streamlit as st
import pandas as pd
from scanner import scan_ticker, get_all_tickers

st.set_page_config(page_title="TradeScanner V2", layout="wide")

st.title("📊 TradeScanner V2 - FULL MARKET SCANNER")

mode = st.selectbox("Modus", ["Top 50", "Top 200", "ALL STOCKS"])

if st.button("🚀 SCAN STARTEN"):

    if mode == "Top 50":
        tickers = get_all_tickers()[:50]
    elif mode == "Top 200":
        tickers = get_all_tickers()[:200]
    else:
        tickers = get_all_tickers()

    results = []

    progress = st.progress(0)

    for i, t in enumerate(tickers):
        res = scan_ticker(t)
        if res:
            results.append(res)

        progress.progress((i+1)/len(tickers))

    if results:
        df = pd.DataFrame(results)
        df = df.sort_values("Score", ascending=False)

        st.success(f"{len(df)} Signale gefunden")
        st.dataframe(df, use_container_width=True)
    else:
        st.error("Keine Treffer gefunden")
