# Airlines Flights Data
#link https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data

# The Flights Booking Dataset of various Airlines is a scraped datewise from a famous website in a structured format. 
# The dataset contains the records of flight travel details between the cities in India. 
# Here, multiple features are present like Source & Destination City, Arrival & Departure Time, Duration & Price of the flight etc.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import dataset
data=pd.read_csv("airlines_flights_data.csv")
#data.info()        #Info about dataset
#data.describe()    #Count, Mean...

#Remove index collumn
data.drop(columns = 'index', inplace = True)

#Get exact value from any column
#data[data['duration']==2.17]

#Check for the missing values in any collumn
data.isnull().sum()

#Q.1. What are the airlines in the dataset, accompanied by their frequencies?¶

#How many airlines?
data['airline'].nunique()       #result: 6

#Show the names of the airlines
#print(data['airline'].unique())

#Show the names of the airlines and their frequencies
#print(data['airline'].value_counts())

# Showing all the Airlines with their Number of Flights in Horizontal Bar Graph
#data['airline'].value_counts(ascending=True).plot.barh( color = ['lightgreen', 'lightblue'])
#plt.title("Airlines with frequencies")
#plt.xlabel(" Number of flights")
#plt.ylabel(" Airlines")
#plt.show()

#Q.2. Show Bar Graphs representing the Departure Time & Arrival Time
departure_time=data['departure_time'].value_counts()
arrival_time=data['arrival_time'].value_counts()
"""
plt.figure(figsize = (16,4))

#using the subplot to show 2 graphs

plt.subplot(1,2,1)
plt.bar( data['departure_time'].value_counts().index , data['departure_time'].value_counts().values, color = ['r', 'b'] )
plt.title("Departure Time")
plt.xlabel("D. Time")
plt.ylabel("D. Freq")

plt.subplot(1,2,2)

plt.bar( data['arrival_time'].value_counts().index, data['arrival_time'].value_counts().values, color = ['g', 'y'])
plt.title("Arrival Time")
plt.xlabel("A. Time")
plt.ylabel("A. Freq")
"""


#Q.3. Show Bar Graphs representing the Source City & Destination City
#using the subplot to show 2 graphs
"""
plt.subplot(1,2,1)
plt.barh( data['source_city'].value_counts().index , data['source_city'].value_counts().values, color = ['r', 'b'] )
plt.title("Source Cities")
plt.xlabel("Cities")
plt.ylabel("Freq.")

plt.subplot(1,2,2)

plt.barh( data['destination_city'].value_counts().index, data['destination_city'].value_counts().values, color = ['g', 'y'])
plt.title("Arrival Cities")
plt.xlabel("Cities")
plt.ylabel("Freq")
plt.show()
"""
#Q.4. Does price varies with airlines ?

#Group airlines and check mean price
#print(data.groupby('airline')['price'].mean())

# Drawing a Categorical Plot
#sns.catplot( x = 'airline', y = 'price', kind = 'bar', palette = 'rocket', data = data, hue = 'class')
#plt.show()

#Q.5. Does ticket price change based on the departure time and arrival time?
#Check the mean price on departure
dep_price=data.groupby('departure_time')['price'].mean()
arr_price=data.groupby('arrival_time')['price'].mean()

#sns.catplot( x = 'departure_time', y = 'price', kind = 'bar', data = data, hue = 'class')
#sns.relplot( x = 'arrival_time', y = 'price',  data = data, col='departure_time', kind = 'line')
#plt.show()

#Q.6. How the price changes with change in Source and Destination?
#print(data.groupby('source_city')['price'].mean())

#sns.relplot( x = 'source_city', y = 'price',  data = data, col='destination_city', kind = 'line')
#plt.show()

#Q.7. How is the price affected when tickets are bought in just 1 or 2 days before departure?
#Get list (array) with unique elements in days_left
#print(data['days_left'].unique())  

#Mean of price groped by days
"""
print(data.groupby('days_left')['price'].mean())

sns.relplot( y='price', x = 'days_left', kind = 'line', data = data )
plt.show()
"""

#Q.8. How does the ticket price vary between Economy and Business class?
#print(data.groupby('class')['price'].mean())

#Q.9. What will be the Average Price of Vistara airline for a flight from Delhi to Hyderabad in Business Class ?

#Create new db with flights from Vistara 

data1=data[(data['airline'] == 'Vistara') & (data['source_city'] == 'Delhi') & (data['destination_city'] == 'Hyderabad') & (data['class'] == 'Business')]
print(data1['price'].mean())