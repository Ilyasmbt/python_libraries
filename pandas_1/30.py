#CALCULATE THE MODE,AND REPLACE ANY EMPTY VALUESWITH IT?
#mode= the value that appears mOST FREQUENTLY
import pandas as pd

df=pd.read_csv('data.csv')

x=df["Calories"].mode()
print(x)

df["Calories"].fillna(x,inplace=True)
print(df.to_string())