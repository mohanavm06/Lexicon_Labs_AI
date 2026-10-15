# Mohana Muruganandham
# Lesson Eight 
# Lab 8
# # Python och AI

# # Part A - Mutable default arguments
# # 1. Create a BadTeam class with name and a default parameter members=[]. Add an add_member()
# # method.
# # 2. Create two BadTeam objects without providing a members list. Add a member to only one team and
# # print both lists. Explain in a comment what happened.
# # 3. Create a corrected Team class using None as the default value and create a new list inside __init__.
# # 4. Repeat the test with two Team objects and show that each object now has its own list.


# class BadTeam:
#     def __init__(self, name, members=[]):
#         self.name = name
#         self.members = members

#     def add_member(self, name):
#         self.members.append(name)


# team_bad = BadTeam("Bad Developing")
# team_evil = BadTeam("Evil Developing")

# team_bad.add_member("Ada Lovelace")

# print(team_bad.members)
# print(team_evil.members)  # Both instances refer to the same list object

# # Correct version
# class Team:
#     def __init__(self, name, members=None):
#         self.name = name
#         self.members = members if members is not None else []

#     def add_member(self, member):
#         self.members.append(member)


# # Part B - Dictionary or class?
# # 1. Represent a movie using a dictionary with title, director and rating.
# # 2. Represent the same information using a Movie class.
# # 3. Add a method to Movie that returns whether the movie is highly rated. Choose a sensible rating
# # threshold.
# # 4. In comments, briefly explain one situation where you would choose a dictionary and one where you
# # would choose a class.

# movie_dict = {
#     "title": "Inception",
#     "director": "Christopher Nolan",
#     "rating": 8.8,
# }

# movie_dict = {
#     "title": "Inception",
#     "director": "Christopher Nolan",
#     "rating": 8.8,
# }


# class Movie:
#     def __init__(self, title, director, rating):
#         self.title = title
#         self.director = director
#         self.rating = rating

#     def is_highly_rated(self):
#         return self.rating >= 8.0


# movie_obj = Movie("Inception", "Christopher Nolan", 8.8)

# print(movie_dict["title"], movie_dict["rating"])
# print(movie_obj.title, movie_obj.rating)
# print(movie_obj.is_highly_rated())  # True

# # Choose class: when the data has behavior or many objects of the same kind
# # are needed, e.g. a movie catalog where every movie has the same fields and methods.

# Part C - Inheritance fundamentals
# 1. Create a base class Account with owner and balance.
# 2. Create SavingsAccount(Account) with an additional interest_rate attribute.
# 3. Use super() so SavingsAccount reuses the initialization from Account.
# 4. Create at least two objects and print their attributes.
# 5. Write the "is-a" statement that explains why this inheritance relationship makes sense.


class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, owner, balance=0.0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


acc = Account("Sam", 1500)
sav = SavingsAccount("Mohana", 50000, 0.03)

print(f"Account: {acc.owner}, balance {acc.balance}")
print(
    f"SavingsAccount: {sav.owner}, balance {sav.balance}, rate {sav.interest_rate:.1%}"
)


# ==============================================================================
# PART D: INHERITED AND SUBCLASS-SPECIFIC BEHAVIOUR
# ==============================================================================

# D1: Base class
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"Employee Name: {self.name}"

# D2: Developer subclass with specific method
class Developer(Employee):
    def write_code(self):
        return f"{self.name} is writing Python code."

# D3: Manager subclass with specific method
class Manager(Employee):
    def approve_leave(self, employee_name):
        return f"Manager {self.name} approved leave for {employee_name}."

# Demonstration D4 & D5
print("=== PART D: Inherited and Subclass-Specific Behaviour ===")
dev = Developer("Alice")
mgr = Manager("Bob")
emp = Employee("Charlie")

# D4: Demonstrate both subclasses can use inherited behaviour from Employee
print(dev.get_information())  # Inherited
print(mgr.get_information())  # Inherited

# Demonstrate subclass-specific methods
print(dev.write_code())
print(mgr.approve_leave("Alice"))

# D5: Demonstrate an Employee object CANNOT use a subclass-specific method
try:
    emp.write_code()  # Will fail because Employee does not have write_code
except AttributeError as e:
    print(f"Expected Error: {e}")
print()


# ==============================================================================
# PART E: super() AND SHARED INITIALIZATION
# ==============================================================================

# E1 & E2: Base class Device with shared initialization & validation
class Device:
    def __init__(self, brand, year):
        if year < 0:
            raise ValueError("Year cannot be negative.")
        self.brand = brand
        self.year = year
        self.is_active = True  # Shared attribute

# E3: Laptop subclass using super()
class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb

# E4: Smartphone subclass using super()
class Smartphone(Device):
    def __init__(self, brand, year, screen_size_inches):
        super().__init__(brand, year)
        self.screen_size_inches = screen_size_inches

# Demonstration E5
print("=== PART E: super() and Shared Initialization ===")
laptop = Laptop("Dell", 2024, 16)
phone = Smartphone("Apple", 2023, 6.1)

# E5: Both receive shared initialization (is_active=True) without code duplication
print(f"Laptop: {laptop.brand}, {laptop.ram_gb}GB RAM, Active: {laptop.is_active}")
print(f"Phone: {phone.brand}, {phone.screen_size_inches}\", Active: {phone.is_active}")

# Demonstration of shared validation catching errors
try:
    invalid_device = Laptop("BadBrand", -2020, 8)
except ValueError as e:
    print(f"Validation caught error in subclass: {e}")
print()


# ==============================================================================
# PART F: METHOD OVERRIDING
# ==============================================================================

# F1: Base Notification class
class Notification:
    def send(self):
        return "Sending a general notification..."

# F2 & F3: Subclasses overriding send()
class EmailNotification(Notification):
    def send(self):
        return "Sending an EMAIL notification with subject and body."

class SMSNotification(Notification):
    def send(self):
        return "Sending an SMS text message."

# Demonstration F4 & Explanation F5
print("=== PART F: Method Overriding ===")
base_notif = Notification()
email_notif = EmailNotification()
sms_notif = SMSNotification()

# F4: Call send() on all objects
print(base_notif.send())
print(email_notif.send())
print(sms_notif.send())

# F5 Explanation:
# - base_notif.send() calls Notification.send() because base_notif is an instance of Notification.
# - email_notif.send() calls EmailNotification.send() because EmailNotification overrides the send method.
# - sms_notif.send() calls SMSNotification.send() because SMSNotification provides its own send implementation.
print()


# ==============================================================================
# PART G: OVERRIDE AND STILL USE THE BASE METHOD
# ==============================================================================

# G1: Base class Report
class Report:
    def get_summary(self):
        return "Report Header: Quarterly Overview."

# G2 & G3: SalesReport overriding and using super().get_summary()
class SalesReport(Report):
    def __init__(self, total_sales):
        self.total_sales = total_sales

    def get_summary(self):
        # Call base implementation using super() and append custom info
        base_summary = super().get_summary()
        return f"{base_summary} Total Sales Revenue: ${self.total_sales:,.2f}"

# Demonstration G4
print("=== PART G: Override and Use Base Method ===")
sales_rep = SalesReport(150000)
print(sales_rep.get_summary())
print()


# ==============================================================================
# PART H: APPLIED CHALLENGE - USER ACCOUNTS
# ==============================================================================

# H10: "IS-A" Relationship Explanation (in comments):
# AdminUser and PremiumUser have an "is-a" relationship with User because:
# 1. An AdminUser IS A User with administrative privileges (it shares core attributes like username and email).
# 2. A PremiumUser IS A User with premium membership features.
# Inheriting from User means both subclasses represent specialized types of a User.

# H2: Base User Class
class User:
    def __init__(self, username, email):
        # H9: Validation using ValueError
        if "@" not in email:
            raise ValueError(f"Invalid email address: '{email}'. Must contain '@'.")
        self.username = username
        self.email = email

    # H3: Common inherited method
    def get_account_info(self):
        return f"User: {self.username} | Email: {self.email}"

    # H6: Base method to be overridden in subclasses
    def get_dashboard(self):
        return "Standard User Dashboard: View Public Profile, View Content."


# H4: Subclass AdminUser
class AdminUser(User):
    def __init__(self, username, email, admin_level):
        # H5: Use super() for initialization
        super().__init__(username, email)
        self.admin_level = admin_level

    # H4: Subclass-specific method
    def delete_user_account(self, target_username):
        return f"Admin [{self.username}] deleted user account: {target_username}"

    # H6 & H7: Overridden method using super() to extend base behavior
    def get_dashboard(self):
        base_dash = super().get_dashboard()
        return f"{base_dash} | ADMIN PANEL (Level {self.admin_level}): Manage Users, View System Logs."


# H4: Subclass PremiumUser
class PremiumUser(User):
    def __init__(self, username, email, subscription_plan):
        # H5: Use super() for initialization
        super().__init__(username, email)
        self.subscription_plan = subscription_plan

    # H4: Subclass-specific method
    def download_4k_video(self, title):
        return f"Downloading '{title}' in 4K HDR for {self.subscription_plan} member."

    # H6: Complete override of base method
    def get_dashboard(self):
        return f"VIP Premium Dashboard ({self.subscription_plan}): Ad-Free Media Player, Priority Support, Offline Downloads."


# Demonstration H8 & H9
print("=== PART H: Applied Challenge - User Accounts ===")

# Create instances
user1 = User("johndoe", "john@example.com")
admin1 = AdminUser("sysadmin", "admin@company.com", admin_level=1)
premium1 = PremiumUser("sarah_g", "sarah@example.com", subscription_plan="Platinum")

# H8: Demonstrate inherited methods
print("--- Inherited Methods ---")
print(user1.get_account_info())
print(admin1.get_account_info())
print(premium1.get_account_info())
print()

# H8: Demonstrate subclass-specific methods
print("--- Subclass-Specific Methods ---")
print(admin1.delete_user_account("spambot99"))
print(premium1.download_4k_video("Planet Earth III"))
print()

# H8: Demonstrate overridden methods
print("--- Overridden Methods ---")
print("User Dashboard:   ", user1.get_dashboard())
print("Admin Dashboard:  ", admin1.get_dashboard())
print("Premium Dashboard:", premium1.get_dashboard())
print()

# H9: Demonstrate ValueError validation
print("--- Validation Error Test ---")
try:
    bad_user = User("invalid_user", "not_an_email_at_all")
except ValueError as e:
    print(f"Validation caught error: {e}")

