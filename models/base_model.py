#!/usr/bin/python3
"""BaseModel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    -----------------
    CLASS: BASE MODEL
    -----------------
    """
    # ------------------------------- #
    #           MAGIC METHODS         #
    # ------------------------------- #
    def __init__(self, *args, **kwargs):
        """
        ----------------------
        MAGIC METHOD: __INIT__
        ----------------------
        DESCRIPTION:
            Initializes the needed attributes
        Args:
            @args: a number of arguments
            @kwargs: a dictionary of attributes
        """
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key in kwargs.keys():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        kwargs[key] = datetime(int(kwargs[key][:4]),
                                               int(kwargs[key][5:7]),
                                               int(kwargs[key][8:10]),
                                               int(kwargs[key][11:13]),
                                               int(kwargs[key][14:16]),
                                               int(kwargs[key][17:19]),
                                               int(kwargs[key][20:]))
                    setattr(self, key, kwargs[key])

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
        storage.save()

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
