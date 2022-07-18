#Read first 5 rows from csv

import pandas as pd
pd.set_option('display.max_rows', 250)
pd.set_option('display.max_columns', 10)
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("First 5 rows:")
print(diamonds.head(5))
