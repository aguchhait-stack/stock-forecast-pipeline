SELECT *
FROM stock;

----
WITH stock_rolling_metrics AS 
(
        SELECT date,                      
        ROUND(AVG(aapl) OVER (ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW)::NUMERIC,2) 
        AS sma_30,

        ROUND(STDDEV(aapl) OVER (ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW)::NUMERIC,2)
        AS vola_30
        from stock)

SELECT * FROM stock_rolling_metrics ORDER BY date DESC LIMIT 5; 
