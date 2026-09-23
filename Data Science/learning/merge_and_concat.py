import pandas as pd

dataset1 = {
    'Artist': ['Alan Walker', 'Charlie Puth', 'Tobu', 'DJ Snake'],
    'GOAT Level': [1, .5, .7, .8]
}

dataset2 = {
    'Artist': ['Alan Walker', 'Charlie Puth', 'Tobu', 'DJ Snake'],
    'Fav Track': ['Darkside', 'We Don\'t Talk Anymore', 'Cloud 9', 'Let Me Love You']
}

df1 = pd.DataFrame(dataset1)
df2 = pd.DataFrame(dataset2)

# Merge the dataframes
df_merged_inner = pd.merge(df1, df2, on='Artist', how='inner')
df_merged_outer = pd.merge(df1, df2, on='Artist', how='outer')

# Print the output
print(f"INNER MERGED DATA (INTERSECTION OF NAMES):\n{df_merged_inner}")
