import pandas as pd

# Load the dataset
dataset_path = 'data/everything_dataset.csv'
df = pd.read_csv(dataset_path)

# Print column names to verify
print(df.columns)
