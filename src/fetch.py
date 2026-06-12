import pandas as pd
import yfinance as yf



def fetch_from_yahoo (ticker:str = None) -> pd.DataFrame:

        if ticker is None:
                raise ValueError("Please provide a ticker ")
        
        df = yf.download(ticker,period = '5Y')["Close"]
        
        # yf.download() return empty DataFrame for invaid ticker
        if df.empty:
                raise ValueError (f"No data found, symbol may be delisted {ticker}")

        df.index = df.index.tz_localize("UTC").tz_convert("Europe/London")
        print(f"✅ Fetched {ticker} | {len(df)} trading days")
        return df


