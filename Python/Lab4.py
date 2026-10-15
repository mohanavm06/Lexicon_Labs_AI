# Mohana

# Lesson Four

# Lab 4 - Collections in Python



# Part A - Function fundamentals

# Write functions greet(), show_course_name() and print_separator(). Call each more than once.





def greet():

  print("Hello")





def show_course_name():

  return "Python and AI"





def print_separator():

  print(", ")





greet()

print(show_course_name())

print_separator()

greet()

print(show_course_name())

print_separator()





# Write greet_person(name) and introduce(name, city).

def greet_person(name):

  print("Hello", name)





greet_person("Sven")





def introduce(name, city):

  print(f"Hi I'm, {name} and I live in {city}.")





introduce("Mohana", "Stockholm")





# Write add(a, b), subtract(a, b), multiply(a, b) and divide(a, b). Each must return a value.

def add(a, b):

  return a + b





def subtract(a, b):

  return a - b





def multiply(a, b):

  return a * b





def divide(a, b):

  if b == 0:

    return "Error: Division by zero is not allowed."

  return a / b





print(add(5, 3))

print(subtract(10, 4))

print(multiply(3, 7))

print(divide(10, 2))

print(divide(20, 0))





# Demonstrate parameter vs argument in comments using one of your functions.

def multiply(a, b): # a och b är parametrar

  return a * b





print(multiply(3, 7)) # 3 och 7 är argument





# Create calculate_area(width, height) and use its returned value in another calculation.

def calculate_area(width, height):

  return width * height





room_area = calculate_area(12, 15)

Volume = room_area * 2.15





# Part B - Return values

# Write is_even(number) returning True/False.





def is_even(number):

  if number % 2 == 0:

    return True

  else:

    return False





print(is_even(48))





# Write get_larger(a, b) returning the larger value without max().

def get_larger(a, b):

  if a > b:

    return a

  return b





get_larger(7, 9)





# Write classify_score(score) returning PASS or FAIL.

def classify_score(score):

  if score >= 50:

    return "Top class"

  elif score < 50 and score >= 10:

    return "Pass"

  else:

    return "Try again"





# Write full_name(first_name, last_name) returning a formatted string.





def full_name(first_name, last_name):

  return f"{first_name.capitalize()} {last_name.capitalize()}"





print(full_name("sven", "eriksson"))





# Write calculate_discount(price, percent) returning the discounted price.

def calculate_discount(price, percent):

  return price * percent / 100





# Show with a small example why print(result) inside a function is not the same as return result.

def print_discount(price, percent):

  print(price * percent / 100) # prints discount, returns none





def return_discount(price, percent):

  return price * percent / 100 # retruns discout, prints nothing





# Part C - Defaults and keyword arguments

# Create greet(name, greeting='Hello'). Test positional and keyword arguments.





def greet_b(name, greeting="Hello"):

  print(f"{greeting.capitalize()} {name.capitalize()}!")





greet_b("Sven")

greet_b("Sven", "Hej")

greet_b("Sven", greeting="Hej på dig")





# Create calculate_price(price, quantity=1, discount=0). Return the final total.

def calculate_price(price, quantity=1, discount=0):

  return price * quantity * (1 - discount / 100)





# Create create_profile(name, city='Unknown', active=True) returning a dictionary.

def create_profile(name, city="Unknown", active=True):

  return {

    "name": name,

    "city": city,

    "active": active,

  }





print(create_profile("sven", "Göteborg"))

print(create_profile("sven"))





# Call one function using keyword arguments in a different order from the parameter definition.

def calc_discount(price, percent):

  return price * percent / 100





calc_discount(percent=20, price=100)



# Write one invalid default-parameter ordering as a comment and explain why it is invalid.

# def broken(price=100, percent):

#   return price * percent / 100





# Part D - Functions and collections

# Write calculate_total(numbers) manually using a loop.

def calculate_total(numbers):

  total = 0

  for num in numbers:

    total += num

  return total





# Write count_even(numbers).

def count_even(numbers):

  count = 0

  for num in numbers:

    if num % 2 == 0:

      count += 1

  return count





# Write get_long_words(words, minimum_length) returning a new list.

def get_long_words(words, minimum_length):

  result = []

  for word in words:

    if len(word) >= minimum_length:

      result.append(word)

  return result





# Write find_student(students, name) where students is a list of dictionaries. Return the matching dictionary or None.

def find_student(students, name):

  for student in students:

    if student.get("name") == name:

      return student

  return None





# Write average_score(students) for a list of dictionaries containing score values.

def average_score(students):

  total = 0

  for student in students:

    total += student.get("score", 0)

  return total / len(students)





# Write get_active_users(users) returning only dictionaries where active is True.

def get_active_users(users):

  active_users = []

  for user in users:

    if user.get("active") is True:

      active_users.append(user)

  return active_users





# Part E - Decomposition

# Build a temperature report using separate functions for Celsius-to-Fahrenheit conversion, classification ('cold/warm/hot') and formatting.





def to_fahrenheit(celsius):

  return celsius * 9 / 5 + 32





def classify_temperature(temp):

  if temp <= 10:

    return "cold"

  elif temp > 10 and temp <= 25:

    return "warm"

  else:

    return "hot"





def formatting(celsius, fahrenheit, category):

  return f"{celsius} degrees Centigrade is {fahrenheit} degrees Fahrenheit and thats {category}!"





celsius = 25

fahrenheit = to_fahrenheit(celsius)

category = classify_temperature(celsius)

print(formatting(celsius, fahrenheit, category))





# Build a small order calculation using separate functions for subtotal, discount and final total.





def subtotal(quantity, price):

  return quantity * price





def discount(price, percentage):

  return price * percentage / 100





def total(price, discount):

  return price - discount





subtot = subtotal(10, 100)

disc = discount(subtot, 25)

print("Final price: ", total(subtot, disc))





# Refactor one earlier exercise that contains repeated code into at least three functions.

# Write a main-like section at the bottom of the file that calls your functions in a clear sequence.

def check_truthiness(value):

  if value:

    print(True)

  else:

    print(False)





def run_tests(test_values):

  for value in test_values:

    check_truthiness(value)





def main():

  empty_str = ""

  my_str = "hello"

  zero = 0

  non_zero = 42

  empty_list = []

  non_empty_list = [1, 2, 3]



  values = [empty_str, my_str, zero, non_zero, empty_list, non_empty_list]

  run_tests(values)





main()



# Part F - Applied challenge: Event registration processor

# 1. Create functions to normalise a participant name, validate an age range using boolean return values, calculate a registration fee based on age/student status, and create a participant dictionary.



participants = {}





def normalize_name(name: str) -> str:

  return name. capitalise ()





def validate_age(age) -> bool:

  if age >= 18:

    return True

  else:

    return False





def registration_fee(age, is_student) -> int:

  if age < 25 or is_student:

    return 100

  else:

    return 200





# 2. Create at least eight participant dictionaries using your functions.

def create_participant(name, age, is_student):

  return {

    "name": normalize_name(name),

    "age": age,

    "valid": validate_age(age),

    "is_student": is_student,

    "fee": registration_fee(age, is_student),

  }





participants["anna"] = create_participant("anna", 22, True)

participants["erik"] = create_participant("erik", 30, False)

participants["fanny"] = create_participant("fanny", 31, False)

participants["gunnar"] = create_participant("gunnar", 33, True)

participants["hanna"] = create_participant("hanna", 37, True)

participants["ingvar"] = create_participant("ingvar", 45, False)

participants["jenny"] = create_participant("jenny", 48, False)

participants["kalle"] = create_participant("kalle", 15, True)





# 3. Write a function that receives the participant list and returns the total expected registration revenue.

def registration_revenue(participants):

  total = 0

  for participant in participants.values():

    total += participant["fee"]



  return total





print(registration_revenue(participants))





# 4. Write a function that returns only student participants.

def students(participants):

  student_participants = []



  for participant in participants.values():

    if participant["is_student"]:

      student_participants.append(participant)



  return student_participants





print(students(participants))





# 5. Write a function that returns the oldest participant.

def oldest(participants):

  oldest_age = -1

  oldest_name = None



  for participant in participants.values():

    if participant["age"] > oldest_age:

      oldest_name = participant["name"]

      oldest_age = participant["age"]



  return oldest_name





print(oldest(participants))





# 6. Write a function that creates a readable summary string for one participant.

def participant_summary(participant):

  return f"{participant['name']}, {participant['age']}, fee: {participant['fee']} kr"





print(participant_summary(participants["jenny"]))

# 1

def min_max(num, min_v, max_v):

  for n in num:

    if n < min_v:

      min_v = n

    elif n > max_v:

      max_v = n

  return min_v, max_v





# 2

def is_palindrome(word):

  return word.lower().strip() == word[::-1].lower().strip()





# 3

def character_frequency(word):

  characters = {}

  for ch in word:

    if ch not in characters:

      characters[ch] = 1

    else:

      characters[ch] += 1

  return characters



# 4

def pos_neg_zero(nums):

  classify = {

    "positive" : 0,

    "negative" : 0,

    "zero" : 0

    }

  for n in nums:

    if n == 0:

      classify["zero"] += 1

    elif n > 0:

      classify["positive"] += 1

    else:

      classify["negative"] += 1

  return classify







# 5

def add(a: int, b: int) -> int:

  """Return the sum of two numbers."""

  return a + b



def is_even(num: int) -> bool:

  """Return True if num is even, otherwise False."""

  return num % 2 == 0



def classify(celsius: float) -> str:

  """Classify a Celsius temperature as cold, warm, or hot."""

  if celsius < 10:

    return "cold"

  elif celsius <= 25:

    return "warm"

  else:

    return "hot"



def calculate_area(width: int, height: int) -> int:

  """ Calculates area, which is the product of width and height"""

  return width * height



def calculate_cost(area: int, price_per_sqm: int) -> int:

  """ Calculates cost by performing the product of area and price per sqm."""

  return area * price_per_sqm



def report_area_cost(width: int, height: int, price_per_sqm: int) -> int:

  """ Calculates cost by calling calculate_area and calculate_cost functions"""

  area = calculate_area(width, height)

  cost = calculate_cost(area, price_per_sqm)

  return cost



if __name__ == "__main__":

 

  numbers = [1, 2, 3, 4, 55, 40, 33, 20, 0]

  min_value, max_value = min_max(numbers, numbers[0], numbers[0])

  print(f"Minimum num : {min_value}, Maximum num : {max_value}")

  print()





  words = ["Madam", "level", "Sam", "Mona", "Harry", "Test"]

  for word in words:

    result = "Palindrome" if is_palindrome(word) else "Not a Palindrome"

    print(f"{word} is {result}")

  print()





  print(character_frequency("hello"))

  print()





  numbers = [0, 1, 2, 3, 4, 0, 55, 40, 33, 20, 0]

  print(pos_neg_zero(numbers))

  print()

