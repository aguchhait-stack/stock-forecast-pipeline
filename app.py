import streamlit as st
from src.fetch import fetch_from_yahoo
from src.features import add_features
from src.model import baseline_forecast
from src.visualise import plot_trend_volatility, plot_returns, plot_cumulative_return

st.set_page_config(page_title="Stock Dashboard", layout="wide")

ticker = st.text_input("Enter Ticker", value="AAPL").upper()

if st.button("Run Analysis"):
    try:
        df = fetch_from_yahoo(ticker)
        df_features = add_features(df)
    except ValueError as e:
        st.error(f"Error: {e}")
        st.stop()
    

    last_price = df[ticker].iloc[-1]
    forecast_price = df_features[f"{ticker}_ma21"].iloc[-1]
    
    st.metric("Current Price", f"${last_price:.2f}")
    st.metric("Forecast Price (MA21)", f"${forecast_price:.2f}", 
              delta=f"{forecast_price - last_price:.2f}")
    
    baseline_forecast(df_features)
    
    plot_trend_volatility(df_features)
    st.image(f"outputs/{ticker}_trend_volatility.png")

    plot_cumulative_return(df_features)
    st.image(f"outputs/{ticker}_cumulative_return.png")
    
    plot_returns(df_features)
    st.image(f"outputs/{ticker}_returns.png")

    
    