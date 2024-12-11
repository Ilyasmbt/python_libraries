import pandas as pd
#right join
#data for the first dataframe

dict1={
    'id':[1,2,3,4,5,6],
    'fname':['anu','jk','abu','aju'],
    'lname':['roserose','kallu','ammi','knr'],
    'age':[10,22,33,44]





}
dic12={'id':[1,2,3,4,5,6],
     'fname':['anu','jeni','kiran','rahul','jack','lilly'],
     'lname':['rose','k','j','das','joy','maria'],
     'age':[23,34,44,35,27,43]}

dic2={'prof':['python','python','bigdata','bigdata','java','java'],
      'salary':[2500,3400,2300,4500,3000,5000],
      'id':[4,5,6,7,8,9],
      'loc':['kannur','kozhikode','malappuram','kochi','alappuzha','kannur']}
#create dataframes
df1=pd.DataFrame(dic12)
df2=pd.DataFrame(dic2)

print("Dataframe 1:")
print (df1)
print("*" * 100)

print("Dataframe 2:")
print(df2)
print("*" * 100)


#perform inner join on id and select specific column
result=pd.merge(df1,df2, on='id', how='right')     #merge
print (result)