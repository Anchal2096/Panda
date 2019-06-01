import pandas as pd

# df = pd.read_csv("weather.csv")
# print(df)
EMPLOYEES = {"NAME": ['ANCHAL', 'SHIVAM', 'ABHISHEK', 'SHASHANK', 'YASHI', 'SUMIRAN'],
             "EMPLOYEE_NO": ['21130', '21131', '21132', '21133', '21134', '21135'],
             "FAVOURITE_COLOR": ['PINK', 'BLACK', 'BLUE', 'GREEN', 'YELLOW', 'BLACK'],
             "SALARY": ['100000000', '500000', '1000000', '6132334', '901813', '200000']}
df = pd.DataFrame(EMPLOYEES)
print(df)  # prints the value of the dataframe object
rows, columns = df.shape
# print(rows, columns, df.head(2))  # head gives the convenience of printing only first few rows
# print(df.tail(2))  # tail gives the convenience of printing only first few rows
# print(df.columns)
# print(df.SALARY)  # df['SALARY']
# print("THE TYPE OF NAME COLUMN IS", type(df.NAME))
# print((df.SALARY).std)  # standard deviation
# print(df.describe())
# print(df.index)
# print(df.set_index('EMPLOYEE_NO', inplace=True))  # inplace implies the changes permanently else it will just
# project the changes
print(df.reset_index(inplace=True))
