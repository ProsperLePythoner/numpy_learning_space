import pandas as pd

data = {
    'Name': ['Ramon', 'Rebecca', 'Pfund'],
    'Age': [20, 18, 60],
    'Gender': ['Male', 'Female', 'Male'],
}

df = pd.DataFrame(data)
print("DataFrame output...")
print(df)

# Create a simple pandas series
fruits = ['apple', 'banana', 'orange', 'cherry']
my_var = pd.Series(fruits)
print("\nSeries output...")
print(my_var)