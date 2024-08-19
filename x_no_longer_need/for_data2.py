import pandas as pd

# Load each dataset and print the first few rows and column names
data1 = pd.read_csv('data2/advisorsmith_cost_of_living_index.csv')
print(data1.head())
print(data1.columns)

# Try reading the kaggle_income.csv with ISO-8859-1 encoding
data2 = pd.read_csv('data2/kaggle_income.csv', encoding='ISO-8859-1')
print(data2.head())
print(data2.columns)

data3 = pd.read_csv('data2/uscities.csv')
print(data3.head())
print(data3.columns)
