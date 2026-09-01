import pandas as pd
import json

data = pd.read_csv('messy_dataset.csv')
print(data)

# Calculate the mean and replace any empty values with it
x = data['Quantity'].mean()
data.fillna(value={'Quantity': x}, inplace=True)
print("\nCleaned data".upper())
print(data)

exit()

# Read JSON file directly
with open('creative_fantasy_data.json', 'r') as f:
    raw_data = json.load(f) # a dictionary

df_raw = pd.Series(raw_data)
print(df_raw)