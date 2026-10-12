----Extra exercises: reviewSELECT, filtering and sorting, creating and changing
--tables, INSERT, UPDATE and DELETE, database design and JOINs. Before you start, check that
--SELECT COUNT(*) FROM orders; gives 15. If not, run webshop_reset.sql and press Ctrl+S.

-- 1. Clothing or Accessories, priced 150–500 kr, most expensive first
SELECT *
FROM products
WHERE category IN ('Clothing', 'Accessories')
  AND price BETWEEN 150 AND 500
ORDER BY price DESC;
--Expected: 4 rows

-- 2. Orders placed in February 2026, excluding cancelled orders
SELECT *
FROM orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01'
  AND status <> 'cancelled';

-- 3. Order lines with line total over 500 kr, biggest first
SELECT ol.order_id,
       p.name AS product_name,
       ol.quantity,
       ol.quantity * ol.unit_price AS line_total
FROM order_lines AS ol
JOIN products AS p ON p.id = ol.product_id
WHERE ol.quantity * ol.unit_price > 500
ORDER BY line_total DESC;
--Expected: 5 rows
-- 4. Customers from Uppsala or Stockholm who have placed an order
SELECT DISTINCT c.id, c.first_name, c.last_name, c.city
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.id
WHERE c.city IN ('Uppsala', 'Stockholm');
-- 5. Add Leo Falk, an order today, and its two order lines
INSERT INTO customers (first_name, last_name, city)
VALUES ('Leo', 'Falk', 'Uppsala');

INSERT INTO orders (customer_id, order_date, status)
VALUES (last_insert_rowid(), date('now', 'localtime'), 'pending');

INSERT INTO order_lines (order_id, product_id, quantity, unit_price)
SELECT last_insert_rowid(), p.id, requested.quantity, p.price
FROM (
    SELECT 'Hoodie Black' AS product_name, 1 AS quantity
    UNION ALL
    SELECT 'Socks 3-pack', 2
) AS requested
JOIN products AS p ON p.name = requested.product_name;

-- Show the receipt
SELECT p.name AS product_name,
       ol.quantity,
       ol.unit_price,
       ol.quantity * ol.unit_price AS line_total
FROM order_lines AS ol
JOIN products AS p ON p.id = ol.product_id
WHERE ol.order_id = (SELECT MAX(id) FROM orders);
--Exercise 6, check order 12’s lines first. Then restore their quantities to stock **once** and cancel the order:
SELECT p.name, ol.quantity
FROM order_lines AS ol
JOIN products AS p ON p.id = ol.product_id
WHERE ol.order_id = 12;

BEGIN;

UPDATE products
SET stock = stock + (
    SELECT SUM(ol.quantity)
    FROM order_lines AS ol
    WHERE ol.order_id = 12
      AND ol.product_id = products.id
)
WHERE id IN (
    SELECT product_id
    FROM order_lines
    WHERE order_id = 12
);

UPDATE orders
SET status = 'cancelled'
WHERE id = 12;

COMMIT;
-- 7. Deleting a product referenced by order lines should fail
DELETE FROM products
WHERE id = 1;

-- To stop selling it without deleting it, use a flag:
ALTER TABLE products ADD COLUMN is_active INTEGER NOT NULL DEFAULT 1
    CHECK (is_active IN (0, 1));

UPDATE products SET is_active = 0 WHERE id = 1;
-- 8. Add discount_percent once; then discount Shoes by 20%
ALTER TABLE products ADD COLUMN discount_percent INTEGER NOT NULL DEFAULT 0
    CHECK (discount_percent BETWEEN 0 AND 90);

UPDATE products
SET discount_percent = 20
WHERE category = 'Shoes';

SELECT name,
       price,
       ROUND(price * (1 - discount_percent / 100.0), 2) AS discounted_price
FROM products;
-- 9. Every product and its order dates, including products never ordered
SELECT p.name AS product_name,
       o.order_date
FROM products AS p
LEFT JOIN order_lines AS ol ON ol.product_id = p.id
LEFT JOIN orders AS o ON o.id = ol.order_id
ORDER BY p.name;
-- 10. Customers who bought a product in Shoes
SELECT DISTINCT c.id, c.first_name, c.last_name
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.id
JOIN order_lines AS ol ON ol.order_id = o.id
JOIN products AS p ON p.id = ol.product_id
WHERE p.category = 'Shoes';
-- 11. Each pair of customers who live in the same city, once
SELECT c1.first_name || ' ' || c1.last_name AS customer_1,
       c2.first_name || ' ' || c2.last_name AS customer_2,
       c1.city
FROM customers AS c1
JOIN customers AS c2
  ON c1.city = c2.city
 AND c1.id < c2.id
ORDER BY c1.city, customer_1, customer_2;
-- 12. After setting Hoodie Black to 649 kr, find lines with a different paid price
UPDATE products
SET price = 649
WHERE name = 'Hoodie Black';

SELECT ol.order_id,
       p.name AS product_name,
       ol.unit_price AS paid_price,
       p.price AS current_price
FROM order_lines AS ol
JOIN products AS p ON p.id = ol.product_id
WHERE ol.unit_price <> p.price;
----Exercise 13: Cinema practice lab
PRAGMA foreign_keys = ON;

CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    length_minutes INTEGER NOT NULL CHECK (length_minutes > 0),
    age_limit INTEGER NOT NULL CHECK (age_limit IN (0, 7, 11, 15))
);

CREATE TABLE salons (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE screenings (
    id INTEGER PRIMARY KEY,
    movie_id INTEGER NOT NULL REFERENCES movies(id),
    salon_id INTEGER NOT NULL REFERENCES salons(id),
    screening_date TEXT NOT NULL,
    screening_time TEXT NOT NULL,
    UNIQUE (salon_id, screening_date, screening_time)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE tickets (
    id INTEGER PRIMARY KEY,
    screening_id INTEGER NOT NULL REFERENCES screenings(id),
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    seat_number TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0),
    UNIQUE (screening_id, seat_number)
);

INSERT INTO movies (id, title, length_minutes, age_limit) VALUES
    (1, 'Moon Garden', 102, 7),
    (2, 'The Last Signal', 118, 11),
    (3, 'Little Adventures', 84, 0);

INSERT INTO salons (id, name) VALUES
    (1, 'Salon A'),
    (2, 'Salon B');

INSERT INTO customers (id, name) VALUES
    (1, 'Anna Berg'),
    (2, 'Johan Lind'),
    (3, 'Sara Holm');

INSERT INTO screenings (id, movie_id, salon_id, screening_date, screening_time) VALUES
    (1, 1, 1, '2026-11-01', '14:00'),
    (2, 2, 1, '2026-11-01', '18:00'),
    (3, 3, 2, '2026-11-02', '13:30'),
    (4, 1, 2, '2026-11-02', '17:00');

INSERT INTO tickets (screening_id, customer_id, seat_number, price) VALUES
    (1, 1, 'A1', 120),
    (1, 2, 'A2', 120),
    (2, 2, 'B1', 140),
    (2, 3, 'B2', 140),
    (3, 1, 'C1', 100),
    (3, 3, 'C2', 100);
 -- All screenings with movie title, by date and time
SELECT s.screening_date, s.screening_time, m.title, sa.name AS salon
FROM screenings AS s
JOIN movies AS m ON m.id = s.movie_id
JOIN salons AS sa ON sa.id = s.salon_id
ORDER BY s.screening_date, s.screening_time;
-- Every ticket with customer, movie and screening date
SELECT c.name AS customer,
       m.title AS movie,
       s.screening_date,
       s.screening_time,
       t.seat_number,
       t.price
FROM tickets AS t
JOIN customers AS c ON c.id = t.customer_id
JOIN screenings AS s ON s.id = t.screening_id
JOIN movies AS m ON m.id = s.movie_id
ORDER BY s.screening_date, s.screening_time, t.seat_number;
-- Screenings with no tickets sold
SELECT s.id, m.title, s.screening_date, s.screening_time
FROM screenings AS s
JOIN movies AS m ON m.id = s.movie_id
WHERE NOT EXISTS (
    SELECT 1
    FROM tickets AS t
    WHERE t.screening_id = s.id
);
