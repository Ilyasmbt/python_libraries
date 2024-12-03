#named indexe
#with the indexes argument,you can name your own indexes.
#add a list of names to give each row a name?


import pandas as py
data={
    "calories":[450,380,390],
    "duration":[50,40,45]
}

df=py.DataFrame(data,index=["day1","day2","day3"])
print(df)