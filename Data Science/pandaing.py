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

# Create a series from a dictionary
high_scores = {
    'Monday': '1000XP',
    'Tuesday': '7890XP',
    'Wednesday': '2800XP',
    'Thursday': '100800XP',
    'Friday': '400XP',
    'Saturday': '0XP',
    'Sunday': '1740XP',
}
scores = pd.Series(high_scores)
print()
print(f"Printing high scores...\n{scores}")

# Select items from Monday to Wednesday
mon_to_wed = pd.Series(high_scores, index=['Monday', 'Tuesday', 'Wednesday'])
print(f"\nPrinting high scores from Monday to Wednesday...\n{mon_to_wed}")
exit()

# Label the fruits using the index argument
labels = []
for fruit in fruits:
    label = input(f"Label for fruit {fruit}: ")
    labels.append(label)
labelled_fruits = pd.Series(fruits, index=labels)
print()
print(labelled_fruits)
