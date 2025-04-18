import pandas as pd

# Load datasets
restaurants_df = pd.read_csv('restaurants.csv')
orders_df = pd.read_csv('orders.csv')

# Merge datasets on restaurant_id
combined_df = pd.merge(orders_df, restaurants_df, on='restaurant_id', how='inner')

# Extract and engineer features
combined_df['order_hour'] = combined_df['order_acknowledged_at'].dt.hour
combined_df['order_day_of_week'] = combined_df['order_acknowledged_at'].dt.dayofweek
combined_df = pd.get_dummies(combined_df, columns=['type_of_food', 'city', 'country'], drop_first=True)