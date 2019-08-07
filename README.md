# SQLalchemy

## Climate Analysis and Exploration


* Climate analysis and data exploration.

* Choose a start date and end date for your trip. 

* Use SQLAlchemy to connect to sqlite database.

* Use SQLAlchemy to reflect tables into classes.

### Precipitation Analysis

* Query to retrieve the last 12 months of precipitation data.

* Select pertinent columns.

* Loaded query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame.

* Plot the results using the DataFrame.

* Use Pandas to print the summary statistics for the precipitation data.

![Precip by Date](https://user-images.githubusercontent.com/50157566/62592993-dfc1b880-b89a-11e9-8e8c-d26d9cb34ff8.png)

### Station Analysis

* Query to calculate the total number of stations.

* Query to find the most active stations.

  * Listed the stations and observation counts in descending order.

  * Retreive the most active station.

* Query to retrieve the last 12 months of temperature observation data (tobs).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram.

![Temp Histogram](https://user-images.githubusercontent.com/50157566/62592994-dfc1b880-b89a-11e9-9207-06d81e8e722c.png)

### Temperature Analysis

* Used the `calc_temps` function to calculate the min, avg, and max temperatures for my trip using the matching dates from the previous year.

* Plotted the min, avg, and max temperature from my previous query as a bar chart.

  * Used the average temperature as the bar height.

  * Used the peak-to-peak (tmax-tmin) value as the y error bar (yerr).

![Trip Avg Temp](https://user-images.githubusercontent.com/50157566/62592995-dfc1b880-b89a-11e9-97d3-46598a730143.png)


### Daily Rainfall Average.

* Calculated the rainfall per weather station using the previous year's matching dates.

* Calculated the daily normals. (Normals are the averages for the min, avg, and max temperatures).

* Created a list of dates for your trip in the format `%m-%d`. Used the `daily_normals` function to calculate the normals for each date string and appended the results to a list.

* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals

![trip_normals](https://user-images.githubusercontent.com/50157566/62593506-98d4c280-b89c-11e9-9627-84cc0a348bc0.png)

## Climate App

Designed a Flask API based on the queries that have just been developed.

* Used FLASK to create your routes.



