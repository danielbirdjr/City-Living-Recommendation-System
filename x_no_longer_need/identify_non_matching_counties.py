import pandas as pd

# Load necessary data
city_county_data = pd.read_csv('data/city-county-mapping-dataset.csv')
population_data = pd.read_csv('data/cleaned_population_data.csv')

# Identify non-matching counties
non_matching_counties = city_county_data[~city_county_data['County'].isin(population_data['County'].str.lower())]
print("Non-matching counties in population data:")
print(non_matching_counties['County'].unique())
