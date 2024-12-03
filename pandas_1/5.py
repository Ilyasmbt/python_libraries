#create a seriess using only data from "day1" and "day3"?

import pandas as pd

calories={"day1":452,"day2":380,"day3":654}

my_var=pd.Series(calories,index=["day1","day3"])

print(my_var)