#pandas- cleaning data f wrong format
#data of wrong format


#to fix it
#remove the rows
#convert all cells IN THE COLUMNS INTO THE SAME FORMAT

#pandas has to_datetime() method for this:

#convert to date?

import pandas as pd

df=pd.read_csv('dd.csv')
print(df)

df['Date']=pd.to_datetime(df['Date'])
print(df.to_string())