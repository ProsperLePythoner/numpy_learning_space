import pandas as pd

characters = {
    'Name': ['Ben Tennyson', 'Bart Simpson', 'Peter Griffin', ''],
    'TV Series': ['Ben 10: Alien Force', 'The Simpsons', 'Family Guy', 'The Amazing World of Gumball'],
}

data = pd.DataFrame(characters)
print(f"RAW DATA:\n{data}")

# Fix the missing character
data.loc[data['TV Series'] == 'The Amazing World of Gumball', 'Name'] = 'Gumball Watterson'
print(f"\n\nCLEANED DATA:\n{data}")

# Add new columns
data['Main Color'] = ['Green', 'Yellow', 'White', 'Blue']
data['Debut Year'] = [2008, 1989, 1999, 2011]
print(f"\n\nDATA WITH ADDED COLUMNS:\n{data}")

# Filter characters whose show started after 2000
modern_shows = data[data['Debut Year'] > 2000]
print(f"\n\nMODERN SHOWS:\n{modern_shows}")

# Try renaming one column
data.rename(columns={'Name': 'Character Name'}, inplace=True)
print(f"\n\nRENAME COLUMN 'Name' to 'Character Name':\n{data}")

# Reindex each row with numbers 1 through 4 instead
data.index = range(1, len(data) + 1)
print(f"\n\nREINDEXED DATA:\n{data}")