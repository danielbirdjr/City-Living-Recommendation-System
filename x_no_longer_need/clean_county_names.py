import pandas as pd

# Load the population data
population_data = pd.read_csv('data/cleaned_population_data.csv')

# Standardize county names
population_data['County'] = population_data['County'].str.lower().str.strip()

# Save the cleaned data
population_data.to_csv('data/cleaned_population_data.csv', index=False)

print("County names in population data have been cleaned and standardized.")
