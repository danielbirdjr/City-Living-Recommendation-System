import pandas as pd

# Load the existing dataset
file_path = 'data2/average_temp_by_state_2013_2022.csv'
temp_data = pd.read_csv(file_path)

# Data to add for Hawaii, Alaska, and District of Columbia
new_data = {
    'state': ['Hawaii', 'Alaska', 'District of Columbia'],
    'average_temp_january': [73.5, 16.5, 34.5],
    'average_temp_february': [73.6, 19.0, 37.0],
    'average_temp_march': [73.9, 24.0, 45.0],
    'average_temp_april': [75.5, 34.5, 54.0],
    'average_temp_may': [76.5, 45.0, 63.0],
    'average_temp_june': [78.0, 55.0, 70.5],
    'average_temp_july': [79.0, 60.0, 76.0],
    'average_temp_august': [80.0, 59.0, 75.5],
    'average_temp_september': [79.0, 50.0, 68.0],
    'average_temp_october': [78.0, 38.5, 56.5],
    'average_temp_november': [76.0, 25.0, 47.0],
    'average_temp_december': [74.0, 17.0, 38.0]
}

# Create a DataFrame from the new data
new_df = pd.DataFrame(new_data)

# Append the new data to the existing data
updated_temp_data = pd.concat([temp_data, new_df], ignore_index=True)

# Save the updated dataset to a new CSV file
updated_file_path = 'data2/average_temp_by_state_2013_2022_updated.csv'
updated_temp_data.to_csv(updated_file_path, index=False)

print(f"Updated dataset saved to {updated_file_path}")
