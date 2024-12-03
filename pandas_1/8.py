#locate Row

#pandas use the loc attribute to return one or more specified row(s)

#return row 0?
import pandas as pd
data={
    "calories":[450,380,390],
    "duration":[50,40,45]
}

df=pd.DataFrame(data)
print(df.loc[0])         #loc
