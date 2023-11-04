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
geolocator = Nominatim(user_agent="MyApp")

#location = geolocator.geocode(place_id)

GEOCODE_KEY = 'bebc019765d94e818ed0a95a81623aac'

f"categories=tourism.attraction&bias=proxmity:{location}&limit = 15"
parameters = {
    f"https://api.geoapify.com/v1/geocode/search?text={user_location}&format=json&apiKey={GEOCODE_KEY}"
}

PLACES_KEY = 'e6b0db864bc4428586627cc9ccb6ce7c'

url = (f"https://api.geoapify.com/v2/places?params={parameters}&apiKey={PLACESzz_KEY}")
response = requests.get(url)
print(response.json())