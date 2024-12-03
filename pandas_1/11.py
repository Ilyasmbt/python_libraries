#LOCATE NAMED INDEXES
#USE THE NAMED INDEX IN THE LOC ATTRIBUTE TO RETURN THE SPECIFIED ROW(S)
#return "days2"/?
import pandas as pd
data={
    "calories":[450,380,390,370],
    "duration":[50,40,45,35]
}

df=pd.DataFrame(data,index=["days1","days2","days3","days4"])
print(df.loc["days2"])
#return row 1 ,4and 3?
print(df.loc[["days1","days3","days4"]])
