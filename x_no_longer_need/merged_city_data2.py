import pandas as pd

# Load each dataset
cost_of_living = pd.read_csv('data2/advisorsmith_cost_of_living_index.csv')
income = pd.read_csv('data2/kaggle_income.csv', encoding='ISO-8859-1')
cities = pd.read_csv('data2/uscities.csv')

# Standardize the city and state names to lowercase to avoid mismatches
cost_of_living['City'] = cost_of_living['City'].str.lower().str.strip()
cost_of_living['State'] = cost_of_living['State'].str.lower().str.strip()

income['City'] = income['City'].str.lower().str.strip()
income['State_ab'] = income['State_ab'].str.lower().str.strip()

cities['city'] = cities['city'].str.lower().str.strip()
cities['state_id'] = cities['state_id'].str.lower().str.strip()

# Merge the datasets
merged_data = pd.merge(cost_of_living, income, left_on=['City', 'State'], right_on=['City', 'State_ab'], how='left')
merged_data = pd.merge(merged_data, cities, left_on=['City', 'State'], right_on=['city', 'state_id'], how='left')

# Drop duplicates
merged_data = merged_data.drop_duplicates(subset=['City', 'State'])

# Save the final merged dataset to a new CSV file
merged_data.to_csv('data2/merged_city_data_final.csv', index=False)

# Output the first few rows to verify the merge
print(merged_data.head())
