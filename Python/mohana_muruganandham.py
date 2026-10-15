# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
total_value = 0
highest_price = 0
highest_product = None

for product in products:
    if product["stock"] > 0:
        print(f"In stock: {product['name']}")

        # Add inventory value
        total_value += product["price"] * product["stock"]

        # Track highest-priced in-stock item
        if product["price"] > highest_price:
            highest_price = product["price"]
            highest_product = product["name"]

print(f"\nTotal inventory value: {total_value}")
print(f"Highest-priced in-stock product: {highest_product}")

Output: In stock: Laptop
In stock: Keyboard
In stock: Monitor
In stock: Webcam

Total inventory value: 67900
Highest-priced in-stock product: Laptop
# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
def calculate_average (score_list):
    return sum(score_list)/len(score_list)

def create_result(score_list):
    avg = calculate_average(score_list)
    if avg >= 70:
        return = "Pass"
        return = "Fail"
# Call create_result() using the scores above.
avg_score = calculate_average(scores)
final_result =create_result(scores)

# Print both the average score and the final result.
print(f"\nAverage Score: {avg_score:.2f}")
print(f"Final Result: {final_result}")
Output:
Average Score: 77.29
Final Result: Pass

# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.

# Write your solution below:
def calculate_order(customer_name, *prices, **settings):
    subtotal = sum(prices)
    final_total = subtotal
    
# Apply discount percentage if present
    if "discount" in settings:
        discount_amount = subtotal * (settings["discount"] / 100)
        final_total -= discount_amount
        
    if "shipping" in settings:
        final_total += settings["shipping"]
        
    return {
        "customer": customer_name,
        "subtotal": subtotal,
        "final_total": final_total,
        "settings": settings
    }

# unpacking for *args and **kwargs
order_summary = calculate_order("Anna", *product_prices, **order_settings)
print(f"\nOrder Summary: {order_summary}")


Output: Order Summary: {'customer': 'Anna', 'subtotal': 1500, 
'final_total': 1399.0, 'settings': {'discount': 10, 'shipping': 49, 'priority': True}}

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
# 1. Normalized player names
normalized_names = [p["name"].strip().title() for p in players]
