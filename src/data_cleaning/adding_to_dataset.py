import pandas as pd

# Step 1: Load the dataset
dataset_path = 'data/everything_dataset.csv'
df = pd.read_csv(dataset_path)

# Step 2: Parse the safety index file
safety_index_path = 'data/safety_index.txt'
safety_index_map = {}

with open(safety_index_path, 'r') as file:
    for line in file:
        if ': ' in line:
            city_state, safety_index = line.split(': ')
            city, state = city_state.rsplit(',', 1)
            city = city.strip().lower()
            state = state.strip().lower()
            safety_index_map[(city, state)] = int(safety_index)

# Step 3: Replace the safety_index values in the DataFrame
def get_safety_index(row):
    city = row['City'].strip().lower()
    state = row['State'].strip().lower()
    key = (city, state)
    if key in safety_index_map:
        return safety_index_map[key]
    else:
        print(f"No match found for: {row['City']}, {row['State']}. Looking for: {key}")
        return row['safety_index']

df['safety_index'] = df.apply(get_safety_index, axis=1)

# Step 4: Save the updated DataFrame
df.to_csv('data/updated_everything_dataset.csv', index=False)

print("Safety index values have been updated and saved in 'data/updated_everything_dataset.csv'")
