-- Exercises: Joining tables
-- Use webshop.db for all exercises.
--============================================
SELECT COUNT(*) FROM orders; 
-- Check first: SELECT COUNT(*) FROM orders; should give 15.

-- Exercise 1
-- Show every order with the customer's first name, last name and the order status.
-- Expected: 15 rows
SELECT 
	customers.first_name, customers.last_name, orders.status
FROM orders
INNER JOIN customers
	ON orders.customer_id = customers.customer_id;

-- Exercise 2
-- Show all orders made by Simon.
-- Expected: 3 rows
SELECT
    customers.first_name,
    customers.last_name,
    orders.order_id,
    orders.status
FROM orders
INNER JOIN customers
    ON orders.customer_id = customers.customer_id
WHERE LOWER(customers.first_name) = 'simon';


-- Exercise 3
-- Show all orders from customers in stockholm, newest first.
-- Expected: 3 rows
SELECT
	customers.customer_id, customers.first_name, customers.city, orders.order_id, orders.order_date
FROM orders
INNER JOIN customers
	ON orders.customer_id = customers.customer_id
WHERE LOWER(customers.city) = 'stockholm'
ORDER BY
	orders.order_date DESC;

-- Exercise 4
-- Show every order item with the product name and category.
-- Expected: 23 rows
SELECT order_items.order_id, order_items.product_id, products.name, products.category
FROM order_items
INNER JOIN products
	ON order_items.product_id = products.product_id;
	
-- Exercise 5
-- Which orders contained Shoes? Show order_id and product name.
-- Expected: 4 rows
SELECT order_items.order_id, order_items.product_id, products.name, products.category
FROM order_items
INNER JOIN products
	ON order_items.product_id = products.product_id
WHERE LOWER(products.category) = 'shoes';

-- Exercise 6
-- Show the full receipt for order 10: product name, quantity, unit price and line total.
-- Expected: 2 rows
SELECT order_items.order_id, 
	products.name, 
	order_items.quantity, 
	order_items.unit_price, 
	order_items.quantity * order_items.unit_price AS line_total
FROM products 
INNER JOIN order_items 
	ON products.product_id = order_items.product_id
WHERE order_items.order_id = 10;

-- Exercise 7
-- Show which customers have bought a Hoodie Black (first name and order date).
-- Expected: 3 rows
SELECT customers.first_name, orders.order_date, products.name
FROM customers
INNER JOIN orders
	ON customers.customer_id = orders.customer_id
INNER JOIN order_items
	ON order_items.order_id = orders.order_id
INNER JOIN products
	ON products.product_id = order_items.product_id
WHERE LOWER(products.name) = 'hoodie black';

-- Exercise 8
-- Show all customers and their orders, including customers with no orders.
SELECT
    customers.first_name,
    customers.last_name,
    orders.order_id,
    orders.status
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id;
-- Expected: 17 rows


-- Exercise 9
-- Which products have never been sold?
SELECT
    products.product_id,
    products.name
FROM products
LEFT JOIN order_items
    ON products.product_id = order_items.product_id
WHERE order_items.order_id IS NULL
-- Expected: 2 rows


-- Exercise 10
-- Challenge: show customers from Uppsala and every product they bought
--This is a one-to-many (1:N) relationship.
-- (first name, product name, quantity).
SELECT customers.first_name, products.name, order_items.quantity
	FROM customers
	JOIN orders ON customers.customer_id = orders.customer_id
	JOIN order_items ON orders.order_id = order_items.order_id
	JOIN products ON order_items.product_id = products.product_id
	WHERE customers.city = 'Uppsala';
-- Expected: 8 rows