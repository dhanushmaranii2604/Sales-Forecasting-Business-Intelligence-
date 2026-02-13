CREATE TABLE IF NOT EXISTS sales (
    Order_Date TEXT,
    Category TEXT,
    Product_Name TEXT,
    Sales REAL,
    Profit REAL
);

SELECT * 
FROM sales 
LIMIT 10;

SELECT 
    strftime('%Y', Order_Date) AS Year,
    strftime('%m', Order_Date) AS Month,
    SUM(Sales) AS Monthly_Sales
FROM sales
GROUP BY Year, Month
ORDER BY Year, Month;

SELECT 
    Category, 
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;

SELECT 
    Product_Name, 
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Product_Name
HAVING Total_Profit < 0
ORDER BY Total_Profit ASC;

SELECT 
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales;
