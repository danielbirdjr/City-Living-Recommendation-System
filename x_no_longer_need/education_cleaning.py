import pandas as pd

# Load the merged city data
city_data = pd.read_csv('data2/merged_city_data_final.csv')

# Load the cleaned education data
education_data = pd.read_csv('data2/cleaned_school_scores_2015.csv')

# Ensure consistency in the State columns
city_data['State_Name'] = city_data['State_Name'].str.lower().str.strip()
education_data['State.Name'] = education_data['State.Name'].str.lower().str.strip()

# Merge the education data based on the State_Name
merged_data = pd.merge(city_data, education_data, how='left', left_on='State_Name', right_on='State.Name')

# Drop the redundant 'State.Name' column
merged_data.drop(columns=['State.Name'], inplace=True)

# Save the final merged dataset
merged_data.to_csv('data2/merge_4_datasets_final.csv', index=False)

# Display the first few rows of the merged data to confirm
print(merged_data.head())
