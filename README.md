# NYC_Progress
Analyze the trends and changes in New York City
![nyc](https://cloud.githubusercontent.com/assets/22182874/21075598/24498c0c-bee4-11e6-839c-041296cf24a2.jpg)

Analyse the complaints registered with respect to all the agencies in various categories to check the trend of NYC Life style and                                                            progress (or deteoriation) 



* About the Data collected

-- The data consists of complaints that has been registered at various agencies at different cities at different times. 
-- It also consists of various categories of complaints and the times at which they were closed. 
-- The data helps you notice the various incidents happening in New York.


An effort has been made to analyze about New York, in order to know how the city is progressing or deteriorating in handling various issues in the city.

The data was then cleansed where a new file was created by using only those columns which provide more information and are helpful for analysis. 

 

Sample of the dataset that was collected. This dataset was then filtered according to the requirement and generated a new csv file for analysis.

OUTPUT - Output of each analysis is stored in the form of csv files and images in the respective folders.

## Analysis 1

This analysis is about the complaints registered across different boroughs.
This helps you notice:
### Complaints with respect to borough.
### Complaints w.r.t to a particular borough. 
  	  Note: User can enter the borough name, or the borough with highest complaints will be considered
### Check how long it took to solve(close) the issue for complaints in a category.
     Also tells average time taken to solve a particular complaint
### Check how many complaints were registered with respect to month.
      NOTE: User can enter the borough name, or the borough with highest complaints will be considered. 
            User can enter the complaint name, or the complaint with the highest count will be considered.


Analysis 2

This helps to analyze the traffic pattern in the city.
This helps you notice:
•	How traffic issues are with respect to borough
•	Traffic issues with respect to the day of a week
  o	User can enter the borough else all the boroughs will be considered.
•	Traffic issues with respect to period of the day
  o	User can enter the borough else all the boroughs will be considered.
  o	User can enter the period else all the periods of the day will be considered.
  (early morning, morning, afternoon, evening, night)
  {8: 'morning', 16: 'evening', 12: 'afternoon', 20: 'night'} – intervals of 4
  Early morning – 00:00 to 08:00


Analysis 3

Time series patterns. Complaint in particular or all complaints that are registered in a month / day.
This helps you notice which day usually has more complaints (in order to take some action based on the various reasons)
•	Patterns with respect to days.
  o	User can enter the borough else all the boroughs will be considered.
•	Patterns with respect to months.
  o	User can enter the borough else all the boroughs will be considered.
•	Patterns with respect to period
  o	User can enter the borough else all the boroughs will be considered.

This helps you concentrate on each borough to take necessary actions based on the months and days of the week. Also depending on the period of the day.



Analysis 4

This is to check how each agency is handling complaints. To check if the agency is able to close the issues before the due date mentioned. 
•	Shows how efficient each agency has been with respect to each complaint category.
•	Shows number of complaints in the category and how efficiently it has been solved/closed.
•	Each agency has been rated (given weights depending on the time taken by each agency to solve a complaint)
•	Percentage of efficiency can be noticed.


Helps to decide what necessary actions can be taken by each agency depending on what category plays a major role in the daily life of city.


Analysis 5

Each agency has various complaints have been opened, closed, pending etc.
Depending on the count of each type of complaints and their status, agency has to take action.
•	Find the pending, closed, assigned and opened complaints for each agency with their count.
•	User can enter agency and status and check records with the incident location

This helps the agency to decide what can be done with respect to incidents that are pending or open across boroughs








