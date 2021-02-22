"""
Created on 19 Feb 2021

@author: conorkiy@gmail.com
"""

import dbinfo
import datetime
from datetime import datetime
import requests
import time
import json
import calendar
from sqlalchemy import create_engine
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

            api_request = requests.get(STATIONS, params={"contract":NAME, "apiKey": dbinfo.APIKEY})

            insert_into_availability(api_request.text)

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
        date = now.date()
        today = now.weekday()
        day = calendar.day_name[today]
        time = now.strftime("%H:%M")
        values = (station.get("number"), station.get("available_bike_stands"), station.get("available_bikes"), station.get("status"), date, day, time)
        
        engine.execute("INSERT INTO availability VALUES(%s,%s,%s,%s,%s,%s,%s)", values) 
