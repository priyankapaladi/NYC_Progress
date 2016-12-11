
# coding: utf-8

# # Finding which borough has more complaints
# # Find which complaint has been registered more number of times in that borough
# # Find in what month more complaints have been registered on the complaint which is been registered more number of times

# In[ ]:




# # We can find which borough has more number of issues!
# # We can also check number of complaints (based on categories) in each borough.
# # We can check the time taken to solve(close) the particular issue in that borough and also calculate the average time taken to close the issue
# # We can check the number of complaints in a borough with respect to the complaint

# In[10]:

import pandas as pd
import numpy as np
import datetime as dt
import calendar


# # Let's see which borough is facing more issues

# In[11]:

dataframe = pd.read_csv('F:/Python_Project/1000linesfile.csv')
#df.to_csv(filename ,  index = False)
dataframe2 = dataframe.drop(['School Not Found','School or Citywide Complaint','Vehicle Type','Taxi Company Borough','Taxi Pick Up Location','Bridge Highway Name','Bridge Highway Direction','Road Ramp','Bridge Highway Segment','Garage Lot Name','Ferry Direction','Ferry Terminal Name','Location','Latitude','Longitude'],axis=1)

dataframe2['Created Date'] = pd.to_datetime(dataframe2['Created Date'])
dataframe2['Closed Date'] = pd.to_datetime(dataframe2['Closed Date'])

dataframe2['Time'] = dataframe2['Closed Date'] - dataframe2['Created Date']
dataframe2['weekday'] = dataframe2['Created Date'].dt.dayofweek
days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
dataframe2['day_of_week'] = dataframe2['weekday'].apply(lambda x: days[x])


# get the highest number of complaints with respect to borough /  or the one you want to check
dataframe3 = dataframe2[['Agency', 'Created Date', 'Complaint Type', 'Time', 'Borough']].groupby(['Borough'])["Borough"].count().reset_index(name="count").sort_values(by='count', ascending=0)
dataframe3 = dataframe3.reset_index(drop = False)
dfborough = dataframe3
dfborough
dfborough.to_csv("F:/Python_Project/Analysis1/CSV/Complaints_wrt_boroughs.csv" ,  index = False)


# In[12]:

get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20,8))
sns.set_style("whitegrid")    # Set style for seaborn output
sns.set_context("notebook", font_scale=2)
sns.barplot(x="Borough", y="count", data=dfborough)
plt.xlabel("Borough")
plt.ylabel("Number of complaints by each borough")
plt.suptitle("Let's see which borough is facing more issues", y=1.05, fontsize=32)
plt.title("Based on NYC 311 reuqests for the year 2015", fontsize=18)
plt.xticks(rotation=60)
plt.savefig("F:/Python_Project/Analysis1/Images/borough_issues.png", bbox_inches='tight')


# In[ ]:




# # Lets check the complaints in each borough

# In[13]:

print("Please enter the borough. If you do not enter, the borough with highest complaints will be consisdered!")
borough_input = input('Please enter which boroughs complaints you want to check:  ')

if borough_input == "":
    borough = dfborough.ix[0,'Borough']
    print("Borough with more complaints:  ", borough)
else:
    borough = borough_input.upper()
    
dataframe3 = dataframe2[['Agency', 'Created Date', 'Complaint Type', 'Time', 'Borough']]
dataframe3 = dataframe3[dataframe3['Borough'] == borough].groupby(['Complaint Type'])["Complaint Type"].count().reset_index(name="count").sort_values(by='count', ascending=0)
dataframe3 =dataframe3.reset_index(drop = False)
dfcomplaints = dataframe3
dfcomplaints
filepath = "F:/Python_Project/Analysis1/CSV/Complaints with respect to particular boroughs.csv"
dfcomplaints.to_csv(filepath ,  index = False)


# In[15]:

get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20,20))
sns.set_style("whitegrid")    # Set style for seaborn output
sns.set_context("notebook", font_scale=2)
sns.barplot(x="count", y="Complaint Type", data=dfcomplaints)
plt.xlabel("Number of complaints based on each category")
plt.ylabel("Various Complaint Categories")
plt.suptitle("Various complaints in a borough: "+borough, y=1.05, fontsize=32)
plt.title("Based on NYC 311 reuqests for the year  2015", fontsize=18)
plt.xticks(rotation=60)
filepath = "F:/Python_Project/Analysis1/Images/complaints_count.png"

plt.savefig(filepath, bbox_inches='tight')


# In[ ]:




# # Lets see how long it takes to solve the complaint

# In[20]:

print("Please enter the borough. If you do not enter, the borough with highest complaints will be consisdered!")
borough_input = input('Please enter the borough of which you want to check complaints of:  ')

if borough_input == "":
    borough = dfborough.ix[0,'Borough']
    print("Borough with more complaints:  ", borough)
else:
    borough = borough_input.upper()


#get the type of complaint which is reported more number of times / or the one you want to check
print("Please enter the complaint type. If you do not enter, the complaint type with highest count will be consisdered!")
complaint_input = input('Please enter which complaint you want to check in the borough entered:  ')

if complaint_input == "":
    complaint = dfcomplaints.ix[0,'Complaint Type']
    print("More complaints are of type:  ",complaint)

else:
    complaint = complaint_input.title()

# get the time required to solve the above complaint
dataframe3 = dataframe2[dataframe2['Agency'].notnull()  & dataframe2['Closed Date'].notnull() & (dataframe2['Borough'] == borough) & (dataframe2['Complaint Type'].str.contains(complaint))]
# dataframe3['date'] = dataframe3['Created Date'].dt.date
# dataframe3['hours'] = dataframe3['Created Date'].dt.time
# dataframe3['time_days'] = dataframe3['Time'].apply(lambda x: x.days)

dataframe3['Month'] = dataframe2['Created Date'].dt.month
dataframe3['Month'] = dataframe3['Month'].apply(lambda x: calendar.month_abbr[x])
dataframe3 = dataframe3[['Agency', 'Created Date','Month','Complaint Type', 'Time', 'Borough']]



# get the average time required to solve the complaint
average_time = dataframe3['Time'].mean()
print('Average Time taken to solve that complaint: ', average_time)

dfaveragetime = dataframe3
dfaveragetime=dfaveragetime.rename(columns = {'Time':'Time Taken to Close'})

filepath = "F:/Python_Project/Analysis1/CSV/TimeToSolve_complaint.csv"
dfaveragetime.to_csv(filepath ,  index = False)

dfaveragetime


# # Get the number of complaints in every month based on the user input for complaint and the borough
# 
# 
# 

# In[21]:

# get the number of complaints in every month

print("Lets get number of complaints in every month based on the user input for complaint and the borough")
print("Please enter the borough. If you do not enter, the borough with highest complaints will be consisdered!")
borough_input = input('Please enter which boroughs complaints you want to check:  ')

if borough_input == "":
    borough = dfborough.ix[0,'Borough']
    print("Borough with more complaints:  ", borough)
else:
    borough = borough_input.upper()
    
print("Please enter the complaint type. If you do not enter, the complaint type with highest count will be consisdered!")
complaint_input = input('Please enter which boroughs complaints you want to check:  ')

if complaint_input == "":
    complaint = dfcomplaints.ix[0,'Complaint Type']
    print("More complaints are of type:  ",complaint)
else:
    complaint = complaint_input.title()

    
dataframe3 = dataframe2[dataframe2['Agency'].notnull()  & dataframe2['Closed Date'].notnull() & (dataframe2['Borough'] == borough) & (dataframe2['Complaint Type'].str.contains(complaint))]

dataframe3['Month'] = dataframe2['Created Date'].dt.month
dataframe3['Month'] = dataframe3['Month'].apply(lambda x: calendar.month_abbr[x])
dataframe3 = dataframe3[['Agency', 'Created Date','Month','Complaint Type', 'Time', 'Borough']]


dfmonthcount = dataframe3.groupby(['Month','Borough','Complaint Type'])['Month'].count().reset_index(name="count")

filepath = "F:/Python_Project/Analysis1/CSV/complaints(per month)_borough.csv"
dfmonthcount.to_csv(filepath ,  index = False)


# In[8]:

dfmonthcount


# In[ ]:




# In[ ]:




# In[23]:

get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20,8))
sns.set_style("whitegrid")    # Set style for seaborn output
sns.set_context("notebook", font_scale=2)
sns.barplot(x="Month", y="count", data=dfmonthcount)
plt.xlabel("Complaints in every month with respect to the complaint in a borough")
plt.ylabel("Number of complaints per month")
plt.suptitle("Complaints per month based on the complaint and borough: "+borough +"-"+complaint, y=1.05, fontsize=32)
plt.title("Based on NYC 311 reuqests for the year 2015", fontsize=18)
plt.xticks(rotation=60)
plt.savefig("F:/Python_Project/Analysis1/Images/complaintspermonth.png", bbox_inches='tight')


# In[ ]:



