from fastapi import FastAPI, HTTPException
from models import Property, PropertyUpdate
import crud

app = FastAPI()

@app.post("/create_new_property")
async def create_new_property(property: Property):
    result = await crud.create_property(property)
    if result:
        properties = await crud.get_all_properties()
        return properties
    raise HTTPException(status_code=500, detail="Property creation failed")

@app.get("/fetch_property_details")
async def fetch_property_details(city: str):
    properties = await crud.get_properties_by_city(city)
    return properties

@app.put("/update_property_details")
async def update_property_details(property_update: PropertyUpdate):
    result = await crud.update_property(property_update)
    if result:
        properties = await crud.get_all_properties()
        return properties
    raise HTTPException(status_code=404, detail="Property not found")

@app.get("/find_cities_by_state")
async def find_cities_by_state(state: str):
    cities = await crud.get_cities_by_state(state)
    return cities

@app.get("/find_similar_properties")
async def find_similar_properties(property_id: str):
    properties = await crud.get_similar_properties(property_id)
    if properties:
        return properties
    raise HTTPException(status_code=404, detail="Property not found")
