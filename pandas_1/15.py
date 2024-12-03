#increase the  maximum number of rows to display the entire dataframe?

import pandas as pd

pd.o.display.max_rows=9999

df=pd.read_csv('big.csv')

print(df)