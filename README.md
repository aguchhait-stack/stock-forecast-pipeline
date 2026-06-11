# Stock Forecast Pipeline

A containerized data pipeline that downloads stock data (AAPL, MSFT, GOOGL, JPM, SPY) from Yahoo Finance, stores it in PostgreSQL, and runs SQL analysis with forecasting capabilities.

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stock-forecast-pipeline.streamlit.app)

## Latest Analysis

![Trend & Volatility](outputs/AAPL_trend_volatility.png)
![Returns](outputs/AAPL_returns.png)
![Cumulative Return](outputs/AAPL_cumulative_return.png)


## Tech

Python / PostgreSQL / Docker / SQL

## Quick Start

```bash
git clone https://github.com/aguchhait-stack/stock-forecast-pipeline.git
cd stock-forecast-pipeline
docker-compose up
streamlit run app.py
```
## Author

**Arijit Guchhait**  
[LinkedIn](https://www.linkedin.com/in/guchhaitarijit/)