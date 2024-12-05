#pandas- cleaning Data
#DATA cleaning
#data cleaning means fixing bad datq in ur data set
#bad data could be:

#empty cells
#data in wrong format
#wrong data
#duplicates

import  pandas as pd
df= pd.read_csv('data1.csv')

print(df.to_string())

# data row 22,28,18 is  empty
#26 is wrong format
#7 is wrong data
#11 and 12 is duplicate