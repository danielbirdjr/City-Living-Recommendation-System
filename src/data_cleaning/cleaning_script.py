import pandas as pd

def calculate_safety_index(row):
    return (0.3 * row['murder'] +
            0.2 * row['rape'] +
            0.2 * row['robbery'] +
            0.3 * row['agrv_assault'] +
            0.5 * row['burglary'] +
            0.4 * row['larceny'] +
            0.1 * row['vehicle_theft']) / 2

# List of files to process
files = [
    'data2/cleaned_crime_40_60.csv',
    'data2/cleaned_crime_60_100.csv',
    'data2/cleaned_crime_100_250.csv',
    'data2/cleaned_crime_250_plus.csv'
]

for file in files:
    print(f"Processing {file}...")
    data = pd.read_csv(file)

    # Convert relevant columns to numeric if they aren't already
    for column in ['murder', 'rape', 'robbery', 'agrv_assault', 'burglary', 'larceny', 'vehicle_theft']:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    # Calculate the safety index
    data['safety_index'] = data.apply(calculate_safety_index, axis=1)

    # Save the updated dataset
    output_file = file.replace('cleaned_', 'safety_')
    data.to_csv(output_file, index=False)
    print(f"Processed and saved {output_file}")
