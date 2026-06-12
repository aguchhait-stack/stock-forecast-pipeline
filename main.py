from src.fetch import fetch_from_yahoo
from src.db import load_to_sql
from src.features import add_features
from src.model import baseline_forecast
from src.visualise import (plot_trend_volatility,plot_returns,plot_cumulative_return)
ticker = "AAPL"

if __name__ == "__main__":

    # Fetch data
    try: 
        
        df = fetch_from_yahoo(ticker=ticker)
    
    except ValueError as e:

        print(f"Error: {e}")
        exit(1) # stop if fails

    # Save to database (optional, continue if fails)
    try:
        load_to_sql(df)
    except Exception as e:
        print(f"Database error (continuing): {e}")

    df_features = add_features(df)
    baseline_forecast(df_features)
    plot_trend_volatility(df)
    plot_returns(df)
    plot_cumulative_return(df)
    
    print("✅ Pipeline completed successfully")



