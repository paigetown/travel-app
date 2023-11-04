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
user_location = input("Enter a City, Country")



## getting longitude and latitude of user input
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")
location = geolocator.geocode(user_location)


parameters = {
    f"categories=tourism.attraction&bias=proxmity:{location.longitude},{location.latitude}&limit = 15"
}


geoapify_responses = requests.get("https://api.geoapify.com/v2/places?",params=parameters, apiKey= "4ce6deba3eee428682f4fd8b9c2944cb")