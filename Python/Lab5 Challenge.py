
# Mohana Muruganandham
# # Lesson Five Challenge
# # Python och AI

# Lab 5  Challenge

# ==========================================
# PART 1: PRODUCTS AND CUSTOMERS DATA
# ==========================================

# 1. Product Catalog (8 products)
# Structured as a dictionary where the key is the Product ID
# and the value is a dictionary of product attributes.
products = {
    "P101": {"name": "Wireless Mouse", "price": 25.99, "category": "Electronics"},
    "P102": {"name": "Mechanical Keyboard", "price": 89.50, "category": "Electronics"},
    "P103": {"name": "USB-C Cable (2m)", "price": 12.99, "category": "Accessories"},
    "P104": {"name": "Stainless Water Bottle", "price": 18.00, "category": "Lifestyle"},
    "P105": {"name": "Noise Cancelling Headphones", "price": 199.99, "category": "Electronics"},
    "P106": {"name": "Notebook & Pen Set", "price": 14.50, "category": "Office"},
    "P107": {"name": "Desk Mat (Large)", "price": 22.00, "category": "Office"},
    "P108": {"name": "Portable Power Bank 10k", "price": 34.99, "category": "Electronics"}
}

# 2. Customer Database (5 customers)
# Structured as a dictionary where the key is the Customer ID.
customers = {
    "C001": {"name": "Alice Smith", "email": "alice@example.com"},
    "C002": {"name": "Bob Jones", "email": "bob.j@example.com"},
    "C003": {"name": "Charlie Brown", "email": "charlie@example.com"},
    "C004": {"name": "Diana Prince", "email": "diana@example.com"},
    "C005": {"name": "Evan Wright", "email": "ewright@example.com"}
}


# Optional helper functions to display the data clearly
def display_catalog():
    print("=== PRODUCT CATALOG ===")
    for pid, details in products.items():
        print(f"[{pid}] {details['name']} - ${details['price']:.2f} ({details['category']})")
    print()

def display_customers():
    print("=== REGISTERED CUSTOMERS ===")
    for cid, details in customers.items():
        print(f"[{cid}] {details['name']} - {details['email']}")
    print()


if __name__ == "__main__":
    display_catalog()
    display_customers()

# ==============================================================================
# GLOBAL DATA & CONFIGURATION
# ==============================================================================

# Global configuration variables (Part 7)
STORE_NAME = "Tech & Living Store"
TAX_RATE = 0.25  # 25% VAT
total_daily_revenue = 0.0  # Used to demonstrate global scope modification (Part 7)

# Existing customer & product data (Part 1 baseline data for unpacking)
customers = {
    "C001": {"name": "Alice Smith", "email": "alice@example.com"},
    "C002": {"name": "Bob Jones", "email": "bob.j@example.com"},
    "C003": {"name": "Charlie Brown", "email": "charlie@example.com"},
    "C004": {"name": "Diana Prince", "email": "diana@example.com"},
    "C005": {"name": "Evan Wright", "email": "ewright@example.com"}
}

products = {
    "P101": {"name": "Wireless Mouse", "price": 25.99, "category": "Electronics"},
    "P102": {"name": "Mechanical Keyboard", "price": 89.50, "category": "Electronics"},
    "P103": {"name": "USB-C Cable (2m)", "price": 12.99, "category": "Accessories"},
    "P104": {"name": "Stainless Water Bottle", "price": 18.00, "category": "Lifestyle"},
    "P105": {"name": "Noise Cancelling Headphones", "price": 199.99, "category": "Electronics"},
    "P106": {"name": "Notebook & Pen Set", "price": 14.50, "category": "Office"},
    "P107": {"name": "Desk Mat (Large)", "price": 22.00, "category": "Office"},
    "P108": {"name": "Portable Power Bank 10k", "price": 34.99, "category": "Electronics"}
}


# ==============================================================================
# PART 7: SCOPE DEMONSTRATION & HELPER FUNCTIONS
# ==============================================================================

# 1. Reading global variables from inside a function
def print_store_header():
    # Demonstrates reading global STORE_NAME without modification
    print(f"==========================================")
    print(f"      WELCOME TO {STORE_NAME.upper()}")
    print(f"==========================================")

# 2. Local variable shadow vs Global variable
def scope_demonstration():
    # Local variable with the same name as global TAX_RATE
    TAX_RATE = 0.10  # Local shadowing
    print(f"[Scope Demo] Local TAX_RATE inside function: {TAX_RATE}")

# 3. Bad global mutation vs Pure Return pattern
# BAD PRACTICE (DO NOT USE IN PRODUCTION):
# def add_to_revenue_bad(amount):
#     global total_daily_revenue
#     total_daily_revenue += amount

# PREFERABLE APPROACH: Pure function returning new calculated value.
# Reason: Pure functions are deterministic, easier to unit test, and prevent bugs 
# caused by unexpected side effects across large codebases.
def update_revenue(current_revenue, order_total):
    """Calculates updated revenue and returns it to be assigned explicitly outside."""
    return current_revenue + order_total

# 4. Enclosing Scope Demonstration (Nested Function)
def create_discount_calculator(discount_percent):
    """Outer function defining an enclosing scope variable."""
    rate = discount_percent / 100.0
    
    def apply_discount(amount):
        """Inner function accessing 'rate' from enclosing scope."""
        return amount * (1.0 - rate)
    
    return apply_discount


# ==============================================================================
# PART 8 & 9: ORDER PROCESSING ENGINE
# ==============================================================================

def process_order(customer_id, *product_ids, express=False, discount_percent=0.0, **custom_settings):
    """
    Processes an order for a customer given a variable number of product IDs.
    
    Parameters:
    - customer_id: Required explicit string ID.
    - *product_ids: Variable positional arguments for flexible product list.
    - express: Keyword-only boolean flag for shipping calculation.
    - discount_percent: Keyword-only float (0 to 100).
    - **custom_settings: Optional keyword settings (e.g., gift_wrap, promo_code).
    """
    if customer_id not in customers:
        raise ValueError(f"Customer ID '{customer_id}' not found.")
    
    if not product_ids:
        raise ValueError("An order must contain at least one product ID.")

    customer_info = customers[customer_id]
    ordered_items = []
    subtotal = 0.0

    for pid in product_ids:
        if pid not in products:
            raise ValueError(f"Product ID '{pid}' not found.")
        prod = products[pid]
        ordered_items.append(prod)
        subtotal += prod["price"]

    # Calculate discount using closure (Part 7 concept)
    calc_discount = create_discount_calculator(discount_percent)
    discounted_subtotal = calc_discount(subtotal)
    discount_amount = subtotal - discounted_subtotal

    # Calculate shipping
    shipping_cost = 15.00 if express else (0.0 if discounted_subtotal >= 100.0 else 5.00)

    # Tax calculation using global tax rate
    tax_amount = discounted_subtotal * TAX_RATE
    final_total = discounted_subtotal + shipping_cost + tax_amount

    return {
        "customer": customer_info,
        "items": ordered_items,
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "shipping_cost": shipping_cost,
        "tax_amount": tax_amount,
        "final_total": final_total,
        "is_express": express,
        "settings": custom_settings
    }


# ==============================================================================
# PART 6: FLEXIBLE ORDER SUMMARY
# ==============================================================================

def order_summary(order_id, customer_name, *notes, **metadata):
    """
    Generates a flexible, readable multi-line summary for an order.
    
    Parameters:
    - order_id: Explicit string ID.
    - customer_name: Explicit string customer name.
    - *notes: Flexible positional notes/messages.
    - **metadata: Flexible key-value pairs (priority, campaign, etc.).
    """
    lines = [
        f"--- ORDER SUMMARY [{order_id}] ---",
        f"Customer: {customer_name}"
    ]

    if notes:
        lines.append("Notes & Instructions:")
        for note in notes:
            lines.append(f"  - {note}")

    if metadata:
        lines.append("Order Metadata:")
        for key, val in metadata.items():
            formatted_key = key.replace("_", " ").title()
            lines.append(f"  * {formatted_key}: {val}")

    return "\n".join(lines)


# ==============================================================================
# PART 5: UNPACKING EXISTING DATA DEMONSTRATION
# ==============================================================================

def register_customer_profile(name, email, city="Stockholm", member_status="Standard"):
    """Target function for unpacking demonstrations."""
    return f"Profile Created: {name} ({email}) | Location: {city} | Tier: {member_status}"

def demonstrate_unpacking():
    print("\n=== PART 5: DATA UNPACKING DEMONSTRATIONS ===")

    # 1. Positional Unpacking (*list / *tuple) - Example 1: Function arguments
    cust_tuple = ("Greta Thunberg", "greta@example.com")
    print("Positional Unpacking 1:", register_customer_profile(*cust_tuple))

    # 2. Positional Unpacking (*list / *tuple) - Example 2: Calling process_order with a list of products
    cart_items = ["P101", "P103", "P106"]
    order_res = process_order("C001", *cart_items)
    print(f"Positional Unpacking 2: Processed {len(order_res['items'])} items using *cart_items.")

    # 3. Dictionary Unpacking (**dict) - Example 1: Target function kwargs
    cust_dict = {
        "name": "Lars Lindqvist",
        "email": "lars@example.com",
        "city": "Gothenburg",
        "member_status": "VIP"
    }
    print("Dictionary Unpacking 1:", register_customer_profile(**cust_dict))

    # 4. Dictionary Unpacking (**dict) - Example 2: Calling process_order with configuration dictionary
    order_config = {
        "express": True,
        "discount_percent": 15.0,
        "gift_wrap": True,
        "gift_message": "Happy Birthday!"
    }
    # Complete dictionary unpacking containing all keyword arguments
    order_res_2 = process_order("C002", "P105", **order_config)
    print(f"Dictionary Unpacking 2: Processed express order total: ${order_res_2['final_total']:.2f}")


# ==============================================================================
# FINAL CHALLENGE: DAILY ORDER REPORT GENERATOR
# ==============================================================================

def generate_report_data(title, *sections, **metadata):
    """Creates a structured dictionary representation of the report."""
    return {
        "title": title,
        "sections": list(sections),
        "metadata": metadata
    }

def format_report_to_string(report_dict):
    """Converts a structured report dictionary into a formatted multi-line string."""
    lines = [
        "==========================================",
        f" REPORT: {report_dict['title'].upper()}",
        "=========================================="
    ]

    if report_dict["metadata"]:
        lines.append("METADATA:")
        for k, v in report_dict["metadata"].items():
            lines.append(f"  • {k.replace('_', ' ').title()}: {v}")
        lines.append("------------------------------------------")

    for section in report_dict["sections"]:
        lines.append(f"\n[{section['heading'].upper()}]")
        for key, val in section["content"].items():
            lines.append(f"  {key}: {val}")

    lines.append("\n==========================================")
    return "\n".join(lines)


# ==============================================================================
# MAIN EXECUTION & TESTING FLOW
# ==============================================================================

if __name__ == "__main__":
    print_store_header()

    # Scope Demonstration
    scope_demonstration()

    # Run Unpacking Demos
    demonstrate_unpacking()

    print("\n=== PART 9: PROCESSING DIFFERENT ORDER TYPES ===")
    
    processed_orders = []

    # Order 1: One product, standard delivery, no discount
    o1 = process_order("C001", "P101")
    
    # Order 2: Several products, standard delivery, no discount
    o2 = process_order("C002", "P102", "P103", "P104")
    
    # Order 3: Order with discount (10%)
    o3 = process_order("C003", "P105", discount_percent=10.0)
    
    # Order 4: Express order
    o4 = process_order("C004", "P107", express=True)
    
    # Order 5: Order with extra metadata & settings
    o5 = process_order("C005", "P108", "P106", express=True, discount_percent=5.0, wrap="Gift Box", card=True)

    all_orders = [o1, o2, o3, o4, o5]

    # Demonstrate Order Summaries (Part 6) & Revenue Updates (Part 7)
    for idx, ord_data in enumerate(all_orders, start=101):
        ord_id = f"ORD-{idx}"
        
        # Updating global revenue state safely using pure function return values
        total_daily_revenue = update_revenue(total_daily_revenue, ord_data["final_total"])
        
        # Sample notes demonstration
        summary_text = order_summary(
            ord_id,
            ord_data["customer"]["name"],
            "Fragile packaging required" if ord_data["is_express"] else "Standard drop-off",
            "Customer opted for tracking",
            shipping_method="Express Air" if ord_data["is_express"] else "Ground Courier",
            items_count=len(ord_data["items"])
        )
        print(f"\n{summary_text}")
        print(f"Final Total: ${ord_data['final_total']:.2f}")

    # ==========================================================================
    # DAILY REPORT GENERATION
    # ==========================================================================
    print("\n=== FINAL CHALLENGE: DAILY REPORT ===")

    # Calculate Report Statistics
    num_orders = len(all_orders)
    totals = [o["final_total"] for o in all_orders]
    avg_order_val = total_daily_revenue / num_orders if num_orders > 0 else 0
    max_order_val = max(totals)
    min_order_val = min(totals)

    # Two additional custom statistics
    express_orders_count = sum(1 for o in all_orders if o["is_express"])
    total_items_sold = sum(len(o["items"]) for o in all_orders)

    # Build report sections
    sec_summary = {
        "heading": "Order Overview",
        "content": {
            "Total Processed Orders": num_orders,
            "Total Revenue": f"${total_daily_revenue:.2f}",
            "Average Order Value": f"${avg_order_val:.2f}"
        }
    }

    sec_extrema = {
        "heading": "Order Extremes",
        "content": {
            "Largest Order Value": f"${max_order_val:.2f}",
            "Smallest Order Value": f"${min_order_val:.2f}"
        }
    }

    sec_custom = {
        "heading": "Additional Insights",
        "content": {
            "Total Items Sold": total_items_sold,
            "Express Shipping Ratio": f"{express_orders_count}/{num_orders} ({express_orders_count/num_orders*100:.0f}%)"
        }
    }

    # Generate structured report data
    report_dict = generate_report_data(
        "Daily E-Commerce Operations Report",
        sec_summary,
        sec_extrema,
        sec_custom,
        generated_by="Automated Order System",
        department="Logistics & Sales",
        date="2026-09-23",
        version="1.4.0",
        confidential=True
    )

    # Print formatted report
    print(format_report_to_string(report_dict))


==============================================================================
LAB 5 CHALLENGE: DESIGN REFLECTIONS
==============================================================================

1. CHOICE 1: process_order(customer_id, *product_ids, express=False, discount_percent=0.0, **custom_settings)
   • Choice: Explicit parameter for 'customer_id', *args for 'product_ids', named keyword defaults for flags, and **kwargs for extra settings.
   • Alternative Considered: Accepting a single list parameter for products: process_order(customer_id, product_id_list, ...).
   • Justification: Using *product_ids allows calling the function naturally with positional items 
   (e.g., process_order("C1", "P1", "P2")) while still supporting positional unpacking (*cart_items) when a list already exists.

2. CHOICE 2: order_summary(order_id, customer_name, *notes, **metadata)
   • Choice: Explicit parameters for required identifying fields (order_id, customer_name), *args for notes, and **kwargs for flexible metadata.
   • Alternative Considered: Passing a single dictionary containing all summary details.
   • Justification: Explicit required fields prevent generating malformed summaries missing critical IDs, while *notes and **metadata keep notes and tags readable without creating rigid dictionary keys.

3. CHOICE 3: update_revenue(current_revenue, order_total)
   • Choice: Explicit normal parameters returning a new float value.
   • Alternative Considered: Using 'global total_daily_revenue' inside the function to mutate state directly.
   • Justification: Returning values explicitly makes functions pure, prevents unintended global side effects, and makes testing and debugging predictable.

4. POOR USE CASE FOR *args / **kwargs (IDENTIFIED PLACE TO AVOID):
   • Example: register_customer_profile(name, email) or create_discount_calculator(discount_percent).
   • Explanation: If register_customer_profile used **kwargs (e.g., def register_customer_profile(**details)), callers wouldn't know which fields are mandatory 
   (like 'name' or 'email') without checking internal code. Explicit named parameters provide self-documentation, 
   IDE autocomplete support, and immediate syntax errors when required arguments are omitted.
"""

