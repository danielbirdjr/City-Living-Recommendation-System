import pandas as pd

# Load the population data
population_data = pd.read_csv('data/cleaned_population_data.csv')

# Filter counties with a population of 100,000 or more
counties_above_threshold = population_data[population_data['TotalPop'] >= 200000]

# Get the count of such counties
number_of_counties = len(counties_above_threshold)

# Print the result
print(f"Number of counties with a population of 100,000 or more: {number_of_counties}")

# Optional: Print a sample of these counties
print("Sample of counties with a population of 100,000 or more:")
print(counties_above_threshold.head())
