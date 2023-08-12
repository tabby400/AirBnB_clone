#!/usr/bin/python3
"""Module that creates a User class and defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):

    """Manages state objects
    Rep a state
    Attributes:
        name (str): The name of the state.
    """

    name = ""
