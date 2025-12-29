import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# --- CONFIGURATION ---
NUM_CUSTOMERS = 500  
NUM_ORDERS = 2000    
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 12, 31)

# --- DATA LISTS ---
cities = ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Antalya', 'Adana']
categories = {
    'Electronics': [('Headphones', 1500), ('Smart Watch', 2500), ('Laptop', 15000), ('Phone Case', 150)],
    'Clothing': [('T-Shirt', 300), ('Jeans', 800), ('Sneakers', 2000), ('Jacket', 1200)],
    'Home & Living': [('Blender', 1200), ('Coffee Maker', 3500), ('Iron', 2000), ('Lamp', 500)],
    'Beauty': [('Perfume', 900), ('Lipstick', 400), ('Shampoo', 150), ('Moisturizer', 350)]
}
payment_methods = ['Credit Card', 'Bank Transfer', 'Cash on Delivery']
statuses = ['Delivered', 'Delivered', 'Delivered', 'Delivered', 'Cancelled', 'Returned'] 

# --- GENERATOR FUNCTIONS ---
def random_date(start, end):
    """Generate a random datetime between start and end."""
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

# 1. GENERATE CUSTOMERS
print("Generating Customer Data...")
customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        'Customer_ID': i,
        'Name': f'Customer_{i}', 
        'City': random.choice(cities),
        'Join_Date': random_date(datetime(2022, 1, 1), datetime(2023, 1, 1)) 
    })
df_customers = pd.DataFrame(customers)

# 2. GENERATE ORDERS
print("Generating Order Data...")
orders = []
for i in range(1, NUM_ORDERS + 1):
    
    cust = random.choice(customers)
    
    cat_name = random.choice(list(categories.keys()))
    prod_name, base_price = random.choice(categories[cat_name])
    
    final_price = base_price + random.randint(-50, 50) 
    
    order_date = random_date(START_DATE, END_DATE)
    
    if order_date.month == 11:
         pass
         
    orders.append({
        'Order_ID': 1000 + i,
        'Customer_ID': cust['Customer_ID'],
        'Order_Date': order_date,
        'Category': cat_name,
        'Product': prod_name,
        'Quantity': random.choices([1, 2, 3], weights=[70, 20, 10])[0],
        'Unit_Price': final_price,
        'Payment_Method': random.choice(payment_methods),
        'Status': random.choice(statuses) 
    })

df_orders = pd.DataFrame(orders)

# 3. MERGE & SAVE (Creating the Master Dataset)
df_full = pd.merge(df_orders, df_customers, on='Customer_ID', how='left')

# Save to CSV
file_name = 'ecommerce_data.csv'
df_full.to_csv(file_name, index=False)

print(f"✅ SUCCESS: Generated {len(df_full)} rows of data.")
print(f"📁 File saved as: {file_name}")
print("--- PREVIEW ---")
print(df_full.head())
