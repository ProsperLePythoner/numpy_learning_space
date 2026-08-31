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
print()
print(my_var[3])

# Label the fruits using the index argument
labels = []
for fruit in fruits:
    label = input(f"Label for fruit {fruit}: ")
    labels.append(label)
labelled_fruits = pd.Series(fruits, index=labels)
print()
print(labelled_fruits)