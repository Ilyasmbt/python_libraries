#info about the data

#the DATAFRAME objct has a method called info(),
#that gives you more information about the data set


#print information about the data ?

import pandas as pd

dd=pd.read_csv('data.csv')
print(dd.info())