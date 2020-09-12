#################################################
# References
# Images sourced from: giphy.com & 
# Information : https://www.scholastic.com/teachers/articles/teaching-content/precipitation-weather/
# Hawaii Climate Information: https://www.weather-us.com/en/hawaii-usa-climate#:~:text=Hawaii's%20climate%20is%20characteristically%20tropical,F%20(21.1%C2%B0C).

##################################################
# Dependencies Setup
#################################################
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

# Create link from Python to database
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def homePage():
# List all available api routes
    return """ <html>
        <h1> Welcome to the Hawaii Climate Info Site</h1>
        <img src = "https://media.giphy.com/media/5QZoin5YqkPF7kXXoI/giphy.gif" ALT="Hawaii Beach" width="400" height="200" style="vertical-align:middle;margin:0px 50px">
        <p> Hawaii is a popular tourist destination due to the islands characteristic tropical climate. The Pacific Ocean that surrounds Hawaii provides a vast amount of fresh sea air that does not allow the temperatures of the islands to reach the same high levels that are typical of the tropics.<br><br> Summer average high temperatures peak at 84°F (28.9°C), while the lows seldom drop below 70°F (21.1°C). Winter average high temperatures are usually at 79°F (26.1°C), and the lows seldom dip below 65°F (18.3°C) at night. Hawaii has the lowest record high temperature at 100°F (37.8°C) and is the only American state never to record a temperature below 32°F (0°C).</p>
        <h3> Available API routes:</h3>
        <ul>
            <li> Hawaii Precipitation: 
            <br>
            <a href = "/api/v1.0/precipitation">/api/v1.0/precipitation</a><br><br>
            <li> Hawaii Weather Stations Data:
            <br>
            <a href = "/api/v1.0/stations">/api/v1.0/stations</a><br><br>
            <li> Hawaii Temperature Observations:
            <br>
            <a href = "/api/v1.0/tobs">/api/v1.0/tobs</a><br><br>
            <li> Start of Day Observations:
            <a href ="/api/v1.0/<start>/<end>">/api/v1.0/<start>/<end></a><br><br>
            </li>
        </ul>       
</html>
    """

# Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
# Create our session (link) from Python to the DB
    session = Session(engine)

    lastDate = dt.date(2017,8,23)
    prevYear = lastDate - dt.timedelta(365)
# Query all precipitation for a year
    result = session.query(measurement.date,measurement.prcp).filter(measurement.date>=prevYear).all()
    
# Convert the query results to a dictionary using 'date' as the key and 'prcp' as the value
# Convert list of tuples into normal list
    prcp_data = list(np.ravel(result))
# Return a JSON list
    return jsonify(prcp_data)
session.close()

# Stations
@app.route("/api/v1.0/stations")
def stations():
# Create our session (link) from Python to the DB
    session = Session(engine)
# Query all stations
    stationsAll = session.query(station.name, station.station).all()
# Convert list of tuples into normal list
    stationsList = list(np.ravel(stationsAll))
# Return a JSON list
    return jsonify(stationsList)
session.close()

# TOBS
@app.route("/api/v1.0/tobs")
def tobs():
# Create our session (link) from Python to the DB
    session = Session(engine)
# Query the dates and temperature observations for the previous year
    lastDate = dt.date(2017,8,23)
    prevYear = lastDate - dt.timedelta(365)
    tobs_max = session.query(measurement.tobs).filter(measurement.date >= prevYear).\
    filter(measurement.station == "USC00519281").\
    order_by(measurement.date).all()

# Convert list of tuples into normal list
    tobs_list = list(np.ravel(tobs_max))
# Return a JSON list
    return jsonify(tobs_list)
session.close()

# Start & End
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
# Create our session (link) from Python to the DB
    session = Session(engine)
# Query the dates and temperature observations for the previous year
    vacay_dates = session.query(measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).group_by(measurement.date).all()
  
# Convert list of tuples into normal list
    vacay_list = list(np.ravel(vacay_dates))
# Return a JSON list
    return jsonify(vacay_list)

session.close()

if __name__ == '__main__':
    app.run(debug=True)
