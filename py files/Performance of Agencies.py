
# coding: utf-8

# # Check if the complaints were closed before Due date!
# # Success rate = How many very solved by the agency before time out of total number of complaints!
# 
# # Calculate the offset between due date and closed date with respect to agency! To get the most efficiently working agency
# 

# In[ ]:




# In[24]:

import pandas as pd
import numpy as np
import datetime as dt
import calendar

dataframe = pd.read_csv('F:/Python_Project/1000linesfile.csv', low_memory = False)
#df.to_csv(filename ,  index = False)

dataframe2 = dataframe.drop(['School Not Found','School or Citywide Complaint','Vehicle Type','Taxi Company Borough','Taxi Pick Up Location','Bridge Highway Name','Bridge Highway Direction','Road Ramp','Bridge Highway Segment','Garage Lot Name','Ferry Direction','Ferry Terminal Name','Location','Latitude','Longitude'],axis=1)

dataframe2['Created Date'] = pd.to_datetime(dataframe2['Created Date'])
dataframe2['Closed Date'] = pd.to_datetime(dataframe2['Closed Date'])
dataframe2['Due Date'] = pd.to_datetime(dataframe2['Due Date'])

dataframe2['Time Left'] = (dataframe2['Due Date'] - dataframe2['Closed Date']).dt.days
dataframe2['Month'] = pd.to_datetime(dataframe2['Created Date']).dt.month.apply(lambda x: calendar.month_abbr[x])
dataframe2['weekday'] = dataframe2['Created Date'].dt.dayofweek

days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

dataframe2['day_of_week'] = dataframe2['weekday'].apply(lambda x: days[x])

dataframe3 = dataframe2[dataframe2['Agency'].notnull()  & dataframe2['Closed Date'].notnull() & dataframe2['Due Date'].notnull()]


dataframe3['Time'] = dataframe3['Closed Date'] - dataframe3['Created Date']

dataframe3 = dataframe3[['Agency','Complaint Type', 'Time Left']].groupby(['Agency','Complaint Type']).mean().reset_index()
dataframe3 = dataframe3.sort_values(by='Time Left', ascending=0)


dataframe4 = dataframe2[dataframe2['Agency'].notnull()  & dataframe2['Closed Date'].notnull() & dataframe2['Due Date'].notnull()]
dataframe4 = dataframe4[['Agency','Complaint Type', 'Time Left']].groupby(['Agency','Complaint Type'])['Complaint Type'].count().reset_index(name="count")


# In[ ]:




# In[30]:



dataframe_new = pd.merge(dataframe3, dataframe4, on='Complaint Type')
dataframe_new = dataframe_new.T.drop_duplicates().T.sort_values(by='Time Left', ascending=0)
dataframe_new.columns = ['Agency','Complaint Type', 'Efficiency in %', 'count']
dataframe_new
dataframe_new.to_csv("F:/Python_Project/Analysis4/CSV/efficiency of agency.csv" ,  index = False)


# In[ ]:




# In[ ]:




# In[33]:

df_good = dataframe_new[dataframe_new['Efficiency in %'] >= 0]
df_bad = dataframe_new[dataframe_new['Efficiency in %'] < 0]

df_good.to_csv("F:/Python_Project/Analysis4/CSV/efficiency of agency_GOOD.csv" ,  index = False)
df_bad.to_csv("F:/Python_Project/Analysis4/CSV/efficiency of agency_BAD.csv" ,  index = False)




# In[46]:

get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20,23))
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=2)
sns.barplot(x="Efficiency in %", y="Complaint Type", data=df_good)
plt.xlabel("weightage - (Quick in closing the issue)")
plt.ylabel("Complaint Types")
plt.suptitle(" Efficiency of the agencies wrt to complaints (Efficient Agencies)", y=1, fontsize=25)
plt.title("Based on NYC 311 reuqests for the year 2015", fontsize=18)
plt.savefig("F:/Python_Project/Analysis4/Images/efficient_agencies.png", bbox_inches='tight')


# In[47]:

get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20,23))
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=2)
sns.barplot(x="Efficiency in %", y="Complaint Type", data=df_bad)
plt.xlabel("weightage - (Quick in closing the issue)")
plt.ylabel("Complaint Types")
plt.suptitle(" Inefficiency of the agencies wrt to complaints (Inefficient Agencies)", y=1, fontsize=32)
plt.title("Based on NYC 311 reuqests for the year 2015",y=0.75, fontsize=18)
plt.savefig("F:/Python_Project/Analysis4/Images/inefficient_agencies.png", bbox_inches='tight')


# In[ ]:



