-- students table
-- teachers table
-- instruments table
-- lessons table with foreign keys
-- lesson_students junction table (N:M)
-- teacher_instruments junction table (N:M)
-- Primary keys on all tables
-- Foreign key relationships correctly defined

CREATE TABLE IF NOT EXISTS "instruments" (
	"instrument_id"	INTEGER,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("instrument_id")
);
CREATE TABLE IF NOT EXISTS "lesson_students" (
	"lesson_id"	INTEGER,
	"student_id"	INTEGER,
	PRIMARY KEY("lesson_id","student_id"),
	FOREIGN KEY("lesson_id") REFERENCES "lessons"("lesson_id"),
	FOREIGN KEY("student_id") REFERENCES "students"("student_id")
);
CREATE TABLE IF NOT EXISTS "lessons" (
	"lesson_id"	INTEGER,
	"teacher_id"	INTEGER NOT NULL,
	"instrument_id"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"room"	TEXT NOT NULL,
	PRIMARY KEY("lesson_id"),
	FOREIGN KEY("instrument_id") REFERENCES "instruments"("instrument_id"),
	FOREIGN KEY("teacher_id") REFERENCES "teachers"("teacher_id")
);
CREATE TABLE IF NOT EXISTS "students" (
	"student_id"	INTEGER,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("student_id")
);
CREATE TABLE IF NOT EXISTS "teacher_instruments" (
	"teacher_id"	INTEGER,
	"instrument_id"	INTEGER,
	PRIMARY KEY("teacher_id","instrument_id"),
	FOREIGN KEY("instrument_id") REFERENCES "instruments"("instrument_id"),
	FOREIGN KEY("teacher_id") REFERENCES "teachers"("teacher_id")
);
CREATE TABLE IF NOT EXISTS "teachers" (
	"teacher_id"	INTEGER,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("teacher_id")
);
