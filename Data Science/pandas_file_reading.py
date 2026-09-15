import pandas as pd
from matplotlib import pyplot as plt

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

# Plot a graph
avg_salary.plot(kind='bar', title='Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.show()