import pandas as pd

# List of cleaned crime files
cleaned_files = [
    'data2/safety_crime_40_60.csv',
    'data2/safety_crime_60_100.csv',
    'data2/safety_crime_100_250.csv',
    'data2/safety_crime_250_plus.csv'
]

# Function to print the first few rows of each file
def inspect_cleaned_files(files):
    for file in files:
        print(f"\n--- {file} ---")
        data = pd.read_csv(file)
        print(data.head(15))  # Print the first 15 rows

# Inspect the cleaned files
inspect_cleaned_files(cleaned_files)
