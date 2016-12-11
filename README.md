# NYC_Progress
Analyze the trends and changes in New York City
![nyc](https://cloud.githubusercontent.com/assets/22182874/21075598/24498c0c-bee4-11e6-839c-041296cf24a2.jpg)

Analyse the complaints registered with respect to all the agencies in various categories to check the trend of NYC Life style and                                                            progress (or deteoriation) 



### Data collected 
 [NYC DATA 311 Requests](https://nycopendata.socrata.com/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/data)

* The data consists of complaints that has been registered at various agencies at different cities at different times. 
* It also consists of various categories of complaints and the times at which they were closed. 
* The data helps you notice the various incidents happening in New York.


An effort has been made to analyze about New York, in order to know how the city is progressing or deteriorating in handling various issues in the city.

The data was then cleansed where a new file was created by using only those columns which provide more information and are helpful for analysis. 

* SAMPLE DATA
![image](https://cloud.githubusercontent.com/assets/22182874/21075858/b7fbd33c-beea-11e6-9406-8d44a1d6d010.png)

 
OUTPUT - Output of each analysis is stored in the form of csv files and images in the respective folders.

## Analysis 1

This analysis is about the complaints registered across different boroughs.
This helps you notice:
* Complaints with respect to borough.

![borough_issues](https://cloud.githubusercontent.com/assets/22182874/21075899/92af496e-beeb-11e6-86fd-4b15afd5e18b.png)

* Complaints w.r.t to a particular borough. 
  	  Note: User can enter the borough name, or the borough with highest complaints will be considered

![complaints_count_borough](https://cloud.githubusercontent.com/assets/22182874/21075908/fb316af8-beeb-11e6-83c2-6bf34762980d.png)

* Check how long it took to solve(close) the issue for complaints in a category.
      Also tells average time taken to solve a particular complaint 

* Sample output data

Agency|Created Date|Month|Complaint Type|Time Taken to Close|Borough
------------ | ------------------ | ------------ | ------------ | ------------ | ------------ 
NYPD|2015-05-21 20:40:35|May|Blocked Driveway|0 days 02:38:58.000000000|BROOKLYN
NYPD|2015-09-26 01:34:39|Sep|Blocked Driveway|0 days 05:02:49.000000000|BROOKLYN
NYPD|2015-04-26 20:32:00|Apr|Blocked Driveway|0 days 01:30:06.000000000|BROOKLYN
NYPD|2015-09-25 11:47:57|Sep|Blocked Driveway|0 days 09:13:34.000000000|BROOKLYN
NYPD|2015-09-13 15:55:11|Sep|Blocked Driveway|0 days 01:14:28.000000000|BROOKLYN
NYPD|2015-04-22 12:53:47|Apr|Blocked Driveway|0 days 00:15:42.000000000|BROOKLYN
NYPD|2015-06-20 22:35:57|Jun|Blocked Driveway|0 days 00:27:26.000000000|BROOKLYN
NYPD|2015-02-23 14:57:13|Feb|Blocked Driveway|0 days 09:11:58.000000000|BROOKLYN
NYPD|2015-02-23 16:46:36|Feb|Blocked Driveway|0 days 01:29:59.000000000|BROOKLYN
NYPD|2015-02-24 01:39:11|Feb|Blocked Driveway|0 days 00:16:53.000000000|BROOKLYN
NYPD|2015-02-24 17:04:39|Feb|Blocked Driveway|0 days 01:25:30.000000000|BROOKLYN
NYPD|2015-09-27 16:31:58|Sep|Blocked Driveway|0 days 02:41:17.000000000|BROOKLYN
NYPD|2015-02-12 14:55:19|Feb|Blocked Driveway|0 days 00:41:53.000000000|BROOKLYN
NYPD|2015-09-20 18:04:34|Sep|Blocked Driveway|0 days 03:06:35.000000000|BROOKLYN
NYPD|2015-09-25 21:11:49|Sep|Blocked Driveway|0 days 08:48:44.000000000|BROOKLYN
NYPD|2015-09-20 22:56:10|Sep|Blocked Driveway|0 days 01:20:27.000000000|BROOKLYN
NYPD|2015-07-03 23:09:16|Jul|Blocked Driveway|0 days 02:10:20.000000000|BROOKLYN
      
* Check how many complaints were registered with respect to month.
      NOTE: User can enter the borough name, or the borough with highest complaints will be considered. 
            User can enter the complaint name, or the complaint with the highest count will be considered.

![complaintspermonth](https://cloud.githubusercontent.com/assets/22182874/21076013/c69b3d2a-beee-11e6-9c48-9611a8965501.png)


## Analysis 2

This helps to analyze the traffic pattern in the city.
This helps you notice:

* How traffic issues are with respect to borough

![traffic_issues_borough](https://cloud.githubusercontent.com/assets/22182874/21076076/499763f6-bef0-11e6-9589-276998f186b2.png)

*	Traffic issues with respect to the day of a week
     NOTE:	User can enter the borough else all the boroughs will be considered.
     For example - Brooklyn
     
![traffic_issues_borough_day](https://cloud.githubusercontent.com/assets/22182874/21076149/1a02cfca-bef2-11e6-8559-2f20a9e62444.png)

     
* Traffic issues with respect to period of the day
  NOTE: User can enter the borough else all the boroughs will be considered.
        User can enter the period else all the periods of the day will be considered.
        
  (early morning, morning, afternoon, evening, night)
  {8: 'morning', 16: 'evening', 12: 'afternoon', 20: 'night'} – intervals of 4
  Early morning – 00:00 to 08:00

![traffic_issues_period_borough](https://cloud.githubusercontent.com/assets/22182874/21076307/f700e3dc-bef5-11e6-9e6e-7ebb454e298e.png)


## Analysis 3

Time series patterns. Complaint in particular or all complaints that are registered in a month / day.
This helps you notice which day usually has more complaints (in order to take some action based on the various reasons)

* Patterns with respect to days.
![complaints_day](https://cloud.githubusercontent.com/assets/22182874/21076751/840b1346-bf01-11e6-89e6-509c558a69d9.png)

* Patterns with respect to months.
![complaints_month](https://cloud.githubusercontent.com/assets/22182874/21076726/fcd283d2-bf00-11e6-841d-c17bde44a4d4.png)

*	Patterns with respect to period
![complaints_period](https://cloud.githubusercontent.com/assets/22182874/21076717/bda810c8-bf00-11e6-97dd-d333e895a2ed.png)

  NOTE:	User can enter the borough and check trends with respect to days of the week, month and period.

* For example: USER enters Brooklyn
![brooklyncomplaints_day_of_week](https://cloud.githubusercontent.com/assets/22182874/21076925/61bbcbcc-bf07-11e6-9e65-03a9f9e1387b.png)
![brooklyncomplaints_month](https://cloud.githubusercontent.com/assets/22182874/21076936/c1fdecea-bf07-11e6-97f0-32f737943b5d.png)
![brooklyncomplaints_period](https://cloud.githubusercontent.com/assets/22182874/21076959/c1d57994-bf08-11e6-8113-6f1b82e74375.png)

This helps you concentrate on each borough to take necessary actions based on the months and days of the week. Also depending on the period of the day.



## Analysis 4

This is to check how each agency is handling complaints. To check if the agency is able to close the issues before the due date mentioned. 
* Shows how efficient each agency has been with respect to each complaint category.
* Shows number of complaints in the category and how efficiently it has been solved/closed.
* Each agency has been rated (given weights depending on the time taken by each agency to solve a complaint)
*	Percentage of efficiency can be noticed.
![efficient_agencies](https://cloud.githubusercontent.com/assets/22182874/21077203/bc42dd38-bf11-11e6-98ec-e820e6e1c77d.png)
![inefficient_agencies](https://cloud.githubusercontent.com/assets/22182874/21077204/c77ca436-bf11-11e6-936a-6fa55a5a5514.png)


Helps to decide what necessary actions can be taken by each agency depending on what category plays a major role in the daily life of city.


## Analysis 5

Each agency has various complaints have been opened, closed, pending etc.
Depending on the count of each type of complaints and their status, agency has to take action.

*	Find the pending, closed, assigned and opened complaints for each agency with their count.

![complaints_statuses](https://cloud.githubusercontent.com/assets/22182874/21077521/7f8b093c-bf1c-11e6-9475-47e497cbb74c.png)

*	User can enter agency and status and check records with the incident location
  For example user entered

![complaints_statuses](https://cloud.githubusercontent.com/assets/22182874/21077549/7d821b98-bf1d-11e6-8a17-e9b6da7200de.png)



This helps the agency to decide what can be done with respect to incidents that are pending or open across boroughs








