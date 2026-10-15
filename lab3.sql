
-- ============================================
-- PART 1: INSERT, UPDATE AND DELETE
-- Database: webshop.db
-- ============================================

-- First, check that there are 15 orders.
SELECT COUNT(*) FROM orders;


-- Exercise 1
-- Add a new customer.
INSERT INTO customers(first_name, last_name, email, city, joined_date)
VALUES ('Harry', 'Potter', 'harry@mail.com', 'Stockholm', '2025-01-02');


-- Exercise 2
-- Add two products at the same time.
INSERT INTO products(name, category, price, stock)
VALUES
    ('Scarf', 'Accessories', 229, 15),
    ('Gloves', 'Accessories', 199, 20);


-- Exercise 3
-- Emma orders 2 Beanies.

-- First, create the order.
INSERT INTO orders(customer_id, order_date)
VALUES (7, '2026-10-07');

-- Then add the products to the order.
INSERT INTO order_items(order_id, product_id, quantity, unit_price)
VALUES (16, 10, 2, 179);


-- Exercise 4
-- Try to add a product with quantity 0.
INSERT INTO order_items(order_id, product_id, quantity, unit_price)
VALUES (1, 1, 0, 100);

-- Why does it fail?
-- Quantity must be greater than 0.
-- The CHECK constraint stops this.


-- Exercise 5
-- Change order 12 to shipped.
UPDATE orders
SET status = 'shipped'
WHERE order_id = 12;


-- Exercise 6
-- Change Water Bottle stock to 50.
UPDATE products
SET stock = 50
WHERE product_id = 5;


-- Exercise 7
-- Increase Accessories prices by 10%.
UPDATE products
SET price = price * 1.10
WHERE category = 'Accessories';

-- Check the new prices.
SELECT name, price
FROM products
WHERE category = 'Accessories';


-- Exercise 8
-- Delete the cancelled order.

-- First, delete its order items.
DELETE FROM order_items
WHERE order_id = 7;

-- Then delete the cancelled order.
DELETE FROM orders
WHERE status = 'cancelled';

-- Why delete order items first?
-- order_items has a FOREIGN KEY linked to orders.
-- We must delete the child rows before the parent row.
-- Otherwise, we may get a FOREIGN KEY error.


-- Exercise 9
-- Click Revert Changes in DB Browser.
-- Then check that there are 15 orders.
SELECT COUNT(*) FROM orders;


-- ============================================
-- PART 2: DATABASE DESIGN
-- Exercises 10 to 15: Theory
-- Exercise 16: Create music.db
-- ============================================


-- Exercise 10
-- Table: student | phone_numbers | course1 | course2 | course3
-- What are the problems?

-- 1. One cell can contain many phone numbers.
--    Each phone number should be stored separately.

-- 2. Courses are stored in different columns.
--    What if a student takes more than 3 courses?

-- 3. There is no PRIMARY KEY.
--    We cannot easily identify each student.

-- 4. Course names are repeated.
--    This can cause spelling mistakes.

-- Solution:
-- Create separate tables for students,
-- phone numbers, courses and student_courses.


-- Exercise 11
-- What is wrong with the products column in order_sheet?

-- It breaks First Normal Form (1NF).
-- One cell contains many products.

-- Example: "Hoodie, Cap x2"

-- Solution:
-- Create an order_items table.
-- Store each product in a separate row.
-- Use order_id, product_id and quantity.


-- Exercise 12
-- Table:
-- order_id | customer_id | customer_email | order_date

-- Which column is in the wrong place?

-- customer_email

-- Why?
-- Email belongs to the customer, not the order.
-- If the email changes, we may need to update many orders.
-- This breaks Third Normal Form (3NF).

-- Solution:
-- Store email in the customers table.
-- Keep only customer_id in the orders table.


-- Exercise 13
-- Music school: Find the main things (entities).

-- Students
-- Teachers
-- Lessons
-- Instruments


-- Exercise 14
-- Find the relationships.

-- One teacher can teach many lessons.       (1:N)
-- One instrument can be used in many lessons.(1:N)
-- Many students can attend many lessons.     (N:M)
-- Many teachers can teach many instruments.  (N:M)


-- Exercise 15
-- Draw the ER diagram for the music school.

-- My ER diagram is saved in music.erd.md.



-- Exercise 16
-- Create tables in music.db
-- ============================================

-- Table 1: Teachers
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);


-- Table 2: Students
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);


-- Table 3: Instruments
CREATE TABLE instruments (
    instrument_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);


-- Table 4: Lessons
CREATE TABLE lessons (
    lesson_id INTEGER PRIMARY KEY,
    teacher_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    room TEXT NOT NULL,

    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);


-- Table 5: Teachers and Instruments
CREATE TABLE teacher_instruments (
    teacher_id INTEGER REFERENCES teachers(teacher_id),
    instrument_id INTEGER REFERENCES instruments(instrument_id),

    PRIMARY KEY (teacher_id, instrument_id)
);


-- Table 6: Lessons and Students
CREATE TABLE lesson_students (
    lesson_id INTEGER REFERENCES lessons(lesson_id),
    student_id INTEGER REFERENCES students(student_id),

    PRIMARY KEY (lesson_id, student_id)
);
