#!/usr/bin/python3
"""Creates the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Manages amenity class.
    Rep an amenity
    Attributes:
    name (str): Name of amenity
    """
    name = ""
