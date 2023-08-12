#!/usr/bin/python3
"""Creates a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Manages city objects
    Rep a city
    Attributes:
        state_id (str): State id
        name (str): Name of the city
    """
    state_id = ""
    name = ""
