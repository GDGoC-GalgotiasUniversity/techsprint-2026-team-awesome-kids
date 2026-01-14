# app/schemas/bot.py

from pydantic import BaseModel, Field
from typing import Optional, List # <-- Make sure List is imported
from .pyobjectid import PyObjectId
from bson import ObjectId

class BotBase(BaseModel):
    name: str

class BotCreate(BotBase):
    pass

# --- UPDATED BotUpdate MODEL ---
class BotUpdate(BaseModel):
    name: Optional[str] = None #<-- Make name optional
    # --- NEW FIELDS ---
    summary: Optional[str] = None
    skills: Optional[List[str]] = None
    experience_years: Optional[float] = None
    # ------------------

class Bot(BotBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: Optional[str] = None
    # --- NEW FIELDS ---
    summary: Optional[str] = None
    skills: Optional[List[str]] = []
    experience_years: Optional[float] = 0.0
    # ------------------

    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True
        arbitrary_types_allowed = True