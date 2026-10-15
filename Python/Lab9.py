# Mohana Muruganandham
# Lesson Nine
# Python AI 
# Lab 9 
# Email Notification ──> send()
# SMSNotification   ──> send()
# PushNotification  ──> send()
#                          ↑
#                   same method name
#                   different behaviour
# ==========================================
# Part A - Polymorphism
# ==========================================
# 1. Create three classes
class EmailNotification:
    # 2. Give all three classes a method called send() with a different return message
    def send(self):
        return "Sending Email: Check your inbox!"
class SMSNotification:
    def send(self):
        return "Sending SMS: Check your text messages!"
class PushNotification:
    def send(self):
        return "Sending Push Notification: Check your phone alerts!"

# 3. Create one object from each class and store them in the same list
notifications = [
EmailNotification(),
SMSNotification(),
PushNotification()
]
# 4. Loop through the list and call send() on every object
for notification in notifications:
    print(notification.send())
    # 5. Explanation of why the loop does not need to know the exact class:
"""
EXPLANATION:
This loop relies on Polymorphism (specifically dynamic duck typing in Python). 
The loop does not need to know the exact class of each object because all three 
classes implement the same method signature (`send()`). 

As long as every object in the list responds to the `.send()` method call, the loop 
can treat them uniformly without needing to check their specific type or class.
"""

# Part B - Polymorphism with inheritance
# ==========================================
# 1. Base class Document with title attribute and describe() method
class Document:
    def __init__(self,title):
        self.title = title
    def describe(self):
        return f"Document: {self.title}"
# 2. Subclasses inheriting from Document
class PDFDoucment(Document):
# 3. Override describe() method
    def describe(self):
        return f"PDF Document: '{self.title}' (Portable Document Format, read-only layout)"
class TextDocument(Document):
    def describe(self):
        return f"TextDocument: '{self.title}'(Plain Text formate, easily editable)"
# 4. Create several PDFDocument and TextDocument objects in one list
documents = [
    PDFDocument("Mohana.pdf"),
    TextDocument("Notes.txt"),
    PDFDocument("User_Manual.pdf"),
    TextDocument("TodoList.txt")
]

# 5. Loop through the list and print each title and describe() result. 
for doc in documents:
    print(f"Title: '{doc.title}' | Description: {doc.describe()}")
    
# ==========================================
# Part C - Duck Typing
# ==========================================

# 1. Create two unrelated classes (no shared base class or inheritance)
class Printer:
# 2. Add display_status() method
    def display_status(self):
        return "Status: Online - Ink level 85%, Paper tray loaded."
class Screen:
    def display_status(self):
        return "Printer Status: Active - Resolution 1920x1080, Brightness 75%."
devices =[Printer(),Screen()]

print("--- Part C: Duck Typing ---")
for device in devices:
    print(device.display_status())

# ==========================================
# Part D - isinstance()
# ==========================================
class User:
    pass
class AdminUser(User):
    pass
admin = AdminUser()
print("--- Part D: isinstance() ---")
is_admin = isinstance(admin,AdminUser)
is_user =  isinstance(admin, User)
is_string = isinstance(admin,str)
print(f"Is instance of AdminUser? {is_admin}")
print(f"Is instance of admin? {is_user}")
print(f"Is instance of str? {is_string}")       
# ==========================================
# Part E -  __str__
# ==========================================
# 1. Create a Product class with name and price
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 3. Add __str__ so printing the Product gives a useful human-readable description
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price} SEK"


# 2. Observe printing before __str__ is defined:
# Without __str__, printing an object outputs its class name and memory address:
# <__main__.Product object at 0x0000022570356F90>
# Python only knows where the object is stored, not what its data represents.

# 4. Create at least three Product objects and print them
p1 = Product("Macbook", 35000)
p2 = Product("Logictech", 3000)
p3 = Product("Mechanical keyboard", 6000)

print("--- Part E: __str__ ---")
print(p1)
print(p2)
print(p3)

# 5. Use str() on one Product object, store the result in a variable and print its type
product_string = str(p2)
print(f"\nString output: {product_string}")
print(f"Type of result: {type(product_string)}")
# ==========================================
# Part F - __str__ with inheritance
# ==========================================

# 1. Base class Account with owner and balance
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # 2. Add __str__ to Account
    def __str__(self):
        return f"Account Owner: {self.owner} | Balance: {self.balance} SEK"


# 3. Subclass SavingsAccount inheriting from Account
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    # 4. Override __str__ to include the interest rate
    def __str__(self):
        return f"{super().__str__()} | Interest Rate: {self.interest_rate:.1%}"


# 5. Create and print both objects inside a loop
account_1 = Account("Sambath", 25000)
savings_account_1 = SavingsAccount("Mohana", 30000, 0.035)

for account in [account_1, savings_account_1]:
    print(account)
# ==========================================
# Part G - Inheritance or composition?
# ==========================================

# 1. Create CPU with a model attribute
class CPU:
    def __init__(self, model):
        self.model = model


# 2. Create Computer with brand and a CPU object (Composition)
class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu  # Computer HAS-A CPU object inside it


# 3. Create a CPU object and pass it to a Computer object
cpu_1 = CPU("Intel Core i7 processor")
computer_c = Computer("Apple Macbook Pro", cpu_1)

# 4. Print the computer brand and CPU model through the Computer object
print(f"Computer Brand: {computer_c.brand}")
print(f"CPU Model:      {computer_c.cpu.model}")

# ==========================================
# 5. Explanation: HAS-A vs IS-A
# ==========================================
"""
EXPLANATION:
"Computer HAS-A CPU" makes more sense than "Computer IS-A CPU" because a computer 
is a complex system made up of smaller components (CPU, RAM, Hard Drive), one of 
which is a processor. 

If we used inheritance ("Computer IS-A CPU"), a Computer would be forced to inherit 
all properties and behaviour of a CPU directly, implying a Computer is simply a specialised 
type of processor. In reality, a CPU is just a part inside a computer, which is the 
definition of Composition (HAS-A).
"""

# ==========================================
# 6. Inheritance (IS-A) vs Composition (HAS-A) Pairs
# ==========================================
"""
1. Car / Engine    -> Composition (HAS-A)
   A Car is not a type of Engine; a Car HAS-AN Engine as a component.

2. Manager / Employee -> Inheritance (IS-A)
   A Manager IS-AN Employee with extra permissions and specialized duties.

3. Course / Teacher  -> Composition (HAS-A)
   A Course is not a type of Teacher; a Course HAS-A Teacher assigned to teach it.

4. Phone / Device   -> Inheritance (IS-A)
   A Phone IS-A specialized type of Device (it inherits general electronic device traits).
"""
