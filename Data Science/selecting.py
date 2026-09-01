import pandas as pd

data = pd.read_csv('sample_data.csv')
filtered = data[data['Age'] > 55]

print(filtered)