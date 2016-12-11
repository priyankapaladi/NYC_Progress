
# coding: utf-8

# # Statuses of various complaints!
# # Statuses of complaints wrt agency!

# In[1]:

import pandas as pd
import numpy as np
from datetime import datetime,timedelta,date
import calendar



# In[ ]:




# In[ ]:

#statuses of various complaints


# In[2]:

dataframe = pd.read_csv('F:/Python_Project/1000linesfile.csv')
dataframe2 = dataframe.drop(['School Not Found','School or Citywide Complaint','Vehicle Type','Taxi Company Borough','Taxi Pick Up Location','Bridge Highway Name','Bridge Highway Direction','Road Ramp','Bridge Highway Segment','Garage Lot Name','Ferry Direction','Ferry Terminal Name','Location','Latitude','Longitude'],axis=1)

dataframe3 = dataframe2[dataframe2['Agency'].notnull() & (dataframe2['Status'].notnull())].groupby(['Status', 'Complaint Type'])["Complaint Type"].count().reset_index(name="count")
dataframe3.sort_values(by='Status', ascending=0).reset_index(drop =True)


# In[ ]:

#statuses of various complaints wrt agencies and boroughs


# In[3]:


dataframe3 = dataframe2[dataframe2['Agency'].notnull() & (dataframe2['Status'].notnull())].groupby(['Status', 'Agency','Borough'])["Agency"].count().reset_index(name="count")
dataframe3.sort_values(by='Status', ascending=0).reset_index(drop =True)


# In[39]:

# group wrt agencies and boroughs
# enter borough
borough_input = input("Please enter borough: ")
if borough_input == "":
    print("Please enter borough")
else:
    borough = borough_input.upper()
    dataframe3 = dataframe2[dataframe2['Agency'].notnull() & (dataframe2['Status'].notnull()) & (dataframe2['Borough'].str.contains(borough))].groupby(['Status', 'Agency'])["Agency"].count().reset_index(name="count")
    dataframe3.sort_values(by='Status', ascending=0).reset_index(drop =True)
dataframe3


# In[45]:

# enter borough
boroughip = input("Please enter borough: ")
if boroughip == "":
    print("No borough entered")
    dataframe_all_borough = dataframe2[dataframe2['Agency'].notnull() & (dataframe2['Status'].notnull())].groupby(['Status', 'Borough'])["Status"].count().reset_index(name="count")
    plot_borough_status()
else:
    boroughip = boroughip.upper()
    dataframe_borough = dataframe2[dataframe2['Agency'].notnull() & (dataframe2['Status'].notnull()) & (dataframe2['Borough'].str.contains(borough))].groupby(['Status', 'Borough'])["Status"].count().reset_index(name="count")
    dataframe_borough = dataframe_borough.sort_values(by='Status', ascending=0).reset_index(drop =True)
    plot_borough_all()
dataframe_borough



# In[ ]:




# In[41]:

# %matplotlib inline
# import matplotlib.pyplot as plt
# import seaborn as sns
# cm = plt.cm.get_cmap('RdYlBu_r')

# dfall.plot.hist(alpha=0.5)
# plt.xlabel("weightage - (Quick in closing the issue)")
# plt.ylabel("Complaint Types")
# plt.suptitle(" Inefficiency of the agencies wrt to complaints (Inefficient Agencies)", y=1.2, fontsize=24)
# plt.title("Based on NYC 311 reuqests for the year 2015",y=1.1, fontsize=18)
# plt.savefig("F:/Python_Project/Analysis4/Images/inefficient_agencies.png", bbox_inches='tight')


def plot_borough_status():
    dfall = dataframe_all_borough.pivot(index='Status', columns='Borough', values='count')
    dfall

    dfall = dfall.fillna(0)
    dfall

    get_ipython().magic('matplotlib inline')
    import matplotlib.pyplot as plt
    import seaborn as sns

    #plt.figure(figsize=(25,8))
    dfp = dfall.cumsum()
    plt.figure(figsize=(15,15))
    dfall.plot()
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=2)
    #sns.barplot(x="Borough", y="count", hue="Status", data=dataframe_all_borough)
    plt.xlabel("Borough")
    plt.ylabel("Count of complaints with their statuses")
    plt.legend(loc= 'upper left', bbox_to_anchor=(1, 1))

    plt.suptitle("Complaints and their statuses", y=1.3, fontsize=24)
    plt.title("Based on NYC 311 reuqests for the year 2015",y=1.2, fontsize=18)
    plt.xticks(rotation=50)
    plt.savefig("F:/Python_Project/Analysis5/Images/"+boroughip+"complaints_statuses.png", bbox_inches='tight')


# In[42]:

def plot_borough_all():
    get_ipython().magic('matplotlib inline')
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(25,8))
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=2)
    sns.barplot(x="Status", y="count", data=dataframe_borough)
    plt.xlabel("Borough")
    plt.ylabel("Count of complaints with their statuses")
    plt.legend(loc= 'upper left', bbox_to_anchor=(1, 1))

    plt.suptitle("Complaints and their statuses for "+ borough, y=1.3, fontsize=24)
    plt.title("Based on NYC 311 reuqests for the year 2015",y=1.2, fontsize=18)
    plt.xticks(rotation=50)
    plt.savefig("F:/Python_Project/Analysis5/Images/"+" complaints_statuses.png", bbox_inches='tight')


# In[ ]:



