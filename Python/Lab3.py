# Mohana Muruganandham

# Lesson Three

# Lab 3 - Collections in Python
# Part A - Conditions

# Write a program that classifies a number as positive, negative or zero.

for n in range(100):

  if n == 0:

    print(f"{n} zero")

  elif n % 2 == 0:

    print(f"{n} even")

  elif n % 2 != 0:

    print(f"{n} odd")



# Ask for an age and classify it into at least four age groups using if/elif/else.

age = int(input("What is your age? "))

if age < 18:

  print("You're a child")

elif age >= 18 and age <= 68:

  print("You're an adult")

else:

  print("You're retired")



# Create a login check using a stored username and password. Both must match.

username = "guest"

password = "python"

uname = input("Username: ")

pword = input("Password: ")

if uname == username and pword == password:

  print("You are granted access")

else:

  print("No access for you")



# Given a score from 0-100, print a grade using at least five ranges. Think carefully about condition order.

score = int(input("Score: "))

if score <= 20:

  grade = "E"

elif score > 20 and score <= 40:

  grade = "D"

elif score > 40 and score <= 60:

  grade = "C"

elif score > 60 and score <= 80:

  grade = "B"

elif score > 80:

  grade = "A"

print(f"Grade: {grade}")



# Create a shipping rule based on order total and whether the customer is a member. Use and/or.

total = float(input("Order total: "))

member = input("Member (y/n)? ") == "y"



if member and total >= 300:

  shipping = 0

elif not member and total >= 500:

  shipping = 0

elif member:

  shipping = 29

else:

  shipping = 49

print(f"Shipping: {shipping} kr, total: {total + shipping} kr")



# Write five expressions using ==, !=, >, <, >= and <= and predict each boolean result before running.

i = 5

print(i == 5) # True

print(i != 5) # False

print(i > 5) # False

print(i < 5) # False

print(i >= 5) # True



# Part B - Truthy, falsy and membership

# Create examples with empty string, non-empty string, zero, non-zero integer, empty list and non-empty list. Test each directly in an if statement.



empty_str = ""

str = "hello"

zero = 0

non_zero = 42

empty_list = []

non_empty_list = [1, 2, 3]



if empty_str:

  print(True)

else:

  print(False)

if str:

  print(True)

else:

  print(False)

if zero:

  print(True)

else:

  print(False)

if non_zero:

  print(True)

else:

  print(False)

if empty_list:

  print(True)

else:

  print(False)

if non_empty_list:

  print(True)

else:

  print(False)



# Ask for a language and check whether it exists in a predefined list of supported languages.

languages = ["Python", "Java", "Perl", "JavaScript", "TypeScript", "C++"]

lang = input("Write a language: ")

if lang in languages:

  print("Yes!!!")

else:

  print("No!")



# Create a list of blocked usernames and reject a supplied username if it appears in the list.

blocked = ["admin", "root", "guest", "test"]

username = input("Username: ")



if username in blocked:

  print("Reject")

else:

  print("Accept")



# Use not to express at least two conditions in a readable way.

username = input("Username: ")

password = input("Password: ")



if not username:

  print("Username is required")

elif not password:

  print("Password is required")

else:

  print("Login attempt registered")



# Part C - F2 loops

# Loop over a list of names and print a numbered greeting for each.

names = ["Anna", "Mona", "Carl", "Sam", "Erik"]

for i, name in enumerate(names, start=1):

  print(f"{i} Hello {name}!")



# Loop over numbers 1-50 and print only even numbers.

for n in range(1, 51):

  if n % 2 == 0:

    print(n)



# Calculate the sum of a list manually using a loop rather than sum().

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0

for number in numbers:

  total += number

print(total)



# Find the largest number in a list manually without max().

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

largest = numbers[0]

for number in numbers:

  if number > largest:

    largest = number



print(largest)



# Count how many words in a list have more than five characters.

words = [

  "cat",

  "elephant",

  "dog",

  "butterfly",

  "sun",

  "computer",

  "run",

  "keyboard",

  "hi",

  "mountain",

]

counter = 0



for word in words:

  if len(word) > 5:

    counter += 1

print(counter)



# Given a list of scores, count passes and failures using a threshold of 70.

scores = [55, 82, 70, 43, 91, 68, 77, 30, 88, 72]

threshold = 70

passes = 0

failures = 0



for score in scores:

  if score >= threshold:

    passes += 1

  else:

    failures += 1



print(f"Passes: {passes}, Failures: {failures}")



# Loop over a dictionary using keys, values and .items() in three separate examples.

prices = {"apple": 10, "bread": 25, "milk": 15, "cheese": 60, "coffee": 45}



for key in prices:

  print(key)



for value in pricesvalues():

  print(value)



for item in pricesitems():

  print(item)



# Part D - range, enumerate and nested loops

# Use range to print 10 down to 1.

for n in range(10, 0, -1):

  print(n)



# Generate the multiplication table for a number supplied by the user.

number = int(input("Write a number: "))

for i in range(1, 11):

  print(f"{number} x {i} = {number * i}")



# Use enumerate to print a playlist with track numbers starting at 1.

playlist = [

  "Bohemian Rhapsody",

  "Hotel California",

  "Stairway to Heaven",

  "Imagine",

  "Smells Like Teen Spirit",

]



for i, song in enumerate(playlist, start=1):

  print(f"{i}. {song}")



# Use nested loops to print coordinate pairs for x=1..3 and y=1..4.

for x in range(1, 4):

  for y in range(1, 5):

    print(f"{x}, {y}")



# Create a simple 5x5 text grid using nested loops.

for _ in range(5):

  for _ in range(5):

    print("*", end="")

  print()



# Part E - While loops

# Create a countdown from 10 to 0.

n = 10

while n >= 0:

  print(n)

  n -= 1



# Ask repeatedly for a password until the correct password is entered.

while True:

  answer = input("Password: ")

  if answer == "top secret":

    break

print("Logged in!")



# Create a menu that repeats until the user chooses 'quit'. The menu can simply print which option was selected.

choice = input("Menu: [1] View [2] Add [3] Delete [quit]: ")

while choice != "quit":

  print(f"You selected: {choice}")

  choice = input("Menu: [1] View [2] Add [3] Delete [quit]: ")

print("Goodbye")



# Ask the user for numbers until they enter 0. Keep a running total.

total = 0

while True:

  number = int(input("Enter a number (0 to stop): "))

  if number == 0:

    break

  total += number

print(f"Total: {total}")



# Create a guessing loop with a fixed secret number. Tell the user whether each guess is too high or too low.

number = 47

guess = 0

while guess != number:

  guess = int(input("Guess a number: "))

  if guess == number:

    print("You found it")

  elif guess < number:

    print("Too low!")

  else:

    print("Too high!")



# Part F - break and continue

# Loop through numbers 1-100 and stop when you reach the first number divisible by both 7 and 9.

for n in range(1, 101):

  if n % 7 == 0 and n % 9 == 0:

    print(f"{n} is divisible by both 7 and 9")

    break



# Loop through a list of strings and skip empty strings using continue.

words = ["apple", "", "banana", "cherry", "", "date", "", "elderberry"]

for word in words:

  if not word:

    continue

  print(word)



# Search a list for a target name. Print 'found' and break when it appears; otherwise explain how you know it was not found.

names = [

  "Anna",

  "Mona",

  "Carl",

  "Sam",

  "Erik",

  "Naveen",

  "Raja",

  "Hanna",

  "Sachin",

  "Aladdin",

  "Karl",

  "Cissi",

  "Magnus",

  "Peter",

  "Oskar",

  "Petra",

  "Zara",

  "Sara",

  "Tobias",

  "Tommy",

]

target = "Tobias"



for name in names:

  if name == target:

    print(f"{target} is found.")

    break

else:

  print(

    "Target not found"

  ) # else in for-else is only executed if the for loop is completed.



# Process a list of numeric values where negative values should be skipped and processing stops completely when the value 999 appears.

numbers = [12, -5, 47, -18, 3, 88, -22, 999, 7, -1, 34]



for number in numbers:

  if number == 999:

    break

  if number >= 0:

    print(number)





# Part G - Applied challenge: Console study tracker

# Create a list of dictionaries representing at least ten study sessions with subject and minutes.

sessions = [

  {"subject": "Python", "minutes": 45},

  {"subject": "English", "minutes": 30},

  {"subject": "Math", "minutes": 60},

  {"subject": "Python", "minutes": 90},

  {"subject": "History", "minutes": 25},

  {"subject": "English", "minutes": 50},

  {"subject": "Math", "minutes": 40},

  {"subject": "Python", "minutes": 75},

  {"subject": "History", "minutes": 35},

  {"subject": "English", "minutes": 55},

]



# Loop through the sessions and calculate total minutes.

time = 0



for session in sessions:

  time += session["minutes"]

print(time)



# Calculate total minutes per subject using a dictionary that starts empty and is updated inside the loop.

totals = {}



for session in sessions:

  subject = session["subject"]

  minutes = int(session["minutes"])

  if subject in totals:

    totals[subject] += minutes

  else:

    totals[subject] = minutes

print(totals)



# Identify the longest study session without max(…, key=…).

longest = sessions[0]

for session in sessions:

  if session["minutes"] > longest["minutes"]:

    longest = session

print(longest)



# Print only sessions longer than 45 minutes.

for session in sessions:

  if session["minutes"] > 45:

    print(session)



# Create a repeated menu that lets a user: view all sessions, view total time, filter by subject, or quit.

# Use break/continue where they genuinely improve the flow.

while True:

  choice = input("\nMenu: [1] View all [2] Total time [3] Filter by subject [quit]: ")



  if choice == "quit":

    print("Goodbye")

    break



  if choice == "1":

    for session in sessions:

      print(f"{session['subject']}: {session['minutes']} min")



  elif choice == "2":

    total = 0

    for session in sessions:

      total += session["minutes"]

    print(f"Total: {total} min")



  elif choice == "3":

    subject = input("Which subject? ")

    for session in sessions:

      if session["subject"] == subject:

        print(f"{session['subject']}: {session['minutes']} min")



  else:

    print("Unknown choice, try again")



# Part H - Stretch challenges

#for n in range(1,101) :

  if n % 3 == 0 and n % 5 == 0 :

    print(f"{n} is FizzBuzz")

  elif n % 3 == 0 :

    print(f"{n} is Fizz")

  elif n % 5 == 0 :

    print(f"{n} is Buzz")

print()





# 2

# vowels = ["a", "e", "i", "o", "u"] # both works

vowels = "aeiou"

sentence = "Python is dynamically typed programming language."

count = 0

for ch in sentence :

  if ch in vowels :

    count += 1

print(count)

print()
--------------------------------------------

# 3



languages = ["python", "c", "c++", "python", "python", "c", "java", "javascript"]

duplicates = []

originals = []

for lang in languages :

  if lang not in originals :

    originals.append(lang)

  elif lang not in duplicates :

    duplicates.append(lang)

print(f"originals : {originals}")

print(f"duplicates : {duplicates}")

print()



# 4

histogram = [3, 5, 2]

for n in histogram :

  print(n * "*")

print()
