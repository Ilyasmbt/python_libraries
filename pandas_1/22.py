#create a csv file??

import pandas as pd
import numpy as np

data ={ 'Duration':[60,606,50,67],
        'date':[np.nan,np.nan,'2020/11/09','2024/11/11'],


        "pulse":[110,111,117,278],
        "maxPulse":[130,130,150,250],
        "calories":[409,409.1,np.nan,230.0]

}
df=pd.DataFrame(data)
print(df)
df.to_csv('createNew.csv')