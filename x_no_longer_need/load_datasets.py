import pandas as pd

# Load datasets
population_df = pd.read_csv('data/acs2017_county_data.csv')
cost_of_living_df = pd.read_csv('data/cost_of_living_us.csv')
crime_df = pd.read_csv('data/merged_crime_data.csv')
education_df = pd.read_csv('data/school_scores.csv')
climate_df = pd.read_csv('data/US_City_Temp_Data.csv')

# Initial exploration
print("Population DataFrame:")
print(population_df.head())
print(population_df.info())
print(population_df.describe())
print(population_df.isnull().sum())

print("\nCost of Living DataFrame:")
print(cost_of_living_df.head())
print(cost_of_living_df.info())
print(cost_of_living_df.describe())
print(cost_of_living_df.isnull().sum())

print("\nCrime DataFrame:")
print(crime_df.head())
print(crime_df.info())
print(crime_df.describe())
print(crime_df.isnull().sum())

print("\nEducation DataFrame:")
print(education_df.head())
print(education_df.info())
print(education_df.describe())
print(education_df.isnull().sum())

print("\nClimate DataFrame:")
print(climate_df.head())
print(climate_df.info())
print(climate_df.describe())
print(climate_df.isnull().sum())
