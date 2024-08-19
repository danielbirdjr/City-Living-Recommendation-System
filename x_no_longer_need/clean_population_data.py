import pandas as pd

# Load population data
population_df = pd.read_csv('data/cleaned_population_data.csv')

# Clean and standardize county names
population_df['County'] = (population_df['County']
                           .str.lower()
                           .str.replace(' county', '')
                           .str.replace(' municipality', '')
                           .str.replace(' census area', '')
                           .str.replace(' city', '')
                           .str.replace(' borough', '')
                           .str.replace(' municipio', '')
                           .str.strip())

# Save cleaned population data
population_df.to_csv('data/cleaned_population_data.csv', index=False)
print("County names in population data have been cleaned and standardized.")
