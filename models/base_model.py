#!/usr/bin/python3
"""BaseModel"""
from datetime import datetime
import uuid


class BaseModel():
    """
    -----------------
    CLASS: BASE MODEL
    -----------------
    """
    # ------------------------------- #
    #       PUBLIC ATTRIBUTES         #
    # ------------------------------- #

    # ------------------------------- #
    #           MAGIC METHODS         #
    # ------------------------------- #
    def __init__(self):
        ""
        ""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        ---------------------
        MAGIC METHOD: __STR__
        ---------------------
        DESCRIPTION:
            Returns a string representation
            of the current instance in the
            following format
            "[<class name>] (<self.id>) <self.__dict__>"
        ARGS:
            @self: current instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    # ------------------------------- #
    #     PUBLIC INSTANCE METHODS     #
    # ------------------------------- #
    def save(self):
        """
        ----------------------------
        PUBLIC INSTANCE METHOD: SAVE
        ----------------------------
        DESCRIPTION:
            Updates the 'updated_at' public attribute
            with the current datetime module accordingly.
        ARGS:
            @self: current instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        -------------------------------
        PUBLIC INSTANCE METHOD: TO_DICT
        -------------------------------
        DESCRIPTION:
            Returns all the atrributes of the current instance
        ARGS:
            @self: current instance
        """
        self_dictionary = dict(self.__dict__)
        self_dictionary['__class__'] = self.__class__.__name__
        self_dictionary['created_at'] = self.created_at.isoformat('T')
        self_dictionary['updated_at'] = self.updated_at.isoformat('T')
        return self_dictionary
