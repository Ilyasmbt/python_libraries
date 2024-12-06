#CALCULATE THE MEDIAN,AND REPLACE ANY EMPTY VALUES WITH IT?

#MEDIAN=THE VALUE IN THE MIDDLE,
#AFTER YOU HAVE SORTED ALL VALUES ASCENDING


import pandas as pd
df=pd.read_csv('data.csv')

x=df["Calories"].median()

df["Calories"].fillna(x,inplace=True)
print(df.to_string())