#!/usr/bin/python3
""" This is the definition of a class BaseModel"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:

    """This is a representation of the basic model of the
    HBNB project which is a foundation of other classes with
    different types of objects"""

    def __init__(self, *args, **kwargs):
        """This initializes an instance of the Base Model
        Args:
            **kwargs(dict): involves keyword arguements of attributes
            *args: arguements of any type passed
            """
        date_fmt = "%Y-%m-%dT%H:%M:%S.%f"  # the format for date
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or "updated_at":
                    self.__dict__[key] = datetime.strptime(val, date_fmt)
                    #  datetime.strptime converts val from
                    #  string to datetime object
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """this updates the public instance att updated_at with
        current time"""
        self.updated_at = datetime.today()
        models.storage.save

    def to_dict(self):
        """ this is used to return a dictionary of the
        BaseModel instance with all key/value pairs"""
        dict_att = self.__dict__.copy()  # copy of instance att,orig remains
        dict_att["__class__"] = self.__class__.__name__
        dict_att["created_at"] = self.created_at.isoformat()
        dict_att["updated_at"] = self.updated_at.isoformat()
        return (dict_att)

    def __str__(self):
        """ this str function returns print format of class
        name, id and the dictionary of BaseModel Instance"""
        classnm = self.__class__.__name__
        return "[{}] ({}) {}".format(classnm, self.id, self.__dict__)
