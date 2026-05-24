import streamlit as st
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

from scanner import scan_ticker, get_all_tickers


st.set_page_config(page_title="TradeScanner V2", layout="wide")

st.title("📊 TradeScanner V2 (Simple + Stable)")


# =========================
# SCAN BUTTON
# =========================
if st.button("🚀 START SCAN"):

    tickers = get_all_tickers()

    results = []
    progress = st.progress(0)
    status = st.empty()

    def run(t):
        return scan_ticker(t)

    with ThreadPoolExecutor(max_workers=10) as executor:

        futures = {executor.submit(run, t): t for t in tickers}

        for i, f in enumerate(as_completed(futures)):

            result = f.result()

            if result:
                results.append(result)

            progress.progress(i / len(tickers))
            status.text(f"Scanned: {i}/{len(tickers)} | Hits: {len(results)}")

    df = pd.DataFrame(results)

    if df.empty:
        st.warning("Keine Signale gefunden")
    else:
        df = df.sort_values("Score", ascending=False)

        st.success(f"{len(df)} Treffer gefunden")

        st.dataframe(df, use_container_width=True)
