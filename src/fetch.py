import pandas as pd
import yfinance as yf

def fetch_from_yahoo (tickers:list=['AAPL', 'MSFT']) -> pd.DataFrame:
        
        df = yf.download(tickers,period = '5Y')["Close"]
        df.index = df.index.tz_localize("UTC").tz_convert("Europe/London")
        print(len(df),df.shape)
        return df

stock = fetch_from_yahoo()

