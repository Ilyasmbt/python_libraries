#load files into a DataFRAME
#if your data sets are stored in a file ,pandas can load them into a dataFRAME
#load a comma separated file(csv file) into a DataFrames ?



import pandas as pd
df=pd.read_csv('data.csv')
print(df)