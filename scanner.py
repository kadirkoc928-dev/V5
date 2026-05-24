import yfinance as yf
import pandas as pd
import ta


# =========================
# TICKER LISTE
# =========================
def get_all_tickers():

    # =========================
    # S&P 500
    # =========================
    SP500 = [
        "A","AAL","AAPL","ABBV","ABNB","ABT","ACGL","ACN","ADBE","ADI","ADM","ADP","ADSK","AEE","AEP","AES",
        "AFL","AIG","AIZ","AJG","AKAM","ALB","ALGN","ALK","ALL","ALLE","AMAT","AMCR","AMD","AME","AMGN",
        "AMP","AMT","AMZN","ANET","ANSS","AON","AOS","APA","APD","APH","APTV","ARE","ATO","AVB","AVGO",
        "AVY","AWK","AXP","AZO","BA","BAC","BALL","BAX","BBWI","BBY","BDX","BEN","BF.B","BG","BIIB","BIO",
        "BK","BKNG","BKR","BLDR","BLK","BMY","BR","BRK.B","BRO","BSX","BWA","BXP","C","CAG","CAH","CARR",
        "CAT","CB","CBOE","CBRE","CCI","CCL","CDNS","CDW","CE","CEG","CF","CFG","CHD","CHRW","CHTR","CI",
        "CINF","CL","CLX","CMA","CMCSA","CME","CMG","CMI","CMS","CNC","CNP","COF","COO","COP","COR","COST",
        "CPAY","CPB","CPRT","CPT","CRL","CRM","CSCO","CSGP","CSX","CTAS","CTLT","CTRA","CTSH","CTVA","CVS",
        "CVX","CZR","D","DAL","DD","DE","DFS","DG","DGX","DHI","DHR","DIS","DLR","DLTR","DOV","DOW","DPZ",
        "DRI","DTE","DUK","DVA","DVN","DXCM","EA","EBAY","ECL","ED","EFX","EIX","EL","ELV","EMN","EMR",
        "ENPH","EOG","EPAM","EQIX","EQR","EQT","ES","ESS","ETN","ETR","ETSY","EVRG","EW","EXC","EXPD",
        "EXPE","EXR","F","FANG","FAST","FCX","FDS","FDX","FE","FFIV","FICO","FIS","FITB","FMC","FOX",
        "FOXA","FRT","FSLR","FTNT","FTV","GD","GE","GEHC","GEN","GILD","GIS","GL","GLW","GM","GNRC",
        "GOOG","GOOGL","GPC","GPN","GRMN","GS","GWW","HAL","HAS","HBAN","HCA","HD","HES","HIG","HII",
        "HLT","HOLX","HON","HPE","HPQ","HRL","HSIC","HST","HSY","HUBB","HUM","HWM","IBM","ICE","IDXX",
        "IEX","IFF","ILMN","INCY","INTC","INTU","INVH","IP","IPG","IQV","IR","IRM","ISRG","IT","ITW",
        "IVZ","J","JBHT","JBL","JCI","JKHY","JNJ","JNPR","JPM","K","KDP","KEY","KEYS","KHC","KIM",
        "KLAC","KMB","KMI","KMX","KO","KR","KVUE","L","LDOS","LEN","LH","LHX","LIN","LKQ","LLY","LMT",
        "LNC","LNT","LOW","LRCX","LULU","LUV","LVS","LW","LYB","LYV","MA","MAA","MAR","MAS","MCD",
        "MCHP","MCK","MCO","MDLZ","MDT","MET","META","MGM","MHK","MKC","MLM","MMC","MMM","MNST","MO",
        "MOH","MOS","MPC","MPWR","MRK","MRNA","MRO","MS","MSCI","MSFT","MSI","MTB","MTCH","MTD","MU",
        "NCLH","NDAQ","NDSN","NEE","NEM","NFLX","NI","NKE","NOC","NOW","NRG","NSC","NTAP","NTRS",
        "NUE","NVDA","NVR","NWL","NWS","NWSA","NXPI","O","ODFL","OKE","OMC","ON","ORCL","ORLY",
        "OTIS","OXY","PANW","PARA","PAYC","PAYX","PCAR","PCG","PEG","PEP","PFE","PFG","PG","PGR",
        "PH","PHM","PKG","PLD","PM","PNC","PNR","PNW","PODD","POOL","PPG","PPL","PRU","PSA","PSX",
        "PTC","PWR","PYPL","QCOM","QRVO","RCL","REG","REGN","RF","RHI","RJF","RL","RMD","ROK",
        "ROL","ROP","ROST","RSG","RTX","RVTY","SBAC","SBUX","SCHW","SHW","SJM","SLB","SMCI","SNA",
        "SNPS","SO","SPG","SPGI","SRE","STE","STLD","STT","STX","STZ","SWK","SWKS","SYF","SYK",
        "SYY","T","TAP","TDG","TDY","TECH","TEL","TER","TFC","TFX","TGT","TJX","TMO","TMUS","TPR",
        "TRGP","TRMB","TROW","TRV","TSCO","TSLA","TSN","TT","TTWO","TXN","TXT","TYL","UA","UAL",
        "UBER","UDR","UHS","ULTA","UNH","UNP","UPS","URI","USB","V","VFC","VICI","VLO","VLTO",
        "VMC","VRSK","VRSN","VRTX","VTR","VTRS","VZ","WAB","WAT","WBA","WBD","WDC","WEC","WELL",
        "WFC","WHR","WM","WMB","WMT","WRB","WST","WTW","WY","WYNN","XEL","XOM","XRAY","XYL",
        "YUM","ZBH","ZBRA","ZION","ZTS"
    ]

    # =========================
    # NASDAQ 100
    # =========================
    NASDAQ100 = [
        "AAPL","ABNB","ADBE","ADI","ADP","ADSK","AEP","AMAT","AMD","AMGN","AMZN","ANSS","ASML","AVGO",
        "AZN","BIIB","BKNG","BKR","CDNS","CDW","CEG","CHTR","CMCSA","COST","CPRT","CRWD","CSCO","CSGP",
        "CSX","CTAS","CTSH","DASH","DDOG","DLTR","DXCM","EA","EBAY","EXC","FANG","FAST","FTNT","GEHC",
        "GFS","GILD","GOOG","GOOGL","HON","IDXX","ILMN","INTC","INTU","ISRG","JD","KDP","KHC","KLAC",
        "LRCX","LULU","MAR","MCHP","MDB","MDLZ","MELI","META","MNST","MRNA","MRVL","MSFT","MU","NFLX",
        "NVDA","NXPI","ODFL","ON","ORLY","PANW","PAYX","PCAR","PDD","PEP","PYPL","QCOM","REGN","ROP",
        "ROST","SBUX","SWKS","TEAM","TMUS","TSLA","TXN","VRSK","VRTX","WBA","WBD","WDAY","XEL","ZS"
    ]

    # =========================
    # RUSSELL (gekürzt + stabil)
    # =========================
    RUSSELL = [
        "AAON","AAN","AAWW","ABCB","ABG","ABM","ABR","ACAD","ACCD","ACCO","ACEL","ACHC","ACIW",
        "ACLS","ACMR","ACRE","ACT","ACVA","ADMA","ADNT","ADUS","AEIS","AEO","AGIO","AGM","AGNC",
        "AGX","AHCO","AHH","AIRS","AIT","AIZ"
    ]

    # =========================
    # DAX 40
    # =========================
    DAX40 = [
        "ADS.DE","AIR.DE","ALV.DE","BAS.DE","BAYN.DE","BMW.DE","CON.DE","DTE.DE","DBK.DE",
        "SAP.DE","SIE.DE","VOW3.DE","IFX.DE","RWE.DE"
    ]

    # =========================
    # CLEAN + UNIQUE
    # =========================
    all_tickers = list(set(SP500 + NASDAQ100 + RUSSELL + DAX40))

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
