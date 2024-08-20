import pandas as pd

# Step 1: Load the datasets
dataset_path = 'data/everything_dataset.csv'
education_scores_path = 'data/education_scores.csv'

df = pd.read_csv(dataset_path)
education_scores_df = pd.read_csv(education_scores_path, header=None, names=['City', 'State', 'education_score'])

# Step 2: Standardize the text data (lowercase and strip whitespace)
df['City'] = df['City'].str.strip().str.lower()
df['State'] = df['State'].str.strip().str.lower()
education_scores_df['City'] = education_scores_df['City'].str.strip().str.lower()
education_scores_df['State'] = education_scores_df['State'].str.strip().str.lower()

# Step 3: Merge the DataFrames on City and State
merged_df = pd.merge(df, education_scores_df, on=['City', 'State'], how='left')

# Step 4: Save the updated DataFrame
merged_df.to_csv('data/updated_everything_dataset.csv', index=False)

print("Education scores have been added and saved in 'data/updated_everything_dataset.csv'")
