import pandas as pd

# Load the CSV file
df = pd.read_csv('sample_data.csv')

# Inspect the first few rows
print(df.head())
print()

# Get dataset summary
print(df.info())
print()
print(df.describe())
print()

# Example aggregation: Average salary by department
avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)