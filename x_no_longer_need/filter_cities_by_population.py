import pandas as pd

# Load the city-county mapping data
city_county_data = pd.read_csv('data/city-county-mapping-dataset.csv')

# Load the population data
population_data = pd.read_csv('data/cleaned_population_data.csv')  # or 'filtered_population_data.csv'

# Convert state and county names to lowercase to standardize
city_county_data['State'] = city_county_data['State'].str.lower()
city_county_data['County'] = city_county_data['County'].str.lower()
population_data['State'] = population_data['State'].str.lower()
population_data['County'] = population_data['County'].str.lower()

# Manual mapping for key counties
manual_mapping = {
    'bronx': 'bronx',
    'richmond': 'richmond',
    'new york': 'new york',
    'kings': 'kings',
    'queens': 'queens',
    'los angeles': 'los angeles',
    'cook': 'cook',
    'harris': 'harris',
    'maricopa': 'maricopa',
    'philadelphia': 'philadelphia',
    'bexar': 'bexar',
    'san diego': 'san diego',
    'dallas': 'dallas',
    'collin': 'collin',
    'santa clara': 'santa clara',
    'travis': 'travis',
    'duval': 'duval',
    'franklin': 'franklin',
    'mecklenburg': 'mecklenburg',
    'multnomah': 'multnomah',
    'wayne': 'wayne',
    'clark': 'clark'
    # Add more as needed
}

city_county_data['County'] = city_county_data['County'].replace(manual_mapping)

# Merge datasets on the appropriate columns
merged_data = pd.merge(city_county_data, population_data, how='left', on=['County', 'State'])

# Filter the cities based on the updated population threshold
population_threshold = 100000  # Updated threshold
filtered_cities = merged_data[merged_data['TotalPop'] >= population_threshold]

# Save the filtered dataset
filtered_cities.to_csv('data/filtered_cities_by_population.csv', index=False)

# Debugging information
print(f"Number of cities after filtering: {len(filtered_cities)}")
print("Sample filtered cities data:")
print(filtered_cities.head())


# ... previous code ...

# Merge datasets on the appropriate columns
merged_data = pd.merge(city_county_data, population_data, how='left', on=['County', 'State'])

# Debugging: Check the number of NaN values in the merged data
nan_count = merged_data['TotalPop'].isna().sum()
print(f"Number of rows with NaN in TotalPop: {nan_count}")

# Filter the cities based on the updated population threshold
population_threshold = 100000  # Updated threshold
filtered_cities = merged_data[merged_data['TotalPop'] >= population_threshold]

# Save the filtered dataset
filtered_cities.to_csv('data/filtered_cities_by_population.csv', index=False)

# Debugging information
print(f"Number of cities after filtering: {len(filtered_cities)}")
print("Sample filtered cities data:")
print(filtered_cities.head())


# Inspect rows where TotalPop is NaN
nan_rows = merged_data[merged_data['TotalPop'].isna()]
print(f"Sample rows with NaN TotalPop:\n{nan_rows.head(20)}")

