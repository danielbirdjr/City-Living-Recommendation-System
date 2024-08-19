import pandas as pd

# Load the dataset
data = pd.read_csv('data2/matched_cities_final.csv')

# Group by 'City' and 'State' and calculate the average safety index for each specific City-State pair
data['safety_index'] = data.groupby(['City', 'State'])['safety_index'].transform('mean')

# Save the updated dataset
data.to_csv('data2/updated_matched_cities_final.csv', index=False)

print("Safety index values updated with averages for duplicates.")
