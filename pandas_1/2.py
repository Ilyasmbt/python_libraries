#pandas Series

#a pandas series is like a column in a table.

#it is a one-d array holding data of any type

#create a simple pandas series from a list ?

import pandas as pd
a =[1,7,2,7,2]

myvar = pd.Series(a)
print(myvar)

#return the first value of the series?
print(myvar[0])