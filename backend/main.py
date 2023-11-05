"""
app.py

This one file is all you need to start off with your FastAPI server!
"""

from typing import Optional

import uvicorn
from fastapi import FastAPI, status



# Initializing and setting configurations for your FastAPI application is one
# of the first things you should do in your code.
app = FastAPI()



@app.get("/home")
def home():
    
    return {"message": "This is the home page"}
  
    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



# TODO: Add POST route for demo

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
#Routes for Geoapify

import requests
#import geocoder

user_location = input("Enter a City, Country: ")
#address = (f'https://maps.googleapis.com/maps/api/geocode/json?{user_location}')
#address.json

import json 

KEY = '8141076d7f8142fd8fe25385b6d373da'
location = f"https://api.geoapify.com/v1/geocode/search?text={user_location}&format=json&apiKey={KEY}"
location_info = requests.get(location)
location_info = location_info.text

data = json.loads(location_info)
#print(data)
limit = 15
place_id = data['results']
place_id = place_id[0]
place_id = place_id[0]
place_id = place_id['place_id']
parameters = f"categories=tourism.attraction&filter=place:{place_id}&limit=15"

url = (f"https://api.geoapify.com/v2/places?{parameters}&apiKey={KEY}")
response = requests.get(url)
print(response.json())

#yelp for hotels

#getting longitude and latitude from previous geoapify call

longitude = data['results']
longitude = longitude[0]
longitude = longitude['lon']

latitude = data['results']
latitude = latitude[0]
latitude = latitude['lat']


yelp_key='rW67PZzaPE67n2ms9CobxWSC7dnglV2whOL5GK82WMNr1cP0U-g8uf_wPQnTJFcTaAGX60x-8zmM_oCzEDeoWZAT4v2SNl0guzmh906MicoEzrTYQTBMF6YKj8lGZXYx'
headers = {'Authorization': 'Bearer %s' % yelp_key}

yelp_parameters = { 'latitude':f"{latitude}",
                     'longitude':f"{longitude}",
                    'term' : 'hotel', 
                    'radius' : 40000,
                    'limit' :5,
                    }
yelp_url = 'https://api.yelp.com/v3/businesses/search'
yelp_response= requests.get(yelp_url,params=yelp_parameters, headers=headers) 
print(yelp_response)
print(yelp_response.json())
response = response.text
places = json.loads(response)
#print(places)
def address_format(response):
    collection = []
    features = response['features']

    for x in features:
        properties = x['properties']
        address = properties['formatted']
        collection.append(address)
    collection.sort()
    return collection

print(address_format(places))
