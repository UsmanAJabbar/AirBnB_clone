#!/usr/bin/python3
"""CLASS FILE STORAGE"""
import json
from ..base_model import BaseModel
from os.path import exists

class FileStorage():
    """
    ------------------
    CLASS: FileStorage
    ------------------
    """

    __file_path = "test.json"
    __objects = {}

    def all(self):
        """
        ---------------------------
        PUBLIC INSTANCE METHOD: ALL
        ---------------------------
        DESCRIPTION:
            Returns the dictionary stored in
            the attribute '__objects'
        ARGS:
            @self: current instance
        """
        return self.__objects

    def new(self, obj):
        """
        ---------------------------
        PUBLIC INSTANCE METHOD: NEW
        ---------------------------
        DESCRIPTION:
            Adds the necessary objects to the
            '__objects' attribute
        ARGS:
            @self: current instance
            @obj: object to add to '__objects'
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        ----------------------------
        PUBLIC INSTANCE METHOD: SAVE
        ----------------------------
        DESCRIPTION:
            Serializes items in __objects to JSON
            and dumps the output into a file defined
            by '__file_path'
        ARGS:
            @self: current instance
        """
        temp = {}

        for keys in self.__objects.keys():
            temp[keys] = self.__objects[keys].to_dict()

        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(temp, jsonfile)

    def reload(self):
        """
        """
        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                deserialized = json.load(jsonfile)
            for keys in deserialized.keys():
                self.__objects[keys] = models.base_model.BaseModel(**deserialized[keys])
