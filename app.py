# import libraries
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect database
Base = automap_base()
Base.prepare(engine, reflect=True)

# Connect to database 
session = Session(engine)
conn = engine.connect()

#Save classes to tables
measurement = Base.classes.measurement
station = Base.classes.station


def calc_temps(start_date, end_date):
    
    return session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).filter(measurement.date <= end_date).all()

#Open Flask module
app = Flask(__name__)

#Match URLs to view functions in Flask
@app.route("/")
def home():
    return(
        f"<bold>Welcome Hawaii Climate API!<br/><br/></bold>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/startdate</br>"
        f"/api/v1.0/startdate/enddate<br>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    prcp_query = session.query(measurement.date, measurement.prcp).filter(measurement.date >= "2016-08-23").\
    filter(measurement.date <= "2017-08-23").all()

    precipitation = []
    for x in prcp_query:
        dates = {}
        dates[x.dates] = x.prcp
        precipitation.append(dates)

        return jsonify(precipitation)



@app.route("/api/v1.0/stations")
def stations():
   


@app.route("/api/v1.0/tobs")
def tobs():
    tobs_return = session.query(measurement.tobs).\
        filter(measurement.date >= "2016-08-23").\
        filter(measurement.date <= "2017-08-22").all()
    


@app.route("/api/v1.0/<start>")
def start(start):
    



@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end_date):
    

    if __name__ == '__main__':
        app.run(debug=True)