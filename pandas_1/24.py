#pandas- cleaning empty cells

#return a new data  frame with no empty cells?

import pandas as pd

df=pd.read_csv('data1.csv')
print(df)

new_df=df.dropna()

print(new_df.to_string())

#note: original file change illa