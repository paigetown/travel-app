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

## getting longitude and latitude of user input
from geopy.geocoders import Nominatim
from requests.structures import CaseInsensitiveDict
import json
geolocator = Nominatim(user_agent="MyApp")

#location = geolocator.geocode(place_id)

KEY = '8141076d7f8142fd8fe25385b6d373da'
location = f"https://api.geoapify.com/v1/geocode/search?text={user_location}&format=json&apiKey={KEY}"
location_info = requests.get(location)
location_info = location_info.text

data = json.loads(location_info)
#print(data)
place_id = data['results']
place_id = place_id[0]
place_id = place_id['place_id']
parameters = f"categories=tourism.attraction&filter=place:{place_id}&limit=15"

url = (f"https://api.geoapify.com/v2/places?{parameters}&apiKey={KEY}")
response = requests.get(url)
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
