
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import uuid

# Initialize Faker
fake = Faker()
Faker.seed(42)
random.seed(42)

# Generate 35 orders
orders = []

# Sample products
products = [
    {"sku": "PROD-001", "name": "Wireless Mouse", "price": 29.99},
    {"sku": "PROD-002", "name": "Mechanical Keyboard", "price": 89.99},
    {"sku": "PROD-003", "name": "USB-C Hub", "price": 49.99},
    {"sku": "PROD-004", "name": "Monitor Stand", "price": 79.99},
    {"sku": "PROD-005", "name": "Webcam HD", "price": 69.99},
    {"sku": "PROD-006", "name": "Laptop Bag", "price": 45.99},
    {"sku": "PROD-007", "name": "Desk Lamp LED", "price": 34.99},
    {"sku": "PROD-008", "name": "Cable Organizer", "price": 15.99},
    {"sku": "PROD-009", "name": "Ergonomic Chair Cushion", "price": 39.99},
    {"sku": "PROD-010", "name": "Bluetooth Speaker", "price": 59.99},
]

# Sample customers
customers = [
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
    {"id": str(uuid.uuid4()), "name": fake.name(), "email": fake.email(), "phone": fake.phone_number()},
]

# Order statuses
statuses = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]
payment_methods = ["Credit Card", "PayPal", "Bank Transfer", "Cash on Delivery"]
warehouses = ["Warehouse A", "Warehouse B", "Warehouse C"]

for i in range(1, 36):
    # Random customer
    customer = random.choice(customers)
    
    # Random product(s) - some orders have multiple items
    num_items = random.randint(1, 3)
    selected_products = random.sample(products, min(num_items, len(products)))
    
    # Calculate quantities and totals
    items = []
    subtotal = 0
    for prod in selected_products:
        qty = random.randint(1, 10)
        item_total = prod["price"] * qty
        subtotal += item_total
        items.append({
            "product_sku": prod["sku"],
            "product_name": prod["name"],
            "quantity": qty,
            "unit_price": prod["price"],
            "line_total": round(item_total, 2)
        })
    
    # Calculate order totals
    tax_rate = random.choice([0.05, 0.10, 0.15, 0.20])
    tax_amount = round(subtotal * tax_rate, 2)
    shipping_cost = random.choice([0, 5.99, 9.99, 15.99])
    total_amount = round(subtotal + tax_amount + shipping_cost, 2)
    
    # Generate dates
    order_date = fake.date_between(start_date='-90d', end_date='today')
    ship_date = order_date + timedelta(days=random.randint(1, 5)) if random.random() > 0.3 else None
    delivery_date = ship_date + timedelta(days=random.randint(2, 7)) if ship_date else None
    
    # Determine status based on dates
    if delivery_date and delivery_date <= datetime.now().date():
        status = "Delivered"
    elif ship_date and ship_date <= datetime.now().date():
        status = random.choice(["Shipped", "Processing"])
    else:
        status = random.choice(["Pending", "Processing"])
    
    order = {
        "order_id": f"ORD-{i:04d}",
        "order_number": f"SO-2026-{i:05d}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "customer_id": customer["id"],
        "customer_name": customer["name"],
        "customer_email": customer["email"],
        "customer_phone": customer["phone"],
        "shipping_address": fake.address().replace('\n', ', '),
        "billing_address": fake.address().replace('\n', ', '),
        "status": status,
        "payment_method": random.choice(payment_methods),
        "payment_status": random.choice(["Paid", "Pending", "Refunded"]) if status != "Cancelled" else "Refunded",
        "warehouse": random.choice(warehouses),
        "subtotal": round(subtotal, 2),
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "shipping_cost": shipping_cost,
        "total_amount": total_amount,
        "currency": "USD",
        "notes": fake.sentence(nb_words=10) if random.random() > 0.5 else "",
        "ship_date": ship_date.strftime("%Y-%m-%d") if ship_date else "",
        "delivery_date": delivery_date.strftime("%Y-%m-%d") if delivery_date else "",
        "tracking_number": f"TRK{random.randint(100000000, 999999999)}" if status in ["Shipped", "Delivered"] else "",
    }
    
    orders.append(order)

# Create DataFrame
df = pd.DataFrame(orders)

# Save to Excel
excel_file = "sample_orders.xlsx"
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f"Successfully generated {len(orders)} orders!")
print(f"\nSample of first 3 orders:")
print(df.head(3).to_string())
print(f"\nFile saved as: {excel_file}")
print(f"\nColumns included:")
for col in df.columns:
    print(f"  - {col}")