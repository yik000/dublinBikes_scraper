"""
Created on 19 Feb 2021

@author: conorkiy@gmail.com
"""

import dbinfo
import datetime
import requests
import time
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, insert
import traceback


"""
API variables
"""
NAME="Dublin"
STATIONS="https://api.jcdecaux.com/vls/v1/stations?"


"""
create engine - connect to database
"""
engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/dbikes".format(dbinfo.USER, dbinfo.PASS, dbinfo.URI), echo=True)


"""
main
"""
def main():
    while True:
        try:

            apiRequest = requests.get(STATIONS, params={"contract":NAME, "apiKey": dbinfo.APIKEY})
            values = list(map( get_availability, apiRequest.json() ))
            insert = availability.insert().values(values)
            engine.execute(insert)

            time.sleep(5*60)

        except:

            print(traceback.format_exc())
    
    return


"""
insert into availability
"""
def insert_into_availability(text):

    stations = json.loads(text)

    for station in stations:
        
        now = datetime.fromtimestamp( int(station.get("last_update")/ 1e3) )
        today = now.weekday()
        day = calendar.day_name[today]
        time = now.strftime("%H:%M")
        values = (station.get("number"), station.get("available_bike_stands"), station.get("available_bikes"), station.get("status"), day, time)
        
        engine.execute("INSERT INTO availability VALUES(%s,%s,%s,%s,%s,%s)", values) 
