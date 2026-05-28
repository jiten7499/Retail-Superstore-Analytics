--- TOTAL SALES & PROFIT

SELECT 
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore;

--- HIGHEST 5 PRODUCT SALES

SELECT 
    product_name,
    round(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5;

--- CATEGORY WISE TOTAL PROFIT

SELECT 
    category,
   round (SUM(profit), 2) AS total_profit
FROM superstore
GROUP BY category
ORDER BY total_profit DESC;

--- REGION WISE TOTAL SALES

SELECT 
    region,
   round (SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY region
ORDER BY total_sales DESC;

--- PRODUCT WISE TOTAL PROFIT

SELECT 
    product_name,
    round(SUM(profit), 2) AS total_profit
FROM superstore
GROUP BY product_name
HAVING total_profit < 0
ORDER BY total_profit ASC;

--- DISCOUNT & AVG PROFIT

SELECT 
    discount,
    round(AVG(profit),2) AS avg_profit
FROM superstore
GROUP BY discount
ORDER BY discount;

--- MONTH WISE TOTAL SALES

SELECT 
    SUBSTRING(order_date, 4, 2) AS month,
    round(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY month
ORDER BY month;