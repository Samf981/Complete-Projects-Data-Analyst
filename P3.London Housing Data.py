# London Housing Data
#link https://www.kaggle.com/datasets/rohitgrewal/london-housing-data/data

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Import dataset
data=pd.read_csv("London Housing Data.csv")
#print(data.isnull().sum())

#Q.1) Convert the Datatype of 'Date' column to Date-Time format.

data.date = pd.to_datetime(data.date)
#print(data.dtypes)

#Q.2.A) Add a new column ''year'' in the dataframe, which contains years only.

data['year'] = data.date.dt.year    #This works if the data.date is already in datetime64 format. dt allows to acess .year; .month; .day...
#print(data.head(2))

#Q.2.B) Add a new column ''month'' as 2nd column in the dataframe, which contains month only.
data.insert(1,'month', data.date.dt.month)
#print(data.head(2))

#Q.3) Remove the columns 'year' and 'month' from the dataframe
data.drop(columns = 'month', inplace = True)
data.drop(columns = 'year', inplace = True)
#or:data.drop( ['month' , 'year'] , axis=1 , inplace = True )

#Q.4) Show all the records where 'No. of Crimes' is 0. And, how many such records are there ?
data1=data[(data['no_of_crimes'] == 0)]
#print(len(data1))

#Q.5) What is the maximum & minimum 'average_price' per year in england 

data['year'] = data.date.dt.year
data2 = data[data.area == 'england']
#print(data2.groupby('year')['average_price'].min())
#print(data.groupby('year')['average_price'].max())

#Q.6) What is the Maximum & Minimum No. of Crimes recorded per area ?
#print(data.groupby('area')['no_of_crimes'].min().sort_values(ascending=False))

#Q.7) Show the total count of records of each area, where average price is less than 100000
#print(data.head(3))
#data3=data[(data['average_price'] < 100000)]

#print(data3.groupby('area'))
print(data[data.average_price < 100000].area.value_counts())
#data.average<100000 creates a boolean table (false,true). Then the data. only shows the values TRUE
#.area              we filter the collumn
#.value_counts()    count the unique values