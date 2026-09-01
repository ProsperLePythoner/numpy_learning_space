import pandas as pd
import json

# Read JSON file directly
with open('creative_fantasy_data.json', 'r') as f:
    raw_data = json.load(f) # a dictionary

df_raw = pd.Series(raw_data)
print(df_raw)