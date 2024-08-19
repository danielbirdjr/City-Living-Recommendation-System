import pandas as pd

# Load population data
population_data = pd.read_csv('data/cleaned_population_data.csv')
city_county_data = pd.read_csv('data/city-county-mapping-dataset.csv')

# Merge datasets
merged_data = pd.merge(city_county_data, population_data, on=['County', 'State'], how='left')

# Identify missing data
missing_data = merged_data[merged_data['CountyId'].isnull()]
print(f"Number of cities with missing data: {len(missing_data)}")
print("Missing data after merge:")
print(missing_data[['City', 'State', 'County']].head(10))

# Save the aggregated data
merged_data.to_csv('data/aggregated_filtered_population_data.csv', index=False)

# Show sample data
print("Sample population data:")
print(population_data.head())
print("Sample city-county mapping data:")
print(city_county_data.head())
print("Sample merged data:")
print(merged_data.head())
