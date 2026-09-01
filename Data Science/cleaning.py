import pandas as pd

dataset = pd.read_csv('messy_dataset.csv')
print("Messy dataset:".upper())
print(dataset)

cleaned_dataset = dataset.dropna(inplace=True) # Actually change the original dataset ( clean it )
print("\nCleaned dataset:".upper())
print(cleaned_dataset)
