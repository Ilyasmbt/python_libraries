#replace empty values
#another way of dealing with empty cells is to insert a new value instead

#replace NULL values with the number 130?


import pandas as pd
df = pd.read_csv('data1.csv')
df.fillna(130,inplace = True)
print(df.to_string())
