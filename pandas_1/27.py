#replace only for specified columns

#the example above replaces all empty cells in the whole data frame

#to only replace empty values for one column

#replace null values in the "calories" columns with the number 130:/

import pandas as pd
df = pd.read_csv('data.csv')
df["Calories"].fillna(130,inplace = True)
print(df.to_string())
