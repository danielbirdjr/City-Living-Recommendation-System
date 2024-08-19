import pandas as pd

# Load the city-county mapping data
city_county_data = pd.read_csv('data/city-county-mapping-dataset.csv')

# Standardize county names
city_county_data['County'] = city_county_data['County'].str.lower().str.strip()

# Save the cleaned data
city_county_data.to_csv('data/city-county-mapping-dataset.csv', index=False)

print("County names in city-county mapping data have been cleaned and standardized.")
