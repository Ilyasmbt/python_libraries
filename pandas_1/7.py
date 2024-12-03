#pandas dataFrames

#a pandas DATAFRAMES is a 2-D data structure,
#like a 2-d array,or a table with rows and columns

#create a simple pandas DataFrame ?


import pandas as py

data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
#load data info a dataframe object:
my_obj=py.DataFrame(data)

print(my_obj)