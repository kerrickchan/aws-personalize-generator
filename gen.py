import uuid
import pandas as pd
import random
import time

# Generate a list of 1000 unique item UUIDs to simulate item pool
item_ids = [str(uuid.uuid4()) for _ in range(1000)]

# Generate a list of 1000 unique user UUIDs to simulate user pool
user_ids = [str(uuid.uuid4()) for _ in range(1000)]

# Define sample categories and event types for demonstration
categories = ['Electronics', 'Books', 'Clothing', 'Home & Garden', 'Toys']
event_types = ['purchase', 'view']

# Generate a list of dictionaries for each user-item interaction
interactions = [
    {
        "USER_ID": random.choice(user_ids),
        "ITEM_ID": random.choice(item_ids),
        "TIMESTAMP": int(time.time()),  # Current Unix timestamp
        "EVENT_TYPE": random.choice(event_types)
    }
    for _ in range(50000)
]

# Generate item details for the items DataFrame
items = [
    {
        "ITEM_ID": item_id,
        "PRICE": round(random.uniform(5.0, 500.0), 2),  # Random price between $5 and $500
        "CATEGORY_L1": random.choice(categories)
    }
    for item_id in item_ids
]

# Create DataFrames
user_item_interactions_df = pd.DataFrame(interactions)
users_df = pd.DataFrame(user_ids, columns=["USER_ID"])
items_df = pd.DataFrame(items)

# Save the DataFrames to CSV files
user_item_interactions_df.to_csv('user_item_interactions.csv', index=False)
users_df.to_csv('users.csv', index=False)
items_df.to_csv('items.csv', index=False)

# Output to console
print(f'{len(interactions)} user-item interactions have been saved to user_item_interactions.csv')
print(f'{len(users_df)} unique users have been saved to users.csv')
print(f'{len(items_df)} items have been saved to items.csv')