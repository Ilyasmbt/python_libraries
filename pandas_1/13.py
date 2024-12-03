#pandas read CSV
#IF YOU HAVE A LARGE dataframe WITH MANY ROWS,

#TO_STRING()--- USED TO PRINT THE ENTIRE DATAFRAMES

import pandas as pd

file_data=pd.read_csv('big.csv')

print(file_data.to_string())

#print(file_data)--method
#will only return the first 5 rows ,and the last 5 rows: