#max_rows
#the number of rows returned is defined in pandas option setting

#you can check your system's maximum rows
#with the pd.option.display.max_rows statement

#check the number of maximum returned rows?



import pandas as pd
print(pd.options.display.max_rows)

#in my system the num is 60,
#which means that if the DAtaframe contains more than 60 rows,
#the print(df) stmnt will return only the header and the first and last 5 row