import pandas as pd

# Show all rows
pd.set_option('display.max_rows', None)

# Show all columns (no horizontal truncation)
pd.set_option('display.max_columns', None)

# Show complete text inside cells without truncating with '...'
pd.set_option('display.max_colwidth', None)

# Prevent auto-wrapping onto new lines for wide tables
pd.set_option('display.width', 1000)

# Load dataset
dataset = pd.read_csv('messy_dataset.csv')

print("MESSY DATASET:")
print(dataset)

print("""
1. Drop rows with missing values
2. Drop columns with missing values
3. Replace missing values
""")

option = int(input("Enter your option: "))

match option:
    case 1:
        # Drop rows where at least one element is missing
        cleaned_dataset = dataset.dropna()
        print("\nCLEANED DATASET (ROWS DROPPED):")
        print(cleaned_dataset)

    case 2:
        # Drop columns where at least one element is missing (axis=1)
        cleaned_dataset = dataset.dropna(axis=1)
        print("\nCLEANED DATASET (COLUMNS DROPPED):")
        print(cleaned_dataset)

    case 3:
        # Option A: Replace missing values across all columns with a default scalar
        # cleaned_dataset = dataset.fillna("Unknown / Missing")

        # Option B: Replace missing values per column type (recommended for practice)
        cleaned_dataset = dataset.copy()

        # Fill missing text fields with placeholders
        cleaned_dataset['Customer_Name'] = cleaned_dataset['Customer_Name'].fillna('Unknown')
        cleaned_dataset['Category'] = cleaned_dataset['Category'].fillna('Uncategorized')

        # Fill missing numeric fields with median/mean or default value (e.g., 1)
        cleaned_dataset['Quantity'] = cleaned_dataset['Quantity'].fillna(cleaned_dataset['Quantity'].median())

        print("\nCLEANED DATASET (MISSING VALUES REPLACED):")
        print(cleaned_dataset)

    case _:
        print("\nInvalid option selected! Please enter 1, 2, or 3.")