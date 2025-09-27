# Weather Data
#link https://www.kaggle.com/datasets/rohitgrewal/weather-data/data/code

#The Weather Dataset is a time-series data set with per-hour information about the weather conditions at a particular location. 
#It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure, and Conditions.
#This data is available as a CSV file. We have analysed this data using the Pandas library.

import pandas as pd



#Import dataset
data=pd.read_csv("Project 1 - Weather Dataset.csv")

#Analyse the data
#df.head(5)
#df.shape()
#df.info()
#df.dtypes
#df.index
#df.columns

#Q. 1) Find all the unique 'Wind Speed' values in the data.
data['Wind Speed_km/h'].unique()


#Q) 2. Find the number of times when the 'Weather is exactly Clear'.

#print((data['Weather'] == 'Clear').sum())

#Additionally - Only get table with weather==Clear
#print(data.groupby('Weather').get_group('Clear'))


#Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.
#print((data['Wind Speed_km/h'] == 4).sum())


#Q) 4. Find out all the Null Values in the data.
#print(data.isnull().sum())

#Q) 5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


#Q) 6. What is the mean 'Visibility' ?
#print(data['Visibility_km'].mean())


#Q. 7) What is the Standard Deviation of 'Pressure' in this data?
#print(data['Press_kPa'].std())

#Q. 8) What is the Variance of 'Relative Humidity' in this data ?
#print(data['Rel Hum_%'].var())


#Q. 9) Find all instances when 'Snow' was recorded.

#print(data.groupby('Weather Condition').get_group('Snow'))
#print((data['Weather Condition'] == 'Snow').sum())

#Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'

data1=data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
#print(data1)

#Q. 11) What is the Mean value of each column against each 'Weather Condition' ?

#print(data.groupby('Weather Condition').mean('numeric_only'))

#Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition' ?
#print(data.groupby('Weather Condition').min())
#print(data.groupby('Weather Condition').max())

#Q. 13) Show all the Records where Weather Condition is Fog.
#print(data.groupby('Weather Condition').get_group('Fog'))

#Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
data2=data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]
#print(data2)

#Q. 15) Find all instances when :
data3=data[((data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]
print(data3)
