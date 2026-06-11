from src.fetch import fetch_from_yahoo
from src.db import load_to_sql
from src.features import add_features
from src.model import baseline_forecast
from src.visualise import (plot_trend_volatility,plot_returns,plot_cumulative_return,plot_price_analysis)
ticker = "AAPL"

if __name__ == "__main__":

    df = fetch_from_yahoo(ticker=ticker)
    load_to_sql(df)
    df_features = add_features(df)
    baseline_forecast(df_features)
    plot_trend_volatility(df_features)
    plot_returns(df_features)
    plot_cumulative_return(df_features)
    plot_price_analysis(df_features)

