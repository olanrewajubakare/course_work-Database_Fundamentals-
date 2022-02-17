import pymongo
import pandas as pd
from pprint import pprint 

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Pollution_db']
date_cols = ['Date Time', 'DateStart', 'DateEnd']
df = pd.read_csv("clean.csv", parse_dates=date_cols, low_memory=False)


df = df[df['SiteID'] == 206]
readings_collection = db['Readings']


single_readings_data = df.drop_duplicates()

readings_data = single_readings_data.to_dict(orient='records')


readings_collection.insert_many(readings_data)

# print(readings_data_list)

# print(single_readings_data)


