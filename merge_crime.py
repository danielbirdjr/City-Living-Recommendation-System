import pandas as pd

# Load each crime dataset
crime_40_60 = pd.read_csv('data/crime_40_60.csv')
crime_60_100 = pd.read_csv('data/crime_60_100.csv')
crime_100_250 = pd.read_csv('data/crime_100_250.csv')
crime_250_plus = pd.read_csv('data/crime_250_plus.csv')

# Standardize column names
crime_40_60.columns = crime_40_60.columns.str.lower().str.replace(' ', '_')
crime_60_100.columns = crime_60_100.columns.str.lower().str.replace(' ', '_')
crime_100_250.columns = crime_100_250.columns.str.lower().str.replace(' ', '_')
crime_250_plus.columns = crime_250_plus.columns.str.lower().str.replace(' ', '_')

# Merge the datasets
crime_df = pd.concat([crime_40_60, crime_60_100, crime_100_250, crime_250_plus], ignore_index=True)

# Save the merged dataset
crime_df.to_csv('data/merged_crime_data.csv', index=False)

# Optional: Print the first few rows and dataset info to verify
print(crime_df.head())
print(crime_df.info())
