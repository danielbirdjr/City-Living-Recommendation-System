import pandas as pd

# Load the cleaned crime data
crime_df = pd.read_csv('data/cleaned_crime_data.csv')

# Extract unique cities and states
unique_cities = crime_df[['cities', 'states']].drop_duplicates()

# Save to a CSV file for further use
unique_cities.to_csv('data/city_state_mapping.csv', index=False)

print(unique_cities.head())
