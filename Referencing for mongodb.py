import pymongo
import pandas as pd
import json
from pprint import pprint 
from bson.dbref import DBRef

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Pollution_db']
station_collection = db['Stations']
date_cols = ['Date Time', 'DateStart', 'DateEnd']
df = pd.read_csv("clean.csv", parse_dates=date_cols, low_memory=False)

# The dateend column has a number of date values that are just zeros, to catter for them, I converted them to none type. 
# df[['DateEnd']] = df[['DateEnd']].astype(object).where(df[['DateEnd']].notnull(), None)

df = df[df['SiteID'] == 206]

# Select the columns with the station columns you want in the station document
station_df = df[['SiteID', 'Location', 'geo_point_2d']]

# Drop duplicate values
single_station_data = station_df.drop_duplicates()

# Convert to dict
station_data = single_station_data.to_dict(orient='records')

station_data = station_data[0]

# new_key = "_id"
# old_key = "SiteID"
# station_data[new_key] = station_data.pop(old_key)

# station_collection.insert_one(station_data)

# For the readings tables
readings_collection = db['Readings']

readings_df = df[['Date Time', 'NOx', 'NO2', 'NO', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5',
'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'DateStart', 'DateEnd', 'Current', 
'Instrument Type']]

single_readings_data = readings_df.drop_duplicates()

readings_data = single_readings_data.to_dict(orient='records')


readings_data_list = []

for reading in readings_data: 
    reading['Site_ID'] = DBRef("Stations", "61cdef7ab3fdd470ed66439a", 'Pollution_db')
    readings_data_list.append(reading)

# readings_collection.insert_many(readings_data_list)

# print(readings_data_list)

# print(single_readings_data)


