import pandas as pd


EMPLOYEES = {"NAME": ['ANCHAL', 'SHIVAM', 'ABHISHEK', 'SHASHANK', 'YASHI', 'SUMIRAN'],
             "EMPLOYEE_NO": ['21130', '21131', '21132', '21133', '21134', '21135'],
             "FAVOURITE_COLOR": ['PINK', 'BLACK', 'BLUE', 'GREEN', 'YELLOW', 'BLACK'],
             "SALARY": ['100000000', '500000', '1000000', '6132334', '901813', '200000']}
df = pd.DataFrame(EMPLOYEES)
# print(df)  # prints the value of the dataframe object
# print(df.columns)
# print(df.index)
# print(df.values)
# print(df.columns.values)
# print(type(df.columns))
# print(type(df.columns.values))
# print(df.dtypes)
print(df.SALARY.to_frame())
# print(df.SALARY)
