#!/usr/bin/python3
""" this __init__ allows the directory to be treated as
a package"""

from models.engine.file_storage import FileStorage
#  class filestorage serializes and deserializes json files

storage = FileStorage()  # storage instance of Filestorage

storage.reload()  # for data reloading
