import pandas as pd

#user_cols show colomns we need.
user_cols = ['carat', 'color', 'depth',  'table',  'price', 'x', 'y', 'z']
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("First 10 rows:")
#It's important put user_cols in square brackets before point
print(diamonds[user_cols].head(10))
