import pandas as pd

# Show all rows
pd.set_option('display.max_rows', None)

# Show all columns (no horizontal truncation)
pd.set_option('display.max_columns', None)

# Show complete text inside cells without truncating with '...'
pd.set_option('display.max_colwidth', None)

# Prevent auto-wrapping onto new lines for wide tables
pd.set_option('display.width', 1000)
