#replace using mean,median, or mode

#replace using mean
#mean= the average value(the sum of all values divided by number of values)
#calculate the mean, and replace any empt values with it?

import pandas as pd

df=pd.read_csv('data.csv')

x=df["Calories"].mean()

df["Calories"].fillna(x,inplace=True)
print(df.to_string())