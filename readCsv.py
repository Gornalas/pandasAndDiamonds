import pandas as pd

#options for EDI
pd.set_option('display.max_rows', 250)
pd.set_option('display.max_columns', 10)
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("First 5 rows:")
#if you need only 5 first
print(diamonds.head(5))
