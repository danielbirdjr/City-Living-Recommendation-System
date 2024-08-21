import sys
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Parse user preferences from command-line arguments
preferences = eval(sys.argv[1])

# Load the dataset
df = pd.read_csv('data/everything_dataset.csv')

# Features to be used for recommendation
features_to_normalize = [
    'Cost of Living Index', 'population', 'Median', 
    'education_score', 'safety_index',
    'average_temp_january', 'average_temp_february', 'average_temp_march', 'average_temp_april',
    'average_temp_may', 'average_temp_june', 'average_temp_july', 'average_temp_august',
    'average_temp_september', 'average_temp_october', 'average_temp_november', 'average_temp_december'
]

# Normalize the selected features
scaler = MinMaxScaler()
df[features_to_normalize] = scaler.fit_transform(df[features_to_normalize])

# Create a weighted sum based on user preferences
df['recommendation_score'] = (
    df['Cost of Living Index'] * float(preferences['cost_of_living']) +
    df['Median'] * float(preferences['median_income']) +
    df['population'] * float(preferences['population']) +
    df['education_score'] * float(preferences['education']) +
    df[['average_temp_january', 'average_temp_february', 'average_temp_march', 
        'average_temp_april', 'average_temp_may', 'average_temp_june', 
        'average_temp_july', 'average_temp_august', 'average_temp_september', 
        'average_temp_october', 'average_temp_november', 'average_temp_december']].mean(axis=1) 
        * float(preferences['temperature']) +
    df['safety_index'] * float(preferences['safety'])
)

# Sort by recommendation score 
df = df.sort_values(by='recommendation_score', ascending=False)

# Show top 10 recommended cities based on the user's preferences
top_cities = df[['City', 'State', 'recommendation_score']].head(10).to_dict(orient='records')

# Output the recommendations as JSON
print(top_cities)
