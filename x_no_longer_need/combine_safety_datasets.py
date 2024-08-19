import pandas as pd

# Load the datasets
filepaths = [
    'data2/safety_crime_40_60.csv',
    'data2/safety_crime_60_100.csv',
    'data2/safety_crime_100_250.csv',
    'data2/safety_crime_250_plus.csv'
]

# Create a list to hold the dataframes
dfs = []

# Loop over the filepaths and load the data into the list
for filepath in filepaths:
    df = pd.read_csv(filepath, usecols=['states', 'cities', 'safety_index'])
    dfs.append(df)

# Concatenate all dataframes
combined_df = pd.concat(dfs)

# Check for overlapping cities
overlapping_cities = combined_df[combined_df.duplicated(subset=['states', 'cities'], keep=False)]

if not overlapping_cities.empty:
    print("Overlapping cities found:")
    print(overlapping_cities)
else:
    print("No overlapping cities found.")

# Drop duplicates (keeping the first occurrence)
combined_df.drop_duplicates(subset=['states', 'cities'], keep='first', inplace=True)

# Save the combined data
combined_df.to_csv('data2/combined_safety_index.csv', index=False)

print("Combined dataset saved to 'data2/combined_safety_index.csv'")
