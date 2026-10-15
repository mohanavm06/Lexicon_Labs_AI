# Mohana M
# esson six
# # Python och AI
# Lab 6
# Part A - 

# 1

squares = []

for n in range(1,21):

  squares.append(n ** 2)

print(squares)



#using list comprehension

sq_nums = [n ** 2 for n in range(1,21)]

print(sq_nums)





# 2

print("\nQ-2")

even_nums = [n for n in range(1,101) if n % 2 == 0]

print(even_nums)





# 3



names = ["harry potter", " ron weasley ", " Hermione granger", " Emma", " john "]

normalizing = [name.strip().title() for name in names]

print(f"Before : {names}")

print(f"After : {normalizing}")





# 4



pass_mark = 75

scores = [40, 50, 60, 80, 90, 45, 75]

passing_scores = [s for s in scores if s>=pass_mark]

print(f"All : {scores}")

print(f"Passed : {passing_scores}")





# 5



scores = [40, 50, 60, 80, 90, 45, 75]

labels = ["PASS" if s >= pass_mark else "FAIL" for s in scores]

print(f"Scores : {scores}")

print(f"Label : {labels}")





# 6

# reference from Lab 3 Part C



words = ["Python", "C", "C++", "C#", "SQL", "JavaScript", "TypeScript"]

long_words = []

for word in words:

  if len(word) > 5:

    long_words.append(word)

print(long_words)



# Refactoring

longer_words = [word for word in words if len(word) > 5]

print(longer_words)



# from lab 4 Part D

students = [

  {

    "name" : "Harry Potter",

    "score" : 85,

    "active" : True

  },

  {

    "name" : "Ron Weasley",

    "score" : 75,

    "active" : True

  },

  {

    "name" : "Hermione Granger",

    "score" : 95,

    "active" : True

  },

  {

    "name" : "Luna",

    "score" : 55,

    "active" : False

  }

]



def get_active_users(users):

  active_users = []

  for student in users:

    if student["active"]:

      active_users.append(student)

  return active_users



active_list = get_active_users(students)

print(active_list)



# Refactoring



def active_users(users):

  return [student for student in users if student["active"]]

active_students = active_users(students)

print(active_students)



# from lab 4 Part F

def student_participants(partpnts):

  student_participants = []

  for participant in partpnts:

    if participant["student"]:

      student_participants.append(participant["name"])

  return student_participants



participants = [

  {'name': 'john', 'age': 18, 'student': True, 'fee': 100},

  {'name': 'bob', 'age': 17, 'student': True, 'fee': 0},

  {'name': 'alice', 'age': 22, 'student': False, 'fee': 500}

]

student_participant_list = student_participants(participants)

print(f"Student participants list : {student_participant_list}")





# Refactoring

def student_participant(partpnts):

  return [p["name"] for p in partpnts if p["student"]]



print(f"Participated students : {student_participant(participants)}")





# 1



squares = {n : n**2 for n in range(1,11)}

print(squares)



# 2



words = ["Python", "C", "C++", "C#", "SQL", "JavaScript", "TypeScript"]

word_length = {word : len(word) for word in words}

print(word_length)





# 3



languages = [" pyThoN", "C", "pYTHOn", "C++", "SqL", "C#", "sQL", " JavaSCRipt ", " TyPEsCrIpT ", "  JavaSCRipT  "]

without_duplicates = {lang.lower().strip() for lang in languages}

# note : unordered and unique

print(without_duplicates)





# 4



products = {

  "Bed_Frame" : 4000,

  "Kitchen_Toy" : 1095,

  "Colours" : 250,

  "Board" : 300,

  "Soft_Toy" : 500

}



threshold = 500

low_budget = {k : v for k, v in products.items() if v < threshold}

print(low_budget)





# 5

print("\nQ-5")

students = [

  {

    "name" : "Harry Potter",

    "score" : 85,

    "active" : True

  },

  {

    "name" : "Ron Weasley",

    "score" : 75,

    "active" : True

  },

  {

    "name" : "Hermione Granger",

    "score" : 95,

    "active" : True

  },

  {

    "name" : "Luna",

    "score" : 55,

    "active" : False

  },

  {

    "name" : "Emily",

    "score" : 60,

    "active" : True

  }

]



pass_mark = 75

score = {s["name"] : "PASS" if s["score"] >=pass_mark else "FAIL" for s in students}

print(score)

# 1

playlist = ["Jai Ho", "Chaiyya Chaiyya", "Chinna Chinna Aasai", "Mustafa Mustafa", "Nenjukkul Peidhidum"]
for index, song in enumerate(playlist, 1):
    print(index, song)


# 2

tasks = ["Login", "Submit_Attendance", "Complete_Lab", "Push_To_Git"]
for index, task in enumerate(tasks, 1):
    print(f"Task {index}: {task}")



# 3

threshold = 500
values = [100, 200, 300, 400, 500, 600, 700, 800, 900]
large_values = [index for index, val in enumerate(values) if val > threshold]
print(large_values)


# 4

words = ["python", "java", "SQL", "C"]
for i in range(len(words)):
    print(i, words[i])

for i, word in enumerate(words):
    print(i, word)

print("""
- range(len(words)), gives only the index, so need to look for the item with words[i]
- Without enumerate words need to be used twice to get length of words len(words) and for indexing words[i]
- enumerate removes manual indexing, gives both the index and the item in one step.
""")

# 1

names =["Harry Potter", "Hermione", "John", "Ron", "Emma"]
scores = [85, 90, 60, 78, 95]

for name, score in zip(names, scores):
    print(f"{name} - {score}")


# 2

student_scores = dict(zip(names, scores))
print(student_scores)


# 3

products = ["Ikea Cot", "Table", "Curtains", "Blinds"]
prices = [4000, 2500, 1000, 1500]
stocks = [50, 20, 100, 200]
product_status = list(zip(products, prices, stocks))
print(product_status)


# 4

product_1 = ["Ikea Cot", "Table", "Curtains", "Blinds", "Kids Kitchen Set"]
price_1 = [4000, 2500, 1000, 1500, 1025]
stock_1 = [50, 20, 100, 200]
product_status_1 = list(zip(product_1, price_1, stock_1))
print(f"Products : {product_status_1}, \n when lists doesn't match value is silently ignored")


# 5

print("product_status = [('Ikea Cot', 4000, 50), ('Table', 2500, 20), ('Curtains', 1000, 100), ('Blinds', 1500, 200)]")
for name, cost, availability in product_status:
    print(f"Product name : {name}")
    print(f"Price : {cost} kr")
    print(f"Availability : {availability}\n")


# 6

student = "Harry"
another_student = "John"
print(f"Before : \nStudent : {student} \nAnother Student: {another_student}")
another_student, student = student, another_student
print(f"After : \nStudent : {student} \nAnother Student: {another_student}")
print("""
Notes :
Python works out the right side and packs it into a tuple.
When values are separated by a comma, Python makes a tuple from them. It reads the current values => ("Harry", "John")
another_student gets assigned as "Harry" first, then student gets "John" second
""")

# 1

words = ["Python", "C", "c++", "C#", "SQL", "JavaScript", "TypeScript"]
sorting = sorted(words, key=len)
print(f"Before sorting : {words}")
print(f"After sorting : {sorting}")

# 2

students = [
    {
        "name" : "Harry Potter",
        "score" : 85,
        "active" : True
    },
    {
        "name" : "Ron Weasley",
        "score" : 75,
        "active" : True
    },
    {
        "name" : "Hermione Granger",
        "score" : 95,
        "active" : True
    },
    {
        "name" : "Luna",
        "score" : 55,
        "active" : False
    },
    {
        "name" : "Emily",
        "score" : 60,
        "active" : True
    }
]

scores_low_to_high = sorted(students, key= lambda student: student["score"])
print(f"Scores low to high")
for student in scores_low_to_high:
    print(f"{student['name']} - {student['score']}")

scores_high_to_low = sorted(students, key= lambda student: student["score"], reverse=True)
print(f"\nScores high to low :")
for student in scores_high_to_low:
    print(f"{student['name']} - {student['score']}")


# 3

products = {"Ikea cot": 4500, "Kids Kitchen set":1025, "curtains" : 1000, "Blinds": 2500}
sort_products = sorted(products.items(), key=lambda product: product[1])
for p in sort_products:
    print(f"{p[0]} - {p[1]} kr")

# 4
people = [
    {
        "first_name" : "Harry",
        "last_name" : "Potter"
    },
    {
        "first_name" : "Hermione",
        "last_name" : "Granger"
    },
    {
        "first_name" : "Ron",
        "last_name" : "Weasley"
    }
]
sort_people = sorted(people, key= lambda person: person["last_name"])
print(sort_people)


# 5

books = [
    {"title": "The Hobbit", "author": "Tolkien", "pages": 310, "year": 1937},
    {"title": "Matilda", "author": "Dahl", "pages": 240, "year": 1988},
    {"title": "Dune", "author": "Herbert", "pages": 612, "year": 1965},
    {"title": "Coraline", "author": "Gaiman", "pages": 162, "year": 2002},
    {"title": "Wonder", "author": "Palacio", "pages": 315, "year": 2012},
]

def book_pages(book):
    return book["pages"]

print("1 - Sorting Books")
sorting_book_pages = sorted(books, key=book_pages)
print("Sorting based on book pages using function")
for book in sorting_book_pages:
    print(f"{book['title']} - {book['pages']} ")

sort_book_pages = sorted(books, key=lambda book: book["pages"])
print("\nSorting based on book pages using lambda")
for book in sort_book_pages:
    print(f"{book['title']} - {book['pages']} ")
print("Final comparison : lambda also looks simpler and understandable")

# sort by average of the two exams from list of student dicts
students = [
    {"name": "Harry", "house": "Gryffindor", "exam_1": 72, "exam_2": 88},
    {"name": "Hermione", "house": "Gryffindor", "exam_1": 98, "exam_2": 99},
    {"name": "Draco", "house": "Slytherin", "exam_1": 85, "exam_2": 80},
    {"name": "Luna", "house": "Ravenclaw", "exam_1": 90, "exam_2": 76},
    {"name": "Cedric", "house": "Hufflepuff", "exam_1": 81, "exam_2": 89},
]

def avg_score(student):
    total = student["exam_1"] + student["exam_2"]
    average =  total/2
    return average

student_avg_score = sorted(students, key=avg_score)
print("\n2 - Student Average Score")
print("Using normal function")
for stu_score in student_avg_score:
    print(f"{stu_score['name']} - {avg_score(stu_score)}")

student_avg_score_1 = sorted(students, key=lambda student: (student["exam_1"] + student["exam_2"])/2)
print("\nUsing lambda - Unable to print the average score as lambda function used")
for student_score in student_avg_score_1:
    print(f"{student_score['name']}")

print("Final comparison : lambda looks simpler but not easily understandable. Normal function is clear stating average score")

print("\n3 - Sorting emails by domain ")
emails = [
    "ron.weasley@hogwarts.edu",
    "Emma@gmail.com",
    "john.smith@Outlook.com",
    "kid_coder@yahoo.com",
    "harry@hogwarts.edu",
]

print("Using lambda")
by_domain = sorted(emails, key= lambda email: (email.strip().lower().split("@"))[1])
print(by_domain)

print("\nUsing normal function")
def email_domain(email):
    email = email.strip().lower()
    parts = email.split("@")
    return parts[1]

by_domain_1 = sorted(emails, key=email_domain)
print(by_domain_1)
print("\nFinal comparison : \nIn lambda, normalizing, splitting and indexing is in same line. \nIn the def, normalizing, splitting and indexing are on separate lines, which might be easy for other developer to understand about code")

print("Overall comparison : I'd pick lambda when I don't want that function later in my code, and would pick def when I want to reuse at some other parts of code like average score, also for code readability")


# 1

products = [
    {
        "category" : "  textiles ",
        "product" : "cushion cover",
        "price": "119",
        "stock": 30,
    },
    {
        "category" : "Textiles",
        "product" : "RUG",
        "price": "4 495 kr",
        "stock": "50",
    },
    {
        "category" : "decoration",
        "product" : "Tealight holder  ",
        "price": 99.0,
        "stock": 100,
    },
    {
        "category" : "Decoration",
        "product" : "Mirror",
        "price": 699,
        "stock": None,
    },
    {
        "Category" : "Table Setting",
        "product" : "glass",
        "price": "129.00",
        "stock": 60,
    },
    {
        "category" : "table setting",
        "product" : "Cutlery",
        "price": 599,
        "stock": -15,
    },
    {
        "category" : "Lighting",
        "product" : "Ceiling Lamp",
        "price": "1995:-",
        "stock": 70,
    },
    {
        "category" : "LIGHTING",
        "product" : " table lamp",
        "price": 799,
    },
    {
        "category" : "Living Room",
        "product" : "3-seater sofa",
        "price": "14995 SEK",
        "stock": "30 pcs",
    },
    {
        "category" : "Living room",
        "product" : "Coffee Table",
        "price": 2495,
        "stock": 30,
    },
    {
        "category" : "Barnrum",
        "product" : "Rock elk",
        "price": 449,
        "stock": "0",
    },
    {
        "category" : " CHILDREN",
        "product" : "Children's kitchen",
        "price": "995 kr",
        "stock": 2,
    },
    {
        "category" : "Living Room",
        "product" : "coffee table ",
        "price": 2495,
        "stock": 30,
    }
]

# 2


def key_normalizing(product):
    return {key.strip().lower(): value for key, value in product.items()}

normalized_product_keys = [key_normalizing(product) for product in products]

def price_normalizing(price):
    if isinstance(price, (int, float)):  # checks whether price is int or float
        return int(price)

    text = price.lower()
    for messy in ["kronor", "sek", ":-", ":", " ", "kr"]:
        text = text.replace(messy, "")
    return int(float(text))   # int("129.00") raises a ValueError as int() can't read a decimal value. float("129.00") gives 129.0, and int(129.0) gives 129

def stock_normalizing(stock):
    # case 1 checks if None then returns 0 without checking further loop
    if stock is None:
        return 0

    # case 2 checks if value is int or float or string
    if isinstance(stock, (int, float)):
        number = int(stock)
    else:
        text = stock.lower()
        for messy in ["pieces", "pcs", " ",]:
            text = text.replace(messy, "")
        number = int(float(text))

    # case 3 check if value is negatvie
    if number < 0:
        return 0

    return number

normalized_products = [
    {
        "category": product.get("category", None).strip().capitalize(),
        "product": product.get("product", None).strip().capitalize(),
        "price": price_normalizing(product.get("price")),
        "stock": stock_normalizing(product.get("stock"))
    }
    for product in normalized_product_keys
]
print(normalized_products)


# 3

in_stock = []
for product in normalized_products:
    if product["stock"] > 0 and product["product"] not in in_stock:
        in_stock.append(product["product"])
print(f"Products in stock : {in_stock}")

# 4

seen = set()
unique_products_list = []
for product in normalized_products:
    if product["product"] not in seen:
        seen.add(product["product"])
        unique_products_list.append(product)

unique_categories = {product["category"] for product in normalized_products}
print(unique_categories)


# 5

product_mapping= {}
for product in normalized_products:
    inv_value = product["price"] * product["stock"]
    product_mapping[product["product"]] = inv_value
print(product_mapping)

# 6

sorting_products = sorted(product_mapping.items(), key=lambda product: product[1], reverse=True)
for product in sorting_products:
    print(f"{product[0]} - {product[1]}")


# 7

for index, inv in enumerate(sorting_products, start=1):
    print(f"{index}. {inv[0]} - {inv[1]}")


# 8

#using unique product list => list of dict Eg : [{'category': 'Textiles', 'product': 'Cushion cover', 'price': 119, 'stock': 30}, {'category': 'Textiles', 'product': 'Rug', 'price': 4495, 'stock': 50}, ......]
names = [product["product"] for product in unique_products_list]
prices = [product["price"] for product in unique_products_list]
product_status = ["In Stock" if product["stock"] > 0 else "Out of Stock" for product in unique_products_list]
print(f"\nProduct Names : {names}")
print(f"\nProduct Prices : {prices}")
product_metadata = list(zip(names, prices, product_status))
print("\nProduct Stock :")
for index, (name, price, status) in enumerate(product_metadata, start=1):
    print(f"{index}. {name} (price : {price}) - {status}")


# 9


complicated = {product["product"]: "Very cheap" if product["price"] < 200 else "Cheap" if product["price"] < 600 else "Budget" for product in unique_products_list if product["stock"] > 0 and product["price"] < 1000}
print(f"Complicated : {complicated}")

def price_label(price):
    if price < 200:
        return "Very cheap"
    elif price < 600:
        return "Cheap"
    return "Budget"

def is_low_budget_in_stock(product):
    return product["stock"] > 0 and product["price"] < 1000

clear = {
    product["product"]: price_label(product["price"])
    for product in unique_products_list
    if is_low_budget_in_stock(product)
}

print(f"Clear : {clear}")
print("""
Over-Complicated : has multiple conditions and has difficult readability
Clear : uses normal functions and has better code readability
""")
# 1
print("Q-1")
numbers = [[1,5], [50, 30], [-1,0], [45, 30]]

simple_nums_list = []
for num_pair in numbers:
    for num in num_pair:
        simple_nums_list.append(num)
print(simple_nums_list)

print("Using list comprehenshion")
sim_nums_list = [no for no_pair in numbers for no in no_pair]
print(sim_nums_list)


# 2

# Outer comprehension makes one row per number, inner comprehension fills that row
table = [[row * col for col in range(1, 11)] for row in range(1, 6)]
# print(table)

for row in table:
    print(row)

# proper alignment
for row in table:
    print(" ".join(f"{n:3}" for n in row))

# Good readability two levels of nesting with clear names (row, col) is still easy to follow.
# If it needed a third level or an extra if-condition, a normal nested loop would be clearer.

# 3
print("\nQ-3")
names = ["Harry", "Emma", "Ron", "Hermione", "John"]
scores = [72, 45, 88, 91, 38]
PASS_MARK = 50

passing_students = [
    {"name": name, "score": score}
    for name, score in zip(names, scores)
    if score >= PASS_MARK
]

for student in passing_students:
    print(student)

# 4

scores = [72, 45, 88, 91, 38, 100]

# Using loop to find if anyone failed ie, score is below 50
anyone_failed = False
for score in scores:
    if score < 50:
        anyone_failed = True
print("Anyone failed (loop):", anyone_failed)

# Using any() to find if anyone failed ie, score is below 50
print("Anyone failed (any):", any(score < 50 for score in scores))


# using loop to find if everyone passed with score 50 or higher
everyone_passed = True
for score in scores:
    if score < 50:
        everyone_passed = False
print("Everyone passed (loop):", everyone_passed)

# using all()
print("Everyone passed (all):", all(score >= 50 for score in scores))

# 5

# 1: list comprehension
numbers = [1, 2, 3, 4]

# Long way
doubled = []
for n in numbers:
    doubled.append(n * 2)
print(doubled)

# Short way
doubled = [n * 2 for n in numbers]
print(doubled)


# 2: enumerate
fruits = ["apple", "banana", "cherry"]

# Long way
for i in range(len(fruits)):
    print(i + 1, fruits[i])

# Short way
for number, fruit in enumerate(fruits, start=1):
    print(number, fruit)


# 3: zip
names = ["Anna", "Chen"]
ages = [25, 30]

# Long way
for i in range(len(names)):
    print(names[i], ages[i])

# Short way
for name, age in zip(names, ages):
    print(name, age)


# 4: swap two variables

# Long way
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)

# Short way
a = 1
b = 2
a, b = b, a
print(a, b)


# 5: f-string
name = "Anna"
age = 25

# Long way
print("My name is " + name + " and I am " + str(age) + " years old")

# Short way
print(f"My name is {name} and I am {age} years old")
