-- ==============================================================
-- Stock Market Analysis (5-year period) — SQL Queries
-- Database : stock_db
-- User     : postgres
-- localhost: 5432
-- Run      : psql -U postgres -d stock_db -f sql/analysis.sql
-- Note: Replace 'aapl' with target ticker column name
-- ===============================================================

WITH add_features AS (

SELECT 
        date,

        aapl AS aapl_current_price,

        (aapl - LAG(aapl) OVER  (ORDER BY date)) * 100 /
        LAG(aapl) OVER  (ORDER BY date) AS aapl_daily_return,

        (aapl-LAG(aapl,5) OVER  (ORDER BY date)) * 100 /
        LAG(aapl,5) OVER  (ORDER BY date) AS aapl_weekly_return,

        CASE 
                WHEN ROW_NUMBER () OVER (ORDER BY date) < 21 THEN NULL
                ELSE AVG(aapl) OVER (ORDER BY date ROWS BETWEEN 20 PRECEDING AND CURRENT ROW)
        END AS aapl_ma21,
        
        CASE 
                WHEN ROW_NUMBER() OVER (ORDER BY date) < 21 THEN NULL
                ELSE STDDEV(aapl) OVER (ORDER BY date ROWS BETWEEN 20 PRECEDING AND CURRENT ROW)
        END AS aapl_vol21

FROM stock)      

SELECT *,
        CASE 
                WHEN date = MAX(date) OVER () AND aapl_current_price < aapl_ma21 THEN 'UP'
                WHEN date = MAX(date) OVER () AND aapl_current_price > aapl_ma21 THEN 'DOWN'
        END AS aapl_forecast_ma21
FROM add_features
ORDER BY date DESC;








