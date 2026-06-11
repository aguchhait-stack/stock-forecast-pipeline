import pandas as pd
def baseline_forecast(df_feature: pd.DataFrame) -> None:

    ticker = df_feature.columns[0]
    
    last_price = df_feature[ticker].iloc[-1]
    ma21 = df_feature[f"{ticker}_ma21"].iloc[-1]
    
    direction = "UP" if ma21 > last_price else "DOWN"
    
    print("="*40)

    print(f"MA Baseline Forecast — {ticker}")
    
    print("="*40)

    print(f"Last Price : ${last_price:.2f}")
    print(f"21-day MA : ${ma21:.2f}")
    print(f"Signal     : {direction}")