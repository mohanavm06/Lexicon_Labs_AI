# Mohana Muruganandham
# # Lesson Seven
# # Python och AI

# Lab 7
# # Part A - Classes and objects
# # 1. Create a Book class with title, author and pages. Create at least four Book objects and print their
# # attributes.

# books = []


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages


# books.append(Book("Röde Orm", "Frans G. Bengtsson", 604))
# books.append(Book("Doktor Glas", "Hjalmar Söderberg", 168))
# books.append(Book("Kallocain", "Karin Boye", 240))
# books.append(Book("Låt den rätte komma in", "John Ajvide Lindqvist", 512))

# for book in books:
#     print(f"{book.title} av {book.author}, {book.pages} sidor")

# # 2. Create a Laptop class with brand, model, ram_gb and price. Create three separate objects and
# # change the price of one object.

# laptops = []


# class Laptop:
#     def __init__(self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# laptops.append(Laptop("Apple", "MacBook Air M3", 16, 15990))
# laptops.append(Laptop("Lenovo", "ThinkPad X1 Carbon", 32, 24500))
# laptops.append(Laptop("Dell", "XPS 13", 16, 18990))

# laptops[0].price += 1000

# for laptop in laptops:
#     print(f"{laptop.brand} av {laptop.model}, {laptop.ram_gb}, {laptop.price} kr.")


# # 3. Create two objects with the same attribute values. Use is to check whether they are the same object.
# laptop1 = Laptop("Apple", "MacBook Air M3", 16, 15990)
# laptop2 = Laptop("Apple", "MacBook Air M3", 16, 15990)

# print(laptop1 is laptop2)

# # 4. Add a default value to at least one __init__ parameter.
# class Laptop:
#     def __init__(self, brand: str, model: str, price: int, ram_gb: int = 16): # default RAM and type hints
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# # 5. Create one object using keyword arguments.
# class Laptop:
#     def __init__(self, brand: str, model: str, price: int, ram_gb: int = 16):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# leno_data = {"brand": "Lenovo", "model": "ThinkPad X1 Carbon Gen 12", "price": 24990}

# lenovo = Laptop(**leno_data)

# # Part B - Methods and state
# # 1. Extend your Book class with an is_long() method that returns True if the
# # book has more than 300 pages.
# books = []


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def is_long(self):
#         if self.pages > 300:
#             return True
#         else:
#             return False


# # 2. Create a BankAccount class with owner and balance. Add a deposit() method that changes the
# # balance.

# # 3. Add a withdraw() method. Prevent withdrawals that would make the balance negative by raising a
# # ValueError.


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         else:
#             self.balance -= amount


# # 4. Create a Task class with title and completed=False. Add complete() and reopen() methods.
# class Task:
#     def __init__(self, title: str, completed: bool = False):
#         self.title = title
#         self.completed = completed

#     def complete(self):
#         self.completed = True

#     def reopen(self):
#         self.completed = False


# # 5. Create at least two objects from one of your classes and show that changing the state of one object
# # does not change the other.
# task1 = Task("Write CV")
# task2 = Task("Apply for jobs")

# print(
#     f"Before: task1.completed = {task1.completed}, task2.completed = {task2.completed}"
# )

# task1.complete()

# print(
#     f"After: task1.completed = {task1.completed}, task2.completed = {task2.completed}"
# )

# # Part C - Instance and class attributes
# # 1. Create a Product class with name and price as instance attributes.
# # 2. Add a class attribute called tax_rate that is shared by all Product objects.
# # 3. Add a price_with_tax() method that returns the price including tax.
# # 4. Create at least three Product objects and print their prices with tax.
# # 5. Change Product.tax_rate and show how it affects the Product objects.
# # 6. Give one Product object its own tax_rate. Print the tax rate from that
# # object, another Product object and the Product class.


# class Product:
#     tax_rate: float = 0.25

#     def __init__(self, name: str, price: float):
#         self.name = name
#         self.price = price

#     def price_with_tax(self) -> float:
#         return self.price * (1 + self.tax_rate)


# coffee_maker = Product("Coffee maker", 799.00)
# toaster = Product("Toaster", 449.00)
# kettle = Product("Kettle", 349.00)

# for product in [coffee_maker, toaster, kettle]:
#     print(f"{product.name}: {product.price_with_tax():.2f} kr")

# Product.tax_rate = 0.12

# for product in [coffee_maker, toaster, kettle]:
#     print(f"{product.name}: {product.price_with_tax():.2f} kr")


# # Part D - Collections of objects
# # 1. Create at least six Student objects with name and score.
# # 2. Store all Student objects in a list.
# # 3. Loop through the list and print each student's name and score.
# # 4. Add a get_status() method that returns "PASS" or "FAIL" based on the score.
# # 5. Loop through the students again and print each student's name and status.
# # 6. Use a list comprehension to create a new list containing only students with a score of 70 or higher.
# class Student:
#     PASS_THRESHOLD = 50

#     def __init__(self, name: str, score: int):
#         self.name = name
#         self.score = score

#     def get_status(self) -> str:
#         return "PASS" if self.score >= self.PASS_THRESHOLD else "FAIL"


# students = [
#     Student("Alice", 85),
#     Student("Bob", 42),
#     Student("Charlie", 70),
#     Student("Diana", 91),
#     Student("Erik", 38),
#     Student("Fatima", 67),
# ]

# for student in students:
#     print(f"{student.name}: {student.score}")

# Part E - Objects inside objects
# 1. Create a Teacher class with a name.
# 2. Create a Course class with a course name and a teacher. The teacher should be a Teacher object.
# 3. Create a Teacher object and use it when creating a Course object.
# 4. Print the course name and the teacher's name through the Course object.
# 5. Extend Course so that it also contains an initially empty list of Student objects.
# 6. Add an add_student() method and use it to add at least three Student objects to the course.
# 7. Loop through course.students and print the name of every student.


class Teacher:
    def __init__(self, name: str):
        self.name = name


class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students: list[Student] = []

    def add_student(self, student: "Student") -> None:
        self.students.append(student)


teacher = Teacher("Alladin")
course = Course("Introduction to Python", teacher)

print(f"Course: {course.course_name}")
print(f"Teacher: {course.teacher.name}")


class Student:
    PASS_THRESHOLD = 50

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def get_status(self) -> str:
        return "PASS" if self.score >= self.PASS_THRESHOLD else "FAIL"


course.add_student(Student("Alice", 25))
course.add_student(Student("Bob", 42))
course.add_student(Student("Charlie", 70))

for student in course.students:
    print(student.name)

# The code includes comments mapped directly to your instructions 
# (e.g., # Part F3, # Part G1) so you can see exactly where each requirement is handled.
class Student:
    # Part G4: Add a useful class attribute. 
    # PASSING_SCORE belongs to the class rather than the object because the threshold
    # to pass a test is a universal standard applied to all students, not a unique 
    # trait that varies from person to person.
    PASSING_SCORE = 50

    def __init__(self, name, score):
        self.name = name
        # We use the setter method during initialization to ensure validation is applied
        self.set_score(score)

    # Part G1: Method that updates a student's score with validation
    def set_score(self, new_score):
        # Part F8: Validation using ValueError
        if not isinstance(new_score, (int, float)):
            raise ValueError(f"Score for {self.name} must be a number.")
        if new_score < 0 or new_score > 100:
            raise ValueError(f"Score for {self.name} must be between 0 and 100.")
        self.score = new_score

    # Part F3: Method that returns "PASS" or "FAIL"
    def get_status(self):
        if self.score >= Student.PASSING_SCORE:
            return "PASS"
        return "FAIL"


class Teacher:
    # Part F4: Teacher should contain at least a name
    def __init__(self, name):
        self.name = name


class Course:
    # Part F5: Course contains a name, a Teacher object and a list of Student objects
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    # Part F6: Add a method for adding a student
    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Only Student objects can be added to the course.")
        self.students.append(student)

    # Part F6: Add a method for showing how many students are currently in the course
    def get_student_count(self):
        return len(self.students)

    # Part F7: Method that returns a list containing only the students who passed
    def get_passing_students(self):
        return [student for student in self.students if student.get_status() == "PASS"]

    # Part G2: Method to find students above a score threshold
    def get_top_students(self, threshold):
        return [student for student in self.students if student.score >= threshold]

    # Part F10: Print a simple course summary
    def print_summary(self):
        passing_students = self.get_passing_students()
        passing_names = [student.name for student in passing_students]
        
        print(f"=== Course Summary: {self.name} ===")
        print(f"Teacher: {self.teacher.name}")
        print(f"Total Students: {self.get_student_count()}")
        print(f"Passed Students: {', '.join(passing_names) if passing_names else 'None'}")
        print("===================================\n")


# --- DEMONSTRATION SECTION ---

if __name__ == "__main__":
    # Part F9: Create one Teacher object and one Course object
    t1 = Teacher("Mr. Smith")
    course1 = Course("Intro to Python", t1)

    # Part F9: Create at least five Student objects
    s1 = Student("Alice", 85)
    s2 = Student("Bob", 42)
    s3 = Student("Charlie", 95)
    s4 = Student("Diana", 50)
    s5 = Student("Evan", 30)

    # Demonstrate adding students
    for student in [s1, s2, s3, s4, s5]:
        course1.add_student(student)

    # Part F10 & F9: Print summary to demonstrate methods work
    course1.print_summary()

    # Part G1 Demo: Update a student's score with validation
    print("--- Updating Evan's Score ---")
    print(f"Evan's original status: {s5.get_status()} (Score: {s5.score})")
    s5.set_score(75)
    print(f"Evan's new status: {s5.get_status()} (Score: {s5.score})\n")

    # Part G2 Demo: Find students above a threshold
    print("--- Top Performing Students (Score >= 90) ---")
    top_performers = course1.get_top_students(90)
    for student in top_performers:
        print(f"- {student.name} ({student.score})")
    print()

    # Part F8 Demo: Demonstrate the ValueError validation works
    print("--- Testing Validation Error Handling ---")
    try:
        s6 = Student("Fiona", 150) # Invalid score
    except ValueError as e:
        print(f"Successfully caught error: {e}")
    print()

    # Part G3: Create another Course object and show its list is separate
    print("--- Testing Separate Course Instances ---")
    t2 = Teacher("Ms. Lovelace")
    course2 = Course("Advanced Data Structures", t2)
    
    s7 = Student("Grace", 99)
    course2.add_student(s7)

    print(f"Students in {course1.name}: {course1.get_student_count()}")
    print(f"Students in {course2.name}: {course2.get_student_count()}")
