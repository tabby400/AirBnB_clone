#!/usr/bin/python3
"""Modules that creates a Review class and defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):

    """Manages review objects
    Rep a review
    Attributes:
        place_id (str): Place id
        user_id (str): User id
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
