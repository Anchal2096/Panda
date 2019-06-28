# Load the Pandas libraries with alias 'pd'
import pandas as pd
import warnings

# Control delimiters, rows, column names with read_csv
df = pd.read_csv("business-operations-survey-2018-business-finance-csv.csv")
# Preview the first 5 lines of the loaded df
# print(df.head())
print(df)
print((df["value"]).max())  # to print the max value

warnings.simplefilter(action='ignore', category=FutureWarning)
print(df["industry"][df["level"] == 2])
print(df.head())

