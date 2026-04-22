import pandas as pd
from data import data_record

df = pd.DataFrame(data_record)
print(df)


# top 5 rows
print(df.head())

# top last rows
print(df.tail())

# shape of the data
print(df.shape)

# data column names
print(df.columns)

# data types
print(df.info())

# data description
print(df.describe())

# get only the names column
print(df["Name"])

df["salary"] = 10_000
print(df)