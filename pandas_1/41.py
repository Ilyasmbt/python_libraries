import pandas as pd
import numpy as ny

a=pd.read_csv("Temperature.unknown",header=None,sep=" ")
a.columns=['year','temp']
print(a)

b=a.groupby("year")['temp'].max().sort_values(ascending=False)
print(b)