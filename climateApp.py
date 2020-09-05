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
        <p> Hawaii's climate is characteristically tropical but with moderate temperatures and humidity due to the influence of north and eastern trade winds. Summer average high temperatures peak at 84°F (28.9°C), as highs usually do not breach 90°F (32.2°C), while the lows seldom drop below 70°F (21.1°C). Winter average high temperatures are usually at 79°F (26.1°C), and the lows seldom dip below 65°F (18.3°C) at night. Hawaii has the lowest record high temperature at 100°F (37.8°C) and is the only American state never to record a temperature below 32°F (0°C).</p>
        <h3>Precipitation Information:</h3>
        <p> Precipitation in meteorology refers to all forms of liquid or solid water particles that form in the atmosphere and then fall to the earth's surface. Types of precipitation include hail, sleet, snow, rain, and drizzle. Frost and dew are not classified as precipitation because they form directly on solid surfaces.</p>
        <h3>Temperature Information:</h3>
        <h3>Start Day Information:</h3>
        <h3>Start & End Day Information:</h3>
   </html>
    """

# Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
# Create our session (link) from Python to the DB
    session = Session(engine)

# Query all precipitation
    results = session.query(measurement.date,measurement.prcp).all()

# Query all precipitation for a year 
    prevYear = lastDate - dt.timedelta(365)
# Convert the query results to a dictionary using 'date' as the key and 'prcp' as the value
    session.close()

# Convert list of tuples into normal list
    prcp_data = list(np.ravel(results))
# Return a JSON list
    return jsonify(prcp_data)

# Stations
@app.route("/api/v1.0/stations")
def stations():
# Create our session (link) from Python to the DB
    session = Session(engine)
# Query all stations
    stationsAll = session.query(station.name, station.station ).all()
# Convert list of tuples into normal list
    stationsList = list(np.ravel(stationsAll))
# Return a JSON list
    return jsonify(stationsList)

    session.close()

# TOBS
# @app.route("/api/v1.0/tobs")
# def tobs():
# # Create our session (link) from Python to the DB
#     session = Session(engine)
# # Query all stations
#     stationsAll = session.query(station.name, station.station ).all()
# # Convert list of tuples into normal list
#     stationsList = list(np.ravel(stationsAll))
# # Return a JSON list
#     return jsonify(stationsList)

#     session.close()

    # # Create a dictionary from the row data and append to a list of all_passengers
    # all_passengers = []
    # for name, age, sex in results:
    #     passenger_dict = {}
    #     passenger_dict["name"] = name
    #     passenger_dict["age"] = age
    #     passenger_dict["sex"] = sex
    #     all_passengers.append(passenger_dict)

    # return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
