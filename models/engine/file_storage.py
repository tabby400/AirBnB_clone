#!/usr/bin/python3
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
import os.path
import json
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """ this class represents the storage engine.
    Attributes:
        __file_path : the file to save objects in
        __objects : Dict of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dict objects are returned"""
        return FileStorage.__objects

    def new(self, obj):
        """onjects with keys"""
        jname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(jname, obj.id)] = obj

    def save(self):
        """objects are serialized to json"""
        obdict = FileStorage.__objects
        objdict = {obj: obdict[obj].to_dict() for obj in obdict.keys()}
        with open(FileStorage.__file_path, "w") as fh:
            json.dump(objdict, fh)

    def reload(self):
        """if file exists,deserealize"""
        try:
            with open(FileStorage.__file_path) as fh:
                objdict = json.load(fh)
                for p in objdict.values():
                    class_name = p["__class__"]
                    del p["__class__"]
                    self.new(eval(class_name)(**p))
        except FileNotFoundError:
            return
