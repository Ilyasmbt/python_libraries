import numpy as np
import pandas            as pd
a=pd.read_csv("sample4.txt"
              ,
              header=None)
a.columns=['id','fname','lname','age','ph_no','loc']
b=a.groupby('loc') ['loc'].count()
print(b)