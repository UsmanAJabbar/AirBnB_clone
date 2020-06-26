#!/usr/bin/python3
"""CLASS FILE STORAGE"""
import json
from os.path import exists

class FileStorage():
    """
    ------------------
    CLASS: FileStorage
    ------------------
    """

    # ------------------------------- #
    #       PUBLIC ATTRIBUTES         #
    # ------------------------------- #
    __file_path = "file.json"
    __objects = {}

    # ------------------------------- #
    #     PUBLIC INSTANCE METHODS     #
    # ------------------------------- #
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
        ------------------------------
        PUBLIC INSTANCE METHOD: RELOAD        
        ------------------------------
        DESCRIPTION:
            Deserializes a JSON file and adds it
            to the __objects attribute. 
        """
        from ..base_model import BaseModel
        from ..user import User
        from ..place import Place
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..review import Review

        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                deserialized = json.load(jsonfile)
            for keys in deserialized.keys():
                if deserialized[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**deserialized[keys])
                elif deserialized[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**deserialized[keys])
                elif deserialized[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**deserialized[keys])
                elif deserialized[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**deserialized[keys])
                elif deserialized[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**deserialized[keys])
                elif deserialized[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**deserialized[keys])
                elif deserialized[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**deserialized[keys])
