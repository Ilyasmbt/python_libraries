#dictionary as json

#json =python Dictionary

#json objects have the same format as python dictionaries

#load a python dictionary into a dataframe?

import pandas as pd

data = {
    "duration":{
        "0":60,
        "1":55,
        "2":33,
        "3":44,
        "4":55,
        "5":60
    },

    "pulse":{
        "0":160,
        "1":155,
        "2":133,
        "3":144,
        "4":155,
        "5":160
    },

    "MAxpulse":{
        "0":260,
        "1":255,
        "2":233,
        "3":44,
        "4":55,
        "5":60
    },
}

df=pd.DataFrame(data)
print(df)
