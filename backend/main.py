"""
app.py

This one file is all you need to start off with your FastAPI server!
"""

from typing import Optional
import uvicorn
from fastapi import FastAPI, status
import json 
import requests

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
KEY = '8141076d7f8142fd8fe25385b6d373da'

user_location = input("Enter a City, Country: ")

location = f"https://api.geoapify.com/v1/geocode/search?text={user_location}&format=json&apiKey={KEY}"
location_info = requests.get(location)
location_info = location_info.text
data = json.loads(location_info)

place_id = data['results']
place_id = place_id[0]
place_id = place_id['place_id']

parameters = f"categories=tourism.attraction&filter=place:{place_id}&limit=15"

url = (f"https://api.geoapify.com/v2/places?{parameters}&apiKey={KEY}")
response = requests.get(url)
response = response.text
places = json.loads(response)

def address_format(list):
    collection = []
    features = list['features']
    for x in features:
        properties = x['properties']
        address = properties['formatted']
        collection.append(address)
    collection.sort()
    return collection

list_of_attractions = address_format(places)


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
                    'limit' :6,
                    }
yelp_url = 'https://api.yelp.com/v3/businesses/search'
yelp_response= requests.get(yelp_url,params=yelp_parameters, headers=headers)
yelp_response = yelp_response.text
hotels = json.loads(yelp_response)

##makes a dictionary for hotel names and images 

def yelp_dictionary(dictionary):
    yelp_collection = {}
    businesses = dictionary.get('businesses', []) 
    for x in businesses:
        name = x.get('name', 'N/A')
        image = x.get('image_url', 'N/A')
        yelp_collection[name]=image
    sorted_yelp_collection = dict(sorted(yelp_collection.items()))
    return sorted_yelp_collection

hotels_for_user= yelp_dictionary(hotels)

for x in list_of_attractions:
    tourist_yelp = []
    lon = get_lon(x)
    lat = get_lat(x)
    tourist_parameters = { 'latitude':f"{lat}",
                     'longitude':f"{lon}",
                    'radius' : 40000,
                    'limit' :5,
                    }
    yelp_url = 'https://api.yelp.com/v3/businesses/search'
    tourist_response= requests.get(yelp_url,params=tourist_parameters, headers=headers)
    tourist_yelp.append(tourist_response)
print(tourist_yelp)