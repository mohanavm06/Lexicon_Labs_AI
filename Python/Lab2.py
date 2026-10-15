# Mohana Muruganandham

# Lesson Two

# Lab 2 - Collections in Python

# Part A - Lists

# 1. Create a list of at least eight programming languages. Access the first, last, third and second-to-last values.



lang = ["Java", "SQL", "Python", "Bash", "JavaScript", "C++", "C", "C#"]



print(

  f"First: {lang[0]}\n Second: {lang[1]}\n Third: {lang[2]}\nSecond last: {lang[-2]}"

)



# 2. Print three different slices of the list, then print the list in reverse order using slicing.

print(

  f"Slice one: {lang[:2]}\nSlice two: {lang[-3:]}\nSlice three: {lang[2:-2]}\nReverse: {lang[::-1]}" # First two, last three, middle four and reverse

)



# 3. Use append, insert, remove and pop. After each operation, print the list so the change is visible. 

print(lang)

lang.append("Ruby")

print(lang)

lang.insert(3, "Go")

print(lang)

lang.remove("C++")

print(lang)

lang.pop()

print(lang)



# 4. Create a numeric list and calculate its length, minimum, maximum and sum using built-in functions

numbers = [1, 5, 6, 8, 12, 32, 48, 17, 99]

print(f"length: {len(numbers)}")

print(f"minimum: {min(numbers)}")

print(f"maximum: {max(numbers)}")

print(f"sum: {sum(numbers)}")



# 5. Sort one list ascending and another descending. Explain in a comment the difference between sort() and sorted

names = ["Anna", "Peter", "Gunnar", "Lisa", "Sune", "Rune"]

print(sorted(names))

print(sorted(names, reverse=True))



# names.sort() sorts the list and changes it; it returns None; sorted(numbers) returns a new sorted list, but doesn't change the original.



# 6. Demonstrate the reference/copy issue using list_b = list_a. Then fix it with copy()

list_a = [1, 2, 3, 4, 5, 6, 7]

list_b = list_a

list_b.append(8)

print(f"A: {list_a}\nB: {list_b}")



list_c = list_a.copy()

list_c.append(9)

print(f"A: {list_a}\nC: {list_c}")



# Part B - Tuples and unpacking

# 1. Create a tuple representing RGB values. Unpack it into three variables and print them

rgb = (255, 128, 64)

red, green, blue = rgb

print("Red:", red)

print("Green:", green)

print("Blue:", blue)



# 2. Create a tuple containing a person's name, age and city. Unpack and use the values in a formatted sentence

person = ("Sven", 56, "Göteborg")

name, age, city = person

print(f"{name} is {age} years old and lives in {city}.")



# 3. Try to change one element of a tuple. Explain in a comment why tuples are useful when values should not be changed

# rgb[0] = 200 #Error

# Tuples are immutable, which is useful because it prevents accidental modification and makes tuple good for storing keys in a dictionary.



# 4. Create a list containing at least four coordinate tuples such as (10, 20). Access individual x and y values

coordinates = [(10, 20), (30, 40), (50, 60), (70, 80)]

print(coordinates[0][0]) # 10

print(coordinates[0][1]) # 20



# Part C - Sets

# 1. Create a list containing duplicate course names. Convert it to a set and compare the lengths before and after

courses = ["Math", "Java", "Physics", "Math", "English", "Java", "Physics", "History"]

unique_courses = set(courses)

print("List:", courses)

print("Length of list:", len(courses))

print("\nSet:", unique_courses)

print("Length of set:", len(unique_courses))

print("\nDuplicates anniliated:", len(courses) - len(unique_courses))



# 2. Compare skills of two developers using set operations

dev1_skills = {"Java", "Python", "SQL", "Git", "Spring"}

dev2_skills = {"Python", "JavaScript", "Git", "Docker", "SQL"}



shared = dev1_skills & dev2_skills

print(f"Shared skills: {shared}")

only_dev1 = dev1_skills - dev2_skills

print(f"Only dev1 has: {only_dev1}")

all_skills = dev1_skills | dev2_skills

print(f"All skills combined: {all_skills}")



# 3. Practice adding, removing, and membership testing

languages = {"Java", "Python", "C++"}

print(f"\nStarting set: {languages}")

languages.add("Rust")

print(f"After adding Rust: {languages}")

languages.remove("C++")

print(f"After removing C++: {languages}")



print(f"'Python' in set? {'Python' in languages} | 'C++' in set? {'C++' in languages}")



# 4. Why a set is better than a list for uniqueness



# Sets are better because removing duplicates is automatic. No check before adding.

# Membership testing is fast.



# A list is better when insertion order needs to be preserved or duplicates are needed



# Part D - Dictionaries



# 1. Create a laptop dictionary and read every value by key

laptop = {

  "brand": "Apple",

  "model": "MacBook Pro",

  "RAM": "32GB",

  "storage": "512GB",

  "price": 30000,

}

print(

  f"Brand: {laptop['brand']}\nModel {laptop['model']}\nRAM: {laptop['RAM']}\nstorage: {laptop['storage']}\nPrice: {laptop['price']}\n\n"

)



# 2. Update the price, add operating_system, remove one key

laptop["price"] = 14000

laptop["operating_system"] = "Mac OS Tahoe"

del laptop["RAM"]

print(laptop)



# 3. Use .get() for an existing and a missing key

print(laptop.get("brand"))

print(laptop.get("color"))

# laptop["color"] would raise a KeyError. get() is safer when the key may not exist.



# 4. Print keys, values and items separately

print(laptop.keys())

print(laptop.values())

print(laptop.items())



# 5. Course names mapped to study hours, and total hours

courses = {"Java": 120, "Python": 80, "SQL": 40, "HTML": 30, "Git": 20}

total = sum(courses.values())

print("Total hours:", total)



# Part E - Nested collections

# 1. Create a list of at least five dictionaries representing books with title author pages and available

books = [

  {"title": "1984", "author": "George Orwell", "pages": 328, "available": True},

  {"title": "Hobbit", "author": "J.R.R. Tolkien", "pages": 310, "available": False},

  {"title": "Dune", "author": "Frank Herbert", "pages": 412, "available": True},

  {"title": "It", "author": "Stephen King", "pages": 1138, "available": True},

  {"title": "Emma", "author": "Jane Austen", "pages": 474, "available": False},

]

# 2. Access the title of the third book and the availability of the last book

print(books[2]["title"])

print(books[-1]["available"])

# 3. Change one nested value and add a new key to one book

books[0]["title"] = "1978"

books[0]["year"] = 1949

print(books[0])



# 4. Create a dictionary where each key is a department, and each value is a list of employee names

departments = {

  "Engineering": ["Anna", "Björn", "Cecilia"],

  "Sales": ["David", "Erik"],

  "HR": ["Fatima", "Gustav", "Hanna"],

}



# 5. Create a structure for three courses where each course contains a name, teacher and list of topics. Print one specific topic using chained indexing

courses = [

  {"name": "Python", "teacher": "Anna", "topics": ["lists", "dictionaries", "loops"]},

  {

    "name": "Java",

    "teacher": "Björn",

    "topics": ["classes", "interfaces", "streams"],

  },

  {"name": "SQL", "teacher": "Naveen", "topics": ["select", "joins", "indexes"]},

]

print(courses[1]["topics"][2])



# Part F - Applied challenge: Personal media catalogue

# 1. Create a catalogue containing at least eight movies, games or books

catalogue = [

  {

    "title": "The Matrix",

    "director": "The Wachowskis",

    "year": 1999,

    "genre": "Sci-Fi",

  },

  {

    "title": "Inception",

    "director": "Christopher Nolan",

    "year": 2010,

    "genre": "Sci-Fi",

  },

  {

    "title": "Pulp Fiction",

    "director": "Quentin Tarantino",

    "year": 1994,

    "genre": "Crime",

  },

  {

    "title": "The Godfather",

    "director": "Francis Ford Coppola",

    "year": 1972,

    "genre": "Crime",

  },

  {

    "title": "Interstellar",

    "director": "Christopher Nolan",

    "year": 2014,

    "genre": "Sci-Fi",

  },

  {

    "title": "Fight Club",

    "director": "David Fincher",

    "year": 1999,

    "genre": "Drama",

  },

  {

    "title": "Forrest Gump",

    "director": "Robert Zemeckis",

    "year": 1994,

    "genre": "Drama",

  },

  {

    "title": "The Dark Knight",

    "director": "Christopher Nolan",

    "year": 2008,

    "genre": "Action",

  },

]

# 2. Store all item dictionaries in one list

movie_list = list(catalogue)

print(movie_list)

genres = [movie["genre"] for movie in catalogue]

print(genres)



# 3. Create a set containing all unique categories/genres represented in the catalogue

unique_genres = {movie["genre"] for movie in catalogue}

print(unique_genres)



# 4. Create a tuple for each item's immutable identifier plus release year and associate it with each movie

for movie in catalogue:

  movie["id"] = (movie["title"], movie["year"])



print(catalogue[0])



# 5. Perform at least ten manual retrieval/update operations that demonstrate

#  nested indexing, membership and collection methods



# Retrieval — nested indexing

print(catalogue[0]["title"]) # 1. The Matrix

print(catalogue[2]["director"]) # 2. Quentin Tarantno

print(catalogue[-1]["year"]) # 3. 2008



# Membership testing

print("genre" in catalogue[0]) # 4. True

print("Batman" in catalogue[7]["title"]) # 5. False

print(1999 in [m["year"] for m in catalogue]) # 6. True



# Collection methods

print(catalogue[1].keys()) # 7.

print(catalogue[1].values()) # 8.



# Updates

catalogue[0]["year"] = 2000 # 9. overwrite existing key

catalogue[3]["rating"] = 9.2 # 10. add new key to one item



print(len(catalogue))



# 6. Print a clean summary of the catalogue without using loops yet.

print(f"Catalogue: {len(catalogue)} items\n")



print(

  f"1. {catalogue[0]['title']} ({catalogue[0]['year']}) — {catalogue[0]['director']}, {catalogue[0]['genre']}"

)

print(

  f"2. {catalogue[1]['title']} ({catalogue[1]['year']}) — {catalogue[1]['director']}, {catalogue[1]['genre']}"

)

print(

  f"3. {catalogue[2]['title']} ({catalogue[2]['year']}) — {catalogue[2]['director']}, {catalogue[2]['genre']}"

)

print(

  f"4. {catalogue[3]['title']} ({catalogue[3]['year']}) — {catalogue[3]['director']}, {catalogue[3]['genre']}"

)

print(

  f"5. {catalogue[4]['title']} ({catalogue[4]['year']}) — {catalogue[4]['director']}, {catalogue[4]['genre']}"

)

print(

  f"6. {catalogue[5]['title']} ({catalogue[5]['year']}) — {catalogue[5]['director']}, {catalogue[5]['genre']}"

)

print(

  f"7. {catalogue[6]['title']} ({catalogue[6]['year']}) — {catalogue[6]['director']}, {catalogue[6]['genre']}"

)

print(

  f"8. {catalogue[7]['title']} ({catalogue[7]['year']}) — {catalogue[7]['director']}, {catalogue[7]['genre']}"

)



# Part G - Stretch challenges



# 1



list_1 = ["Elena", "Henry", "John", "Bob", "Sam", "Dennis"]

list_2 = ["Elena", "Henry", "John", "Karan", "Harry"]

print(set(list_1) & set(list_2)) # & intersection works only on sets and not on lists, this gives values available in both

unique_1 = set(list_1) ^ set(list_2) # ^(symmetric difference) unique values in both sets

print(unique_1)

print(set(list_1) | set(list_2)) # all values from both sets

print(set(list_1) - set(list_2)) # unique values from first set

print(set(list_2) - set(list_1)) # unique values from second set

print()





# 2



online_course_platform = [

  {

    "name": "Python",

    "teacher": "Aladdin",

    "students" : ["john", "bob", "alice"],

    "topics" : ["Python fundamentals", "Object-Oriented Programming", "Data Structures"]

  },

  {

    "name": "JavaScript",

    "teacher": "Haithem",

    "students": ["Alice", "Mona", "Elena"],

    "topics": ["DOM", "Events", "Async"],

  },

  {

    "name": "Java",

    "teacher": "Genie",

    "students": ["bob", "henry"],

    "topics": ["Classes", "Collections", "Streams"],

  },

]

print()





# 3



inventory = {

  "Keyboard": 25,

  "Mouse": 40,

  "Monitor": 12,

  "USB Cable": 100,

  "Webcam": 8,

}

print()



# using loop

count = 0

for values in inventoryvalues():

  count = count + values

print(f"Total in stock (before): {count}")



# using built-in function

inventory["Webcam"] = 10

inventory["Mouse"] = 50

print(f"Total in stock (after): {sum(inventory.values())}")

print()





# 4



print("""

List :

Eg : [1,2,3]

- Ordered, indexable, allows duplicates, mutable.

- use when order matters and items may be added/removed/changed.

- BEST FIT : to-do list



Tuple :

Eg : (10, 20)

- Ordered, indexable, allows duplicates, IMMUTABLE (cannot be changed).

- Use for a fixed group of values that belong together and must

- BEST FIT : (x, y) coordinates, RGB color (255, 165, 0).



Set :

Eg : {1,2,3}

- unordered, not indexable, NO Duplicates, mutable

- Fast membership tests ("python in courses")

- only sets has & ^ | -

- BEST FIT: collecting the unique tags on a blog post, or checking which usernames appear in two lists.



Dictionary :

Eg: {"name": "Ada", "age": 25}

- Key-value pairs; keys are unique; fast lookup by key, mutable

- Use when each value needs a label instead of position number.

- BEST FIT: One product's details (brand, price, stock)



""")