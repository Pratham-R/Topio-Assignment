from bson import ObjectId
from database import db
from models import Property, PropertyUpdate

async def create_property(property: Property):
    property_dict = property.dict()
    result = await db.properties.insert_one(property_dict)
    return result.inserted_id

async def get_all_properties():
    properties = await db.properties.find().to_list(None)
    return properties

async def get_properties_by_city(city: str):
    properties = await db.properties.find({"city": city}).to_list(None)
    return properties

async def update_property(property_update: PropertyUpdate):
    property_id = property_update.property_id
    update_data = {k: v for k, v in property_update.dict().items() if v is not None and k != "property_id"}
    result = await db.properties.update_one({"_id": ObjectId(property_id)}, {"$set": update_data})
    return result.modified_count == 1

async def get_cities_by_state(state: str):
    properties = await db.properties.find({"state": state}).to_list(None)
    cities = list(set([property["city"] for property in properties]))
    return cities

async def get_similar_properties(property_id: str):
    property = await db.properties.find_one({"_id": ObjectId(property_id)})
    if property:
        city = property["city"]
        properties = await db.properties.find({"city": city}).to_list(None)
        return properties
    return None
