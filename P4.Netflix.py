# Netflix Data Analysis with Python
#link https://www.kaggle.com/code/rohitgrewal/netflix-data-analysis-with-python

#This Netflix Dataset has information about the TV Shows and Movies available on Netflix till 2021.

import pandas as pd
import seaborn as sns  
import matplotlib.pyplot as plt

#Import dataset
data=pd.read_csv("Netflix Dataset.csv")

#print(data.head(5))
#print(data.shape)
#print(data.tail(5))
#print(data.info())
#print(data.columns)
#print(data.dtypes)


#Task.1. Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.

#print(data.duplicated().sum())  #Show nº of duplicated rows
#print(data[data.duplicated()])  #Show the duplicated cores

data.drop_duplicates(inplace=True)
#print(data[data.duplicated()])

#Task.2. Is there any Null Value present in any column ? Show with Heat-map.

#print(data.isnull().sum())
#sns.heatmap(data.isnull())
#plt.show()

#Q.1. For 'House of Cards', what is the Show Id and Who is the Director of this show ?

data1=data[(data['Title'] == 'House of Cards')]
#or data[data['Title'].str.contains('House of Cards')]  # or data[data['Title'].isin(['House of Cards'])] 

#Q.2. In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.

#print(data.Category.value_counts()) #There are only 2 show: Movie and TV show
#print(data.dtypes)          #Release_Date is object

#Convert object to datetime64
data['Release_Date']=pd.to_datetime(data['Release_Date'], format = 'mixed')

#Add a column and group
data['year'] = data['Release_Date'].dt.year 
#print(data['year'].value_counts())

"""
plt.bar(data['year'].value_counts().index, data['year'].value_counts().values, color = ['b', 'b'])
#or: data['Release_Date'].dt.year.value_counts().plot(kind='bar')   #bar graph for one variable
plt.title("Nº Releases per Year")
plt.xlabel("Years")
plt.ylabel("Count")
plt.show()
"""
# Q.3. How many Movies & TV Shows are in the dataset ? Show with Bar Graph
data_m=data[(data['Category'] == 'Movie')]
data_t=data[(data['Category'] == 'TV Show')]

"""
plt.bar(1, len(data_m), color='#7f6d5f', label='Movies')
plt.bar(2, len(data_t), color='#557f2d', label='TV Shows')
plt.title("Shows")
plt.xlabel("Type of Shows")
plt.ylabel("Count")
"""

#sns.countplot(data['Category'])     # Counts and automatically gives the graph
#plt.show()

#Q.4. Show all the Movies that were released in year 2030.

#Convert the collumn year from float to integer
"""
data3 = data.dropna(subset=['year'])     #There are year with missing values. I need to eliminate this collumns before converting ot int
data3['year'] = data3['year'].astype('int')
data4=data3[(data3['Category'] == 'Movie') & (data3['year'] == 2020)]
print(len(data4))
"""


#Q.5. Show only the Titles of all TV Shows that were released in India only

#data2=data[(data['Country'] == 'India') & (data['Category'] == 'TV Show')]
#print(data2['Title'])

#Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix 

#print(data['Director'].value_counts().head(10))

#Q.7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom

#data2=data[((data['Category'] == 'Movie') & (data['Type'] == 'Comedies'))| (data['Country'] == 'United Kingdom')]


#Q.9. What are the different Ratings defined by Netflix 
#print(data['Rating'].unique())

#Q.9.1. How many Movies got the 'TV-14' rating, in Canada 

#print(len(data[((data['Rating'] == 'TV-14') & (data['Category'] == 'Movie') & (data['Country'] == 'Canada'))]))

#Q9.2 How many TV Show got the 'R' rating, after year 2018 ?
#print(len(data[((data['Rating'] == 'R') & (data['year'] > 2018) & (data['Category'] == 'TV Show'))]))

#Q.10. What is the maximum duration of a Movie/Show on Netflix (only compare the lines with minutes - not seasons)
#print(data.Duration.dtypes)        # or:  #print(data['Duration'].dtypes)

#Convert object to Data64 format:
data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand = True)

#print(data['Minutes'].max())
# data['Minutes'].mean()

#Q.11. Which individual country has the Highest No. of TV Shows ?

#data2=data[(data['Category']== 'TV Show')]
#print((data2['Country'].value_counts()))

#Q.12. How can we sort the dataset by Year ?
#print(data.sort_values(by = 'year', ascending = False).head(10))

##Q.13. Find all the instances where :Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'
#data3=data[((data['Category']=='Movie') & (data['Type']=='Dramas')) | ((data['Category']=='TV Show') & (data['Type']== "Kids' TV"))]
#print(data['Type'].value_counts())
#print(len(data3))