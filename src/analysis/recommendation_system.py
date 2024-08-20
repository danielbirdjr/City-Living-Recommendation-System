import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

# User preferences
preferences = {
    'cost_of_living_weight': -1.5,  # High priority (3) -> Negative weight for low cost
    'median_income_weight': 1.5,    # High priority (3)
    'population_weight': 1.0,       # High priority (3)
    'education_weight': 1.5,        # High priority (3)
    'temperature_weight': 1.5,      # High priority (3)
    'safety_weight': 1.5            # High priority (3)
}

# Create a weighted sum based on user preferences
df['recommendation_score'] = (
    df['Cost of Living Index'] * preferences['cost_of_living_weight'] +
    df['Median'] * preferences['median_income_weight'] +
    df['population'] * preferences['population_weight'] +
    df['education_score'] * preferences['education_weight'] +
    df[['average_temp_january', 'average_temp_february', 'average_temp_march', 
        'average_temp_april', 'average_temp_may', 'average_temp_june', 
        'average_temp_july', 'average_temp_august', 'average_temp_september', 
        'average_temp_october', 'average_temp_november', 'average_temp_december']].mean(axis=1) 
        * preferences['temperature_weight'] +
    df['safety_index'] * preferences['safety_weight']
)

# Sort by recommendation score
df = df.sort_values(by='recommendation_score', ascending=False)

# Splitting the data into training and testing sets (though this is for demonstration purposes)
X = df[features_to_normalize]
y = (df['recommendation_score'] > df['recommendation_score'].median()).astype(int)  # Assuming 1 for top recommendations

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Show top 10 recommended cities based on the user's preferences
print(df[['City', 'State', 'recommendation_score']].head(10))
