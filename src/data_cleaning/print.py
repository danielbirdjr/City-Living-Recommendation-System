import pandas as pd

# Load your dataset
df = pd.read_csv('data/everything_dataset.csv')

# Print the next 50 rows (rows 50 to 100)
print(df[['City', 'State']].iloc[0:308])
