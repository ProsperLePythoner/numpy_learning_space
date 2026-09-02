import pandas as pd
import data_formatting # Custom module

# Read raw csv dataset
raw_data = pd.read_csv('shows_dataset.csv')
print(f"RAW DATA:\n{raw_data}")

## 1. GROUPING
# Group the data by genre and network
grouped_by_network = raw_data.groupby('Network')
grouped_by_genre = raw_data.groupby('Genre')

# Check how many network and genre groups were created
print("\n\nDone grouping!")
print(f"Number of network groups: {grouped_by_network.ngroups}")
print(f"Number of genre groups: {grouped_by_genre.ngroups}")

# See which rows belong to Cartoon Network
print(f"\n\nSHOWS BELONGING TO 'Cartoon Network':\n{grouped_by_network.get_group('Cartoon Network')}")

# See which rows are in the Sci-Fi genre
print(f"\n\nSCI-FI SHOWS:\n{grouped_by_genre.get_group('Sci-Fi')}")


## 2. AGGREGATION
# Calculate total viewership (in millions) for each Network [ SINGLE-COLUMN ]
total_network_views = raw_data.groupby('Network')['Views_Millions'].sum()
total_genre_views = raw_data.groupby('Genre')['Views_Millions'].sum()

print(f"\n\nTOTAL VIEWERSHIP PER NETWORK: {total_network_views}")
print(f"\nTOTAL VIEWERSHIP PER GENRE: {total_genre_views}")

# Calculate multiple metrics with .agg()
network_summary = raw_data.groupby('Network').agg(
    {
        'Show_Title': 'count',
        'Avg_Rating': 'mean',
        'Views_Millions': 'sum'
    }
)

# Rename columns to make the report tidy
network_summary.columns = ['Total Shows', 'Avg Rating', 'Total Views (Millions)']
print(f"\n\n---- NETWORK PERFORMANCE SUMMARY ----:\n{network_summary}")