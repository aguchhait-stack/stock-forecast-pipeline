# Stock Forecast Pipeline

A containerised data pipeline that downloads stock data from Yahoo Finance, stores it in PostgreSQL, engineers time-series features, and serves a live Streamlit dashboard with forecasting signals.


## Live Demo

👉 [Click here to open the live app](https://stock-forecast-pipeline-m3b9zu9mrqn5w4t4uvfptl.streamlit.app)

## Latest Analysis

![Trend & Volatility](outputs/AAPL_trend_volatility.png)
![Returns](outputs/AAPL_returns.png)
![Cumulative Return](outputs/AAPL_cumulative_return.png)

## Key Findings
- AAPL 5-year cumulative return: ~63%
- Current signal: UP (price below MA21)
- Average daily volatility tracked via 21-day rolling std

## Project Structure

```
├── Dockerfile
├── README.md
├── app.py           # Streamlit dashboard
├── docker-compose.yml
├── main.py          # pipeline entry point
├── requirements.txt
├── sql
│   └── analysis.sql # window functions, forecast signal
└── src
    ├── __init__.py
    ├── db.py       # PostgreSQL connection
    ├── features.py  # feature engineering (returns, MA, volatility)
    ├── fetch.py     # yfinance data download
    ├── model.py    # MA baseline forecast signal
    └── visualise.py
```
## Future Work

- ARIMA/SARIMA time series forecasting
- Compare ML models (XGBoost, Random Forest, LSTM)

## Tech

- Python (pandas, numpy, yfinance, sqlalchemy)
- PostgreSQL
- Docker
- Streamlit
- GitHub Actions (CI/CD)

## Quick Start

```bash
git clone https://github.com/aguchhait-stack/stock-forecast-pipeline.git
cd stock-forecast-pipeline
cp .env.example .env
docker-compose up
streamlit run app.py
```

## 📄 License & Acknowledgments

MIT License

**AI assistance:** Claude (Anthropic) and DeepSeek for CI/CD, code review, and debugging.

---

## 👨‍💻 Author

**Arijit Guchhait**  
[LinkedIn](https://www.linkedin.com/in/guchhaitarijit/)