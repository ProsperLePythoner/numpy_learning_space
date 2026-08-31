import pandas as pd

data = pd.read_csv('sample_data.csv')

# Print the data's head
print(f"Print the first 10 rows:\n{data.head(10)}")
print(f"\nPrint the default head:\n{data.head()}")

# Print the data's tail
print(f"\nPrint the last 20 rows:\n{data.tail(20)}")
print(f"\nPrint the default tail:\n{data.tail()}")

# Print the data's info
print("\nINFO..........")
data.info()

# Describe the data
print("\nDESCRIPTION..........")
print(data.describe())