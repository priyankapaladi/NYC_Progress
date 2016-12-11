
# coding: utf-8

# # Time series for each complaint type / all of them (And days of a week)
# 

# In[1]:

import pandas as pd
import numpy as np
import datetime as dt
import calendar


# In[ ]:




# In[2]:


dataframe = pd.read_csv('F:/Python_Project/1000linesfile.csv')
#df.to_csv(filename ,  index = False)
dataframe2 = dataframe.drop(['School Not Found','School or Citywide Complaint','Vehicle Type','Taxi Company Borough','Taxi Pick Up Location','Bridge Highway Name','Bridge Highway Direction','Road Ramp','Bridge Highway Segment','Garage Lot Name','Ferry Direction','Ferry Terminal Name','Location','Latitude','Longitude'],axis=1)
dataframe2.head()


# In[3]:

dataframe2['Created Date'] = pd.to_datetime(dataframe2['Created Date'])
dataframe2['Closed Date'] = pd.to_datetime(dataframe2['Closed Date'])

dataframe2['Time Taken'] = dataframe2['Closed Date'] - dataframe2['Created Date']

# complaint created on what month of the year
dataframe2['Month'] = dataframe2['Created Date'].dt.month

dataframe2['Month'] = dataframe2['Month'].apply(lambda x: calendar.month_abbr[x])
#get only date
dataframe2['date'] = dataframe2['Created Date'].dt.date
#get only time
dataframe2['hours'] = dataframe2['Created Date'].dt.time

#get only hour and minute
dataframe2['only_hour'] = dataframe2['Created Date'].dt.hour
dataframe2['only_min'] = dataframe2['Created Date'].dt.minute

dataframe2['approx_min'] = np.where(dataframe2['only_min']>=30, 1, 0) # 1 if its above 30 else 0
dataframe2['hr'] = dataframe2['only_hour'] + dataframe2['approx_min']


# complaint created on what day of the week
dataframe2['weekday'] = dataframe2['Created Date'].dt.dayofweek
days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
dataframe2['day_of_week'] = dataframe2['weekday'].apply(lambda x: days[x])

#get period of the day
times = list(range(8, 21, 4))
labels = ['morning', 'afternoon', 'evening', 'night']
periods = dict(zip(times, labels))
periods
#{8: 'morning', 16: 'evening', 12: 'afternoon', 20: 'night'}

def period(row):
    created_time = {'hour': row.Cd.hour, 'min': row.Cd.minute} # get hour, min of visit start
    for period_start, label in periods.items():
        period_end = period_start + 4
        if period_start <= created_time['hour'] < period_end:
            return label
        else:
            if 8>created_time['hour'] >= 0:
                return "early morning"
          

dataframe2['Cd'] = pd.to_datetime(dataframe['Created Date'])

dataframe2['period'] = dataframe2.apply(period, axis=1)



# In[ ]:




# In[ ]:




# In[ ]:




# # All complaints w.r.t days, months, periods

# In[32]:

dataframe3 = dataframe2[['Agency', 'day_of_week', 'Created Date', 'Complaint Type', 'Time Taken', 'Borough', 'Month', 'period' ]]
# days
dfday = dataframe3.groupby(['day_of_week','Borough'])['day_of_week'].count().reset_index(name="count").sort_values(by='Borough', ascending=1)
# months
dfmonth = dataframe3.groupby(['Month','Borough'])['Month'].count().reset_index(name="count").sort_values(by='Borough', ascending=1)
#periods
dfperiod = dataframe3.groupby(['period','Borough'])['period'].count().reset_index(name="count").sort_values(by='Borough', ascending=1)
dfperiod

filename = "F:/Python_Project/Analysis3/CSV/"
dfday.to_csv(filename+"complaints_days.csv",  index = False)
dfmonth.to_csv(filename+"complaints_month.csv",  index = False)
dfperiod.to_csv(filename+"complaints_period.csv",  index = False)

dfperiod.head()





# In[ ]:

# %matplotlib inline
# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.figure(figsize=(25,8))
# sns.set_style("whitegrid")
# sns.set_context("notebook", font_scale=2)
# sns.barplot(x="Month", y="count", hue="Borough", data=dfmonth.sort_values(['Month', 'count']))
# plt.xlabel("Month of the year")
# plt.ylabel("Count of complaints")
# plt.suptitle("Complaints in each borough per month", y=1.05, fontsize=32)
# plt.title("Based on NYC 311 reuqests for the year 2015", fontsize=18)
# plt.xticks(rotation=50)
# plt.savefig("F:/Python_Project/Analysis3/Images/"+"complaints_month.png", bbox_inches='tight')


# %matplotlib inline
# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.figure(figsize=(25,8))
# sns.set_style("whitegrid")
# sns.set_context("notebook", font_scale=2)
# sns.barplot(x="day_of_week", y="count", hue="Borough", data=dfday.sort_values(['day_of_week', 'count']))
# plt.xlabel("Day of week")
# plt.ylabel("Count of complaints")
# plt.suptitle("Complaints in each borough per day of the week", y=1.05, fontsize=32)
# plt.title("Based on NYC 311 reuqests for the year 2015", fontsize=18)
# plt.xticks(rotation=50)
# plt.savefig("F:/Python_Project/Analysis3/Images/"+"complaints_day_of_week.png", bbox_inches='tight')


# %matplotlib inline
# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.figure(figsize=(25,8))
# sns.set_style("whitegrid")
# sns.set_context("notebook", font_scale=2)
# sns.barplot(x="period", y="count", hue="Borough", data=dfperiod.sort_values(['period', 'count']))

# plt.xlabel("Period of the day")
# plt.ylabel("Count of complaints")
# plt.suptitle("Complaints in each borough depending on the period of the day", y=1.05, fontsize=32)
# plt.title("Based on NYC 311 reuqests for the year 2015", fontsize=18)
# plt.xticks(rotation=50)
# plt.savefig("F:/Python_Project/Analysis3/Images/"+"complaints_period.png", bbox_inches='tight')

# import seaborn as sns
# sns.set()

# sns.pairplot(dfperiod, hue="Borough")


# In[28]:

dfp


# In[24]:

dfp = dfperiod.pivot(index='period', columns='Borough', values='count')

dfp
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

#dfperiod.plot.hist(alpha=0.5)
dfp = dfp.cumsum()
plt.figure(figsize=(15,15))
dfp.plot()
plt.xlabel("Period of the day")
plt.ylabel("Count of complaints")
plt.suptitle("Complaints in each borough depending on the period of the day", y=1.2, fontsize=28)
plt.title("Based on NYC 311 reuqests for the year 2015",y=1.1, fontsize=18)
plt.xticks(rotation=50)
plt.legend(loc= 'upper left', bbox_to_anchor=(1, 1))
plt.savefig("F:/Python_Project/Analysis3/Images/"+"complaints_period.png", bbox_inches='tight')


# In[26]:

dfd = dfday.pivot(index='day_of_week', columns='Borough', values='count')
dfd




# In[29]:

import matplotlib.pyplot as plt
import seaborn as sns

dfd = dfd.cumsum()
plt.figure(); 
dfd.plot();
plt.legend(loc= 'upper left', bbox_to_anchor=(1, 1))
plt.xlabel("day of the week")
plt.ylabel("Count of complaints")
plt.suptitle("Complaints in each borough depending on the day of the week", y=1.2, fontsize=28)
plt.title("Based on NYC 311 reuqests for the year 2015",y=1.1, fontsize=18)
plt.xticks(rotation=50)
plt.legend(loc= 'upper left', bbox_to_anchor=(1, 1))
plt.savefig("F:/Python_Project/Analysis3/Images/"+"complaints_day.png", bbox_inches='tight')



# In[25]:

dfm = dfmonth.pivot(index='Month', columns='Borough', values='count')


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

dfm = dfm.cumsum()
plt.figure(); 
dfm.plot();
plt.legend(loc= 'upper left', bbox_to_anchor=(1, 1))
plt.xlabel("Month")
plt.ylabel("Count of complaints")
plt.suptitle("Complaints in each borough depending on the month", y=1.2, fontsize=28)
plt.title("Based on NYC 311 reuqests for the year 2015",y=1.1, fontsize=18)
plt.xticks(rotation=50)
plt.legend(loc= 'upper left', bbox_to_anchor=(1, 1))
plt.savefig("F:/Python_Project/Analysis3/Images/"+"complaints_month.png", bbox_inches='tight')





# In[ ]:




# In[ ]:




# In[ ]:




# # Check trend in each borough w.r.t day

# In[50]:

# get the number of complaints with respect to day of the week and borough

#dataframe3 = dataframe2[dataframe2['Agency'].notnull()]

dataframe3 = dataframe2[['Agency', 'day_of_week','weekday', 'Created Date', 'Complaint Type', 'Time Taken', 'Borough','Month','period','hr' ]]
borough = input('Please enter: ')
print(borough)


# get the number of complaints with repect to day of the week
if borough=="":
    print("Please enter borough")

else:
    # get the number of complaints with repect to day of the week and borough
    borough = borough.upper()
    dataframe3 = dataframe3[dataframe3['Borough'] == borough]
    dataframe4=dataframe3.groupby(['weekday','day_of_week'])["weekday"].count().reset_index(name="count").sort_values(by='count', ascending=0)
    filename = "F:/Python_Project/Analysis3/CSV/"
   
    dataframe4.to_csv(filename+"complaints_borough_days.csv",  index = False)
    
dataframe4
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20,8))
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=2)
sns.barplot(x="day_of_week", y="count", data=dataframe4)
plt.xlabel("Day of week")
plt.ylabel("Count of complaints")
plt.suptitle("Complaints in each borough per day of the week -- "+borough, y=1.05, fontsize=32)
plt.title("Based on NYC 311 reuqests for the year 2015", fontsize=18)
plt.xticks(rotation=50)
plt.savefig("F:/Python_Project/Analysis3/Images/"+borough+"complaints_day_of_week.png", bbox_inches='tight')



# In[ ]:




# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.scatter(dataframe4['weekday'],dataframe4['count']) #You can also add more variables here to represent color and size.
# plt.show()
# 

# dataframe4['count'].plot(kind='pie', autopct='%.2f', labels=['','','',''],  ax=ax, fontsize=10)
# ax.legend(loc=3, labels=dataframe4.index)

# In[ ]:

def plot_borough_day_month_period(df, xaxis, yaxis):
    
    get_ipython().magic('matplotlib inline')

    import matplotlib.pyplot as plt
    import seaborn as sns
       #dftrafficday = df
    plt.figure(figsize=(25,30))
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=2)
    sns.barplot(x=xaxis, y=axis, data=df)
    plt.xlabel("day_of_week")
    plt.ylabel("Number of complaints")
    plt.title("Number of complaints with respect to noise in every borough")
    plt.savefig("F:/Python_Project/Analysis3/Images/borough_day.png", bbox_inches='tight')


# # Check trend in each borough w.r.t month

# In[55]:

#dataframe5=dataframe3.groupby(['day_of_week', 'Borough'])["day_of_week"].count().reset_index(name="count").sort_values(by='count', ascending=0)

dataframe3 = dataframe2[['Agency', 'day_of_week', 'Created Date', 'Complaint Type', 'Time Taken', 'Borough','Month','period','hr' ]]
borough = input('Please enter: ')
print(borough)


# get the number of complaints with respect to month 
if borough=="":
    print("Please enter borough")
else:
    # get the number of complaints with repect to month and borough
    borough = borough.upper()
    dataframe3 = dataframe3[dataframe3['Borough'] == borough]
    dataframe6=dataframe3.groupby(['Month'])["Month"].count().reset_index(name="count").sort_values(by='count', ascending=0)
    filename = "F:/Python_Project/Analysis3/CSV/"

    dataframe6.to_csv(filename+"complaints_borough_month.csv",  index = False)
    name = borough+'_month'


dataframe6

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(25,8))
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=2)
sns.barplot(x="Month", y="count", data=dataframe6)
plt.xlabel("Month")
plt.ylabel("Count of complaints")
plt.suptitle("Complaints in each borough per Month -- "+borough, y=1.05, fontsize=32)
plt.title("Based on NYC 311 reuqests for the year 2015", fontsize=18)
plt.xticks(rotation=50)
plt.savefig("F:/Python_Project/Analysis3/Images/"+borough+"complaints_month.png", bbox_inches='tight')

dataframe6.plot(x="Month", y="count")


# In[ ]:




# # Check trend in each borough w.r.t period

# In[60]:

#dataframe5=dataframe3.groupby(['day_of_week', 'Borough'])["day_of_week"].count().reset_index(name="count").sort_values(by='count', ascending=0)

dataframe3 = dataframe2[['Agency', 'day_of_week', 'Created Date', 'Complaint Type', 'Time Taken', 'Borough','Month','period','hr' ]]
borough = input('Please enter: ')
print(borough)


# get the number of complaints with respect to month 
if borough=="":
    print(" Please enter borough ")
    
else:
    # get the number of complaints with repect to month and borough
    borough = borough.upper()
    dataframe3 = dataframe3[dataframe3['Borough'] == borough]
    dataframe6=dataframe3.groupby(['period'])["period"].count().reset_index(name="count").sort_values(by='count', ascending=0)
    filename = "F:/Python_Project/Analysis3/CSV/"

    dataframe4.to_csv(filename+"complaints_borough_period.csv",  index = False)
    name = borough+'_period'

    
dataframe6


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(25,8))
# sns.set_style("whitegrid")
# sns.set_context("notebook", font_scale=2)
# sns.barplot(x="period", y="count", data=dataframe6)
dataframe6.plot(x="period", y="count")
plt.xlabel("Period of the day")
plt.ylabel("Count of complaints")
plt.suptitle("Complaints in each borough wrt period of the day -- "+borough, y=1.2, fontsize=32)
plt.title("Based on NYC 311 reuqests for the year 2015",y=1.05, fontsize=18)
plt.xticks(rotation=70)
plt.savefig("F:/Python_Project/Analysis3/Images/"+borough+"complaints_period.png", bbox_inches='tight')





# In[ ]:




# In[ ]:



