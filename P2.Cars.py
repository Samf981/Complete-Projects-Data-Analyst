# Cars_Data_Analysis
#link https://github.com/datasciencelovers/Project-2_Cars_Data_Analysis/tree/main

import pandas as pd
import seaborn as sns     

#Import dataset
data=pd.read_csv("2. Cars Data.csv")


#Q.1.Find all null values in the dataset. If there is any null value, fill it with mean value of column
#print(data.isnull().sum())
#data['Cylinders'].fillna(data['Cylinders'].mean(), inplace = True)
#print(data.isnull().sum())

#Q.2.Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data ?
#print(data['Make'].value_counts())

#Q.3.Show all the records where Origin is Asia or Europe.
data1=data[(data['Origin'] == 'Asia') | (data['Origin'] == 'Europe')]
#print(len(data1))

#Q.4.Remove all the records (rows) where Weight is above 4000.
data2=data[(data['Weight'] <=4000)]
#print(len(data2))

#Q.5. Increase all the values of 'MPG_City' column by 3.
#print(data.head(5))
#data["MPG_City"] = data["MPG_City"] + 3
#print(data.head(5))