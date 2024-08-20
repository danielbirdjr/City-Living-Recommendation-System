import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = 'data/everything_dataset.csv'
data = pd.read_csv(file_path)

# Drop any rows with missing data
data = data.dropna()

# Define the features and target
features = [
    'Cost of Living Index', 'population', 'Mean', 'Median',
    'average_temp_january', 'average_temp_february', 'average_temp_march',
    'average_temp_april', 'average_temp_may', 'average_temp_june',
    'average_temp_july', 'average_temp_august', 'average_temp_september',
    'average_temp_october', 'average_temp_november', 'average_temp_december',
    'Total.Math', 'Total.Verbal', 'Academic Subjects.English.Average GPA',
    'Academic Subjects.Mathematics.Average GPA', 'safety_index'
]

X = data[features]

# Define default weights
default_weights = {
    'Cost of Living Index': 2,
    'population': 2,
    'Mean': 2,
    'Median': 2,
    'average_temp_january': 2,
    'average_temp_february': 2,
    'average_temp_march': 2,
    'average_temp_april': 2,
    'average_temp_may': 2,
    'average_temp_june': 2,
    'average_temp_july': 2,
    'average_temp_august': 2,
    'average_temp_september': 2,
    'average_temp_october': 2,
    'average_temp_november': 2,
    'average_temp_december': 2,
    'Total.Math': 1,
    'Total.Verbal': 1,
    'Academic Subjects.English.Average GPA': 1,
    'Academic Subjects.Mathematics.Average GPA': 1,
    'safety_index': 0.75
}

# User-defined weight adjustments
def adjust_weights(safety_priority, education_priority):
    adjusted_weights = default_weights.copy()
    
    # Adjust safety index based on user priority
    adjusted_weights['safety_index'] = 0.5 + 0.25 * (safety_priority - 1)
    
    # Adjust education based on user priority
    adjusted_weights['Total.Math'] *= 0.75 + 0.25 * (education_priority - 1)
    adjusted_weights['Total.Verbal'] *= 0.75 + 0.25 * (education_priority - 1)
    adjusted_weights['Academic Subjects.English.Average GPA'] *= 0.75 + 0.25 * (education_priority - 1)
    adjusted_weights['Academic Subjects.Mathematics.Average GPA'] *= 0.75 + 0.25 * (education_priority - 1)
    
    # Adjust other features down if safety is prioritized
    if safety_priority == 3:
        for key in adjusted_weights:
            if key != 'safety_index':
                adjusted_weights[key] = 1
    
    return adjusted_weights

# Example user inputs
user_safety_priority = 3  # User prioritizes safety the most
user_education_priority = 2  # Education is moderately important

# Apply user-defined weight adjustments
weights = adjust_weights(user_safety_priority, user_education_priority)

# Scale features before applying weights
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=features)

# Apply the weighting to the features
for feature in features:
    X_scaled[feature] = X_scaled[feature] * weights[feature]

# Create a dummy target variable for training purposes
y = (data['population'] > 100000).astype(int)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model's performance
accuracy = model.score(X_test, y_test)

# Apply the model to the entire dataset to get recommendation scores
recommendation_scores = model.predict_proba(X_scaled)[:, 1]
data['recommendation_score'] = recommendation_scores

# Get the top 10 recommended cities
top_10_cities = data[['City', 'State', 'population', 'recommendation_score']].sort_values(by='recommendation_score', ascending=False).head(10)

print("Accuracy:", accuracy)
print(top_10_cities)
