import pandas as pd

# Load the existing merged dataset
merged_file_path = 'data2/merge_4_datasets_final.csv'
merged_data = pd.read_csv(merged_file_path)

# Load the temperature dataset
temperature_file_path = 'data2/average_temp_by_state_2013_2022_updated.csv'
temperature_data = pd.read_csv(temperature_file_path)

# Ensure consistency in the State columns
merged_data['State_Name'] = merged_data['State_Name'].str.lower().str.strip()
temperature_data['state'] = temperature_data['state'].str.lower().str.strip()

# Merge the datasets based on the 'State_Name' from merged data and 'state' from temperature data
final_merged_data = pd.merge(merged_data, temperature_data, how='left', left_on='State_Name', right_on='state')

# Drop the redundant 'state' column after merging
final_merged_data.drop(columns=['state'], inplace=True)

# Save the final dataset with the added temperature data
final_merged_file_path = 'data2/merge_5_datasets_final.csv'
final_merged_data.to_csv(final_merged_file_path, index=False)

print(f"Final merged dataset saved to {final_merged_file_path}")
