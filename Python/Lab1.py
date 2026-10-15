# Mohana Muruganandham
# # Lesson One
# # Python och AI

# Lab 1


print("Mohana Muruganandham")

print("Python and AI")

print("Todays exercise  goal")



print("Part A – Warm-up: Python basics")

print("2 Create variables\n")

name = "Mohana Muruganandham"

age = 40

height = 1.65

student = True



print(name)

print(type(name))

print(age)

print(type(age))

print(height)

print(type(height))

print(student)

print(type(student))



print("\n3 Change the value stored in one variable to a different data type.")

print(type(age))

age = str(age)

print(type(age)) # demonstrates that Python is dynamically typed



print("\n4 Create two numeric variables and calculate...")



a = 10

b = 3

print(f"Addition: {a + b}")

print(f"Subtraction: {a - b}")

print(f"Multiplication: {a * b}")

print(f"Division: {a / b}")

print(f"Floor division: {a // b}")

print(f"Remainder: {a % b}")

print(f"Exponentiation: {a**b}")



print("\n5 Write three examples where explicit type conversion is necessary")



age = "40"

print(f"Years to retirement: {70 - int(age)}")

days_left = 3.333333333333

print(f"It's {days_left} left.")

points = 450

print("You have " + str(points) + " points.")





print("\nPart B - User input and calculations")

print("A program that asks for name and year of birth, then prints an approximate age.")

this_year = 2026

born_year = int(input("Which year are you born? "))

print(f"You are {this_year - born_year} years old.")



print(

  "Ask the user for the price of an item and a discount percentage and calculate the price."

)

price = int(input("Which price (SEK)? "))

discount = int(input("Which discount percentage (integer)? "))

print(f"The final price is {int(price - (price * discount / 100))} SEK.")



print(

  "\nNormalize text input so accidental surrounding spaces do not affect the result."

)

text = input("Write text with whitespace before and/or after: ")

print(text.strip())



print("\nPart B – User input and calculations")

print("Create a generated user ID from parts of the person's name and year of birth")

first_name = input("First name: ")

last_name = input("Last name: ")

birth_year = input("Birth year: ")

print(f"Your username is {first_name[:4] + last_name[:4] + birth_year[2:]}")





print(

  "Ask for a temperature in Celsius and convert it to Fahrenheit using F = C * 9 / 5 + 32."

)

celsius = int(input("Provide a temperature C°: "))

print(f"That is {celsius * 9 / 5 + 32} degrees Fahrenheit.")



print(

  "Ask for the length and width of a room and calculate area and perimeter. Use descriptive variable names."

)

length = int(input("Length: "))

width = int(input("Width: "))

print(f"Area: {length * width}\nPerimeter: {2 * length + 2 * width}.")



print(

  "Extend one of the programs so invalid numeric input is discussed in comments: what would happen today if the user entered 'hello'?"

)

# If a string is entered where an integer is expected, the program can't convert it to an integer = ValueError.



print("Part C - Strings")



print(

  "Store a full sentence in a variable. Print its length, uppercase version, lowercase version and a version with leading/trailing whitespace removed."

)

str = "  This is a full sentence stored in a variable.\t"

print(

  f"Length: {len(str)}\nUppercase: {str.upper()}\nLowercase: {str.lower()} \nStripped: {str.strip()}"

)



print(

  "\nAsk for first name and last name. Create a formatted full name using an f-string."

)

first_name = input("First name: ")

last_name = input("Last name: ")

print(f"{first_name.capitalize()} {last_name.capitalize()}")



print(

  "Given the string 'python programming', print the first character, last character, first six characters, last eleven characters and the entire string reversed."

)

str = "python programming"

print(str[0])

print(str[-1])

print(str[:6])

print(str[-11:])

print(str[::-1])



print("Create a username generator.")

# ask for first and last name, remove surrounding spaces, convert to lowercase and create a username using the first

# three letters of the first name plus the first five letters of the last name.



first = input("First name: ")

last = input("Last name: ")

print(f"{first.strip().lower()[:3]}{last.strip().lower()[:5]}")





print("Use string operations to extract the part before @ and the domain after @")

email = "svenpleriksson@gmail.com"

[first, last] = email.split("@")

print(f"First part: {first} \nLast: {last}")



print(

  "Create a sentence containing the word 'Java'. Replace it with 'Python' and print."

)

str = "Java is the best language"

new_str = str.replace("Java", "Python")

print(str)

print(new_str)



print("Part D – String investigation")

print(

  "Predict the output of at least eight expressions using indexing and slicing before running them. Include positive indexes, negative indexes, omitted start/end values and a step."

)



str = "En meningslös mening för test."



print(str[0]) # E

print(str[0:5]) # En me

print(str[3:7]) # meni

print(str[8:11]) # gsl

print(str[19:29]) # g för test.

print(str[-7:-1]) # r test

print(str[1:-1]) # n meningslös mening för test

print(str[::2]) # E eiglsmnn ö et



print(

  "\nCreate a variable containing 'Artificial Intelligence'. Produce at least six different slices from it and comment what each slice means."

)

str = "Artificial Intelligence"



print(str[0]) # first letter

print(str[-1]) # last letter

print(str[3:7]) # letter 4-7 'ific'

print(str[::2]) # every other letter

print(str[-5:]) # last five letters

print(str[:4]) # first five letters



print(

  "Investigate the difference between .split(), .strip(), .replace() and the in operator. Write one useful example of each."

)





# Demonstrate string immutability: attempt conceptually to change one character, explain why direct character assignment fails, then create a new modified string instead.



str = "String"

# str[0] = x # Doesn't work = SyntaxError, string immutable

new_str = str.replace("S", "x")

print(new_str)



print("Part E – Applied challenge: Registration summary")

# Build a console program that collects: first name, last name, city, year of birth and favourite programming language.

# Normalize text input so accidental surrounding spaces do not affect the result.

# Create a generated user ID from parts of the person's name and year of birth.

# Print a clean multi-line summary using f-strings.

# Print the initials, full name length excluding the space, and the favourite language reversed.

# Add at least three extra pieces of derived information of your own choice using only concepts from Lesson 1.



first = input("First name: ").strip()

last = input("Last name: ").strip()

city = input("Your city: ").strip()

year = input("Birth year: ").strip()

fav_prog_lang = input("Your favourite programming language: ").strip()



print(f"UserId: {first[:2]}{last[:2]}{year[-2:]}")

print(

  f"Name: {first.capitalize()} {last.capitalize()} \nCity: {city.capitalize()} \nBirthyear: {year}\nFavourite programming language: {fav_prog_lang}."

)

print(f"Initials: {first[0]}{last[0]}")

print(f"Full name, no space: {len(first + last)}")

print(f"Favourite lang backwards: {fav_prog_lang[::-1]}")

print(f"Every other letter: {first.capitalize()[::2]} {last.capitalize()[::2]}")

print(f"Reversed first name: {first[::-1]}")

print(f"City upper case: {city.upper()}")



print("Part F - Stretch challenges Python Foundation")

# Create a simple seconds converter: input total seconds and calculate whole hours, remaining minutes and remaining seconds using // and %.

seconds = int(input("Seconds: "))

print(

  f"Hours: {seconds // 3600}, Minutes: {(seconds % 3600) // 60}, Seconds: {seconds % 60}"

)



# Given a four-digit integer, extract and print each digit without converting the number to a string.

num = 1234

print(f"First number: {num // 1000}")

print(f"Second number: {num // 100 % 10}")

print(f"Third number: {num // 10 % 10}")

print(f"Fourth number: {num % 10}")



# Create a text masking program that displays only the first two and last two characters of a supplied word, replacing the middle with * characters.

text = input("Enter a word: ")

print(f"{text[:2]}{'*' * (len(text) - 4)}{text[-2:]}")





# Write five short 'predict before running' examples that you could give to another student. Include at least one type conversion and two string slices.

# Write a message…



# 1. Type conversion — predict the result and the type

x = "10"

y = 3

print(int(x) + y) # 13 (int), not "103" — int(x) converts before adding



# 2. String slice — positive indexes

word = "programming"

print(word[3:7]) # "gram"



# 3. String slice — negative index with step

word = "programming"

print(

  word[-4::-1]

) # "mmargorp" — starts at 'm' (index -4) and steps backwards to start



# 4. Type conversion inside an f-string / arithmetic

price = "199"

print(f"Double: {int(price) * 2}") # Double: 398 — without int() it would be "199199"



# 5. Boolean from a comparison plus slice

name = "Python"

print(name[:2] == "Py") # True
