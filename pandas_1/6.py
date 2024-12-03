#dataFrames

#data sets in pandas are usually multi_dimensional tables,called Dataframes.

#series is like a column ,a dataFrame is the whole table.
#create a dataFrame from two series?

import pandas as py

data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
my_var=py.DataFrame(data)

print(my_var)