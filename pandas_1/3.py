#create Labels

#with the index arguments,you can name your own labels.
#create your own labels?

import pandas as pd
a=[1,2,34,8]

myvar= pd.Series(a,index=["x","y","z","a"])

print(myvar)

#return the value of "y"?
print(myvar["y"])