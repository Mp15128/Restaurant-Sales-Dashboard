import csv
import random
from datetime import datetime, timedelta

# 1. Variables & Lists (Day 3 Concept)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
payment_methods = ["Card", "Cash", "UPI"]
order_types = ["Dine In", "Delivery", "Takeaway"]

# Menu items mapped to their (Category, Price)
menu = {
    "Pepperoni Pizza": ("Pizza", 18),
    "Margherita Pizza": ("Pizza", 15),
    "BBQ Chicken Pizza": ("Pizza", 19),
    "Veggie Supreme Pizza": ("Pizza", 17),
    "Garlic Bread": ("Drinks & Sides", 6),
    "Chicken Wings": ("Drinks & Sides", 9),
    "Mozzarella Sticks": ("Drinks & Sides", 7),
    "Chocolate Lava Cake": ("Dessert", 8),
    "Apple Pie": ("Dessert", 6),
    "Coca Cola": ("Drinks & Sides", 3),
    "Iced Tea": ("Drinks & Sides", 3)
}

# 2. Setup timing parameters (Full Year of 2026)
start_date = datetime(2026, 1, 1)
total_orders = 1000

# 3. Create and populate the CSV file
with open("data/restaurant_sales.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Writing the Header Column (Day 2 Schema)
    writer.writerow(["OrderID", "Date", "CustomerID", "City", "Category", "ItemName", "Quantity", "Price", "Total", "Payment", "OrderType", "Rating"])
    
    # 4. The Loop (Day 3 Concept: Generating 1,000 orders programmatically)
    for i in range(total_orders):
        order_id = 1001 + i
        
        # Randomly progress dates across the whole year
        days_to_add = int((i / total_orders) * 364)
        current_date = (start_date + timedelta(days=days_to_add)).strftime("%Y-%m-%d")
        
        # Generate customer profiles and order attributes
        customer_id = f"C{random.randint(100, 600):03d}"
        city = random.choice(cities)
        item_name = random.choice(list(menu.keys()))
        category, price = menu[item_name]
        
        quantity = random.randint(1, 4)
        total_amount = quantity * price  # Basic function math
        
        payment = random.choice(payment_methods)
        order_type = random.choice(order_types)
        
        # Give higher weights to better ratings to simulate a popular restaurant
        rating = random.choices([5, 4, 3, 2, 1], weights=[40, 35, 15, 6, 4])[0]
        
        # Write the row
        writer.writerow([order_id, current_date, customer_id, city, category, item_name, quantity, price, total_amount, payment, order_type, rating])

print("Successfully generated data/restaurant_sales.csv with 1,000 records!")
