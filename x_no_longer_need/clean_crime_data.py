import pandas as pd

# Load the crime dataset
crime_df = pd.read_csv('data/merged_crime_data.csv')

# Display initial info to understand the data
print("Before cleaning:")
print(crime_df.info())

# Convert columns to numeric types, coercing errors to NaN
crime_df['violent_crime'] = pd.to_numeric(crime_df['violent_crime'], errors='coerce')
crime_df['murder'] = pd.to_numeric(crime_df['murder'], errors='coerce')
crime_df['rape'] = pd.to_numeric(crime_df['rape'], errors='coerce')
crime_df['agrv_assault'] = pd.to_numeric(crime_df['agrv_assault'], errors='coerce')
crime_df['prop_crime'] = pd.to_numeric(crime_df['prop_crime'], errors='coerce')
crime_df['burglary'] = pd.to_numeric(crime_df['burglary'], errors='coerce')
crime_df['larceny'] = pd.to_numeric(crime_df['larceny'], errors='coerce')
crime_df['vehicle_theft'] = pd.to_numeric(crime_df['vehicle_theft'], errors='coerce')

# Fill missing values in columns that are important
crime_df['violent_crime'].fillna(crime_df['violent_crime'].median(), inplace=True)
crime_df['prop_crime'].fillna(crime_df['prop_crime'].median(), inplace=True)

# Drop columns with too much missing data
crime_df.drop(columns=['total_crime', 'tot_violent_crime', 'tot_prop_crim', 'arson'], inplace=True)

# Display the info again to verify that the missing data has been handled
print("\nAfter cleaning:")
print(crime_df.info())

# Save the cleaned data to a new CSV file
crime_df.to_csv('data/cleaned_crime_data.csv', index=False)

print("Cleaned crime data saved to 'data/cleaned_crime_data.csv'")
