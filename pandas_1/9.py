#return row 1 and3?
import pandas as pd
data={
    "calories":[450,380,390,380],
    "duration":[50,40,45,45]
}
#load data into a dataframe object:
df=pd.DataFrame(data)
print(df.loc[[1,3]])         #note: when using[], the result is a pandas dataframe
