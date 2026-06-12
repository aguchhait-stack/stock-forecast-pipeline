import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    
    df_feature = df.copy()

    for ticker in df.columns:
        df_feature[f"{ticker}_daily_return"] = df_feature[ticker].pct_change(periods=1).mul(100)
        df_feature[f"{ticker}_weekly_return"] = df_feature[ticker].pct_change(periods=5).mul(100)
        df_feature[f"{ticker}_ma21"] = df_feature[ticker].rolling(window=21).mean()
        df_feature[f"{ticker}_vol21"] = df_feature[ticker].rolling(window=21).std()
        
    print(f"✅ Features added for {ticker} | Shape: {df_feature.shape}")
    return df_feature
