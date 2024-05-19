from pydantic import BaseModel
from typing import Optional

class Property(BaseModel):
    property_name: str
    address: str
    city: str
    state: str

class PropertyUpdate(BaseModel):
    property_id: str
    property_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
