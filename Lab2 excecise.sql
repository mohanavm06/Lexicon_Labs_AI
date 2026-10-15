--CREATE TABLE Example
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER CHECK (age >= 18),
    city TEXT DEFAULT 'Stockholm'
);
--What each column means
--student_id INTEGER PRIMARY KEY: This column is the primary key for the table, 
--which means it uniquely identifies each student in the table. 
--It is of type INTEGER, which means it can store whole numbers.
name TEXT NOT NULL: This column stores the name of the student.
email TEXT UNIQUE: This column stores the email address of the student.
--The UNIQUE constraint ensures that no two students can have the same email address.
city TEXT DEFAULT 'Stockholm': This column stores the city where the student lives.
--Insert data into the students table
INSERT INTO students
VALUES (1, 'Mohana', 'mohana@example.com', 25, 'Jakobsberg');
--Using the Default Value
INSERT INTO students
(student_id, name, email, age)
VALUES
(2, 'Sai', 'sai@example.com', 20);
