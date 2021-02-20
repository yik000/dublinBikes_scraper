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
