#!/usr/bin/python3
"""Module that creates a User class and defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Manages user objects
    Rep a User.
    Attributes:
        email (str): Email of the user
        password (str): Password of the user
        first_name (str): The first name of the user
        last_name (str): Last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
