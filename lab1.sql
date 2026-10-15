--------------LEVEL 1--------------------

-----Excercise 1----------
SELECT * FROM products WHERE category != 'Accessories' AND stock > 0 AND name LIKE '% %' ORDER BY price DESC;


-----Excercise 2----------
SELECT * FROM customers WHERE city LIKE 'S%' OR city LIKE 'M%' OR city IS NULL;

-----Excercise 3 ---------
SELECT * FROM products ORDER BY price DESC LIMIT 1 OFFSET 1;


-----Excercise 4----------
-- DIFFERENT WAYS--
SELECT * FROM customers WHERE (joined_date > '2023-31-31' AND  joined_date < '2026-01-01') ORDER BY joined_date DESC LIMIT 3;

SELECT * FROM customers WHERE joined_date BETWEEN '2023-31-31' AND '2026-01-01'  ORDER BY joined_date DESC LIMIT 3;

-----ANSWER--CONVERTING TEXT to DATE and compare Year
SELECT * FROM customers WHERE STRFTIME('%Y',joined_date) IN ('2024','2025') ORDER BY joined_date DESC LIMIT 3;


---------------------LEVEL 2----------------------------------------------


-------------Excercise 5----------------
SELECT first_name || ' ' || last_name AS customer_name from customers ORDER BY last_name;

SELECT concat_ws(' ',first_name,last_name) AS customer_name from customers ORDER BY last_name;


-------------Excercise 6-----------------
SELECT name, price,
CASE
 WHEN price < 200 THEN 'budget'
 WHEN price BETWEEN 200 AND 799 THEN 'mild'
 WHEN price >= 800 THEN 'premium'
END as Price_Level
FROM products ORDER BY PRICE;


-----------Excercise 7------------

SELECT first_name, city FROM customers
WHERE city IN (SELECT city FROM customers GROUP BY city HAVING COUNT(*) > 1)
ORDER BY city, first_name;  

-------------------------  QUESTIONS -------------------------


--1. Show products that are Clothing or Shoes and cost more than 1000 kr.
 (3 rows)
SELECT * FROM products WHERE category IN ('Clothing', 'Shoes') AND price > 1000;
SELECT * FROM products WHERE (category = 'Clothing' OR category = 'Shoes') AND price > 1000;
-- Without brackets AND runs before OR, so the price check only applies to Shoes (7 rows).


--2. For every product in stock, show name, price, stock and the total value

SELECT name, price, stock, price * stock AS stock_value
FROM products 
WHERE stock > 0 
ORDER BY stock_value DESC;

--3. Which customers have a first name with exactly 4 letters?

SELECT * FROM customers WHERE first_name LIKE '____';


--4. Sort the products by price, cheapest first, and show only products number 6 to 10.

SELECT * FROM products ORDER BY price LIMIT 5 OFFSET 5;