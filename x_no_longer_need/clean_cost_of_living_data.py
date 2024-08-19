import pandas as pd

# Load the cost of living dataset
cost_of_living_df = pd.read_csv('data/cost_of_living_us.csv')

# Display initial info to understand the data
print("Before cleaning:")
print(cost_of_living_df.info())

# Fill missing values in 'median_family_income' with the median of the column
cost_of_living_df['median_family_income'].fillna(cost_of_living_df['median_family_income'].median(), inplace=True)

# Display the info again to verify that the missing data has been handled
print("\nAfter cleaning:")
print(cost_of_living_df.info())

# Save the cleaned data to a new CSV file
cost_of_living_df.to_csv('data/cleaned_cost_of_living_data.csv', index=False)

print("Cleaned cost of living data saved to 'data/cleaned_cost_of_living_data.csv'")
