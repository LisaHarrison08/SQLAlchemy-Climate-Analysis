# Climate Analysis - Hawaii


![surfs-up.png](Images/surfs-up.png)

Climate analysis for a holiday vacation in Honolulu, Hawaii! 

## Climate Analysis and Exploration

Used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. All of the analysis have been completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Chose a start date and end date for the vacation. 

* Used SQLAlchemy `create_engine` to connect to the sqlite database.

* Used SQLAlchemy `automap_base()` to reflect the tables into classes and saved a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.

  ![precipitation](Images/precipitation.png)

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

* Listed the stations and observation counts in descending order.

* Identified the station with the highest number of observations

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

* Filtered by the station with the highest number of observations.

* Plotted the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

- - -

## Step 2 - Climate App

* Designed a Flask API based on the queries.

* Used Flask to create your routes.

### Routes

* `/`

* Home page.

* Listed all available routes.

* `/api/v1.0/precipitation`

* Converted the query results to a dictionary using `date` as the key and `prcp` as the value.

* Returned a JSON representation of the dictionary.

* `/api/v1.0/stations`

* Returned a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
* Queried the dates and temperature observations of the most active station for the last year of data.
  
* Returned a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

* Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

* Calculated the `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

* Calculated the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

* Used Flask `jsonify` to convert the API data into a valid JSON response object.

- - -

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Identified the average temperature in June at all stations across all available years in the dataset. Also completed the same for December temperature.

* Used the t-test to determine whether the difference in the means, if any, was statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II

* Used the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

* Plotted the min, avg, and max temperature from your previous query as a bar chart.

* Used the average temperature as the bar height.

* Used the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average

* Calculated the rainfall per weather station using the previous year's matching dates.

* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.

* Using a function called `daily_normals` , calculated the daily normals for a specific date. The date string format `%m-%d`. Used all historic TOBS that matched that date string.

* Created a list of dates for the trip in the format `%m-%d`. Used the `daily_normals` function to calculate the normals for each date string and appended the results to a list.

* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Used Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/daily-normals.png)

