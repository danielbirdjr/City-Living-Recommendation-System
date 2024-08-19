import pandas as pd

# Load your final dataset
data = pd.read_csv('data2/final_city_data_with_safety.csv')

# Handle NaN values in the input columns
data['density'].fillna(data['density'].mean(), inplace=True)
data['safety_index'].fillna(data['safety_index'].mean(), inplace=True)
data['Total.Math'].fillna(data['Total.Math'].mean(), inplace=True)
data['Total.Verbal'].fillna(data['Total.Verbal'].mean(), inplace=True)

# Normalize the data to bring all indicators to a comparable scale
data['normalized_density'] = (data['density'] - data['density'].min()) / (data['density'].max() - data['density'].min())
data['normalized_safety'] = (data['safety_index'] - data['safety_index'].min()) / (data['safety_index'].max() - data['safety_index'].min())
data['normalized_education'] = (data['Total.Math'] + data['Total.Verbal']) / 2  # Averaging education scores
data['normalized_education'] = (data['normalized_education'] - data['normalized_education'].min()) / (data['normalized_education'].max() - data['normalized_education'].min())

# Calculate the healthcare approximation score
data['healthcare_score'] = (0.4 * data['normalized_density']) + (0.4 * data['normalized_safety']) + (0.2 * data['normalized_education'])

# Drop any remaining NaN values
data.dropna(subset=['healthcare_score'], inplace=True)

# Save the dataset with the new healthcare score
data.to_csv('data2/final_city_data_with_healthcare_cleaned.csv', index=False)

# Print the first few rows to verify
print(data[['City', 'State', 'healthcare_score']].head())
