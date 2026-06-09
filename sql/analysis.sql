SELECT "Date",
       "Close",
       lag("Close",1) over (order by "Date"),
       lead("Close",1) over (order by "Date"),
       AVG("Close") 
        over (ORDER BY "Date" ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS MV
FROM silver.stock_price 