#!/usr/bin/python3
"""A Wild Class Appears"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """AirBnB Interpreter"""
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "State": State, "City": City, "Amenity": Amenity,
               "Review": Review}

    # ----------------------------------- #
    #       CUSTOM BEHAVOIR METHODS       #
    # ----------------------------------- #
    def emptyline(self):
        """
        ------------------------
        PUBLIC METHOD: EMPTYLINE
        ------------------------
        DESCRIPTION:
            Overrides empty input behavior in
            the console
        """
        pass

    # ----------------------------------- #
    #           CONSOLE COMMANDS          #
    # ----------------------------------- #
    def do_quit(self, arg):
        """
----------------
COMMAND: DO QUIT
----------------
DESCRIPTION:
    Allows you to exit the console.
NOTES:
    Usage: exit
    Also see, EOF.
        """
        exit()

    def do_EOF(self, arg):
        """
---------------
COMMAND: DO EOF
---------------
DESCRIPTION:
    Allows you to exit the console.
NOTES:
    Usage: EOF
    Also see, quit.
        """
        print()
        exit()

    def do_create(self, arg):
        """
------------------
COMMAND: DO_CREATE
------------------
DESCRIPTION:
    Creates a new instance of any given class
    saves it to a JSON file, and prints out
    the unique ID generated.
NOTES:
    Usage: create [class_name]
        """
        args = self.input_check(arg, 1)
        if args == False:
            return

        cls_names = list(self.classes.keys())
        for index in range(len(cls_names)):
            if cls_names[index] == arg:
                instance = self.classes[cls_names[index]]()
                print(instance.id)
                instance.save()
                return

    def do_show(self, arg):
        """
----------------
COMMAND: DO_SHOW
----------------
DESCRIPTION:
    Prints out a string representation
    of any instance, given that it exists
NOTES:
    Usage: show [class_name] [UUID]
        """
        args, obj = self.input_check(arg, 2)
        if args == False:
            return

        print(obj)

    def do_destroy(self, arg):
        """
-------------------
COMMAND: DO_DESTROY
-------------------
DESCRIPTION:
    Deletes an instance if it exists
NOTES:
    Usage: destroy [class_name] [UUID]
        """
        args = self.input_check(arg, 2)
        if args == False:
            return

        del obj

    def do_all(self, arg):
        """
----------------
COMMAND: DO_ALL
----------------
DESCRIPTION:
    Prints out a string representation of all the
    instances stored.
NOTES:
    If an class name is given prints out instances
    of that specific class.

    If no arguments are passed to all, all instances
    are expected to be printed.

    USAGE: all | all [class_name]
    Example - "all" | "all BaseModel"
        """

        if len(arg) == 0:
            print(storage.all())
            return
        else:
            args = self.input_check(arg, 1)
            if args == False:
                return

        dict_of_instances = storage.all()
        instances = []

        print(dict_of_instances)
        print(type(dict_of_instances))

        for keys in list(dict_of_instances.keys()):
            print(keys)
            if parsed_class_name in keys:
                instances.append(str(dict_of_instances[keys]))
        print(instances)

    def do_update(self, arg):
        """
------------------
COMMAND: DO_UPDATE
------------------
DESCRIPTION:
    Updates a given instance attribute.
NOTES
    Usage: update [class_name] [uuid] [key] [value]
    eg. - "update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        args = self.input_check(arg, 4)
        if args == False:
            return

        key, value = args[2], args[3]

        # Check if value's a string
        if value[0] == '"' and value[-1] == '"':
            value = value[1:-1]
        # Check if its a float
        elif '.' in value:
            value = float(value)
        # Else, try converting it to an int
        else:
            value = int(value)

        setattr(obj, key, value)
        storage.save()

    # ----------------------------------- #
    #       CUSTOM HELPER METHODS         #
    # ----------------------------------- #
    def parse(self, console_in):
        """
        ---------------
        FUNCTION: PARSE
        ---------------
        DESCRIPTION:
            Takes in a string and returns a list
            of words found
        ARGS:
            @cons_str: string passed by the console
        """
        list_of_words = console_in.split(" ")
        return list_of_words

    def input_check(self, arg, arglen):
        """
        ---------------------
        FUNCTION: INPUT_CHECK
        ---------------------
        DESCRIPTION:
            Responsible for checking the input and
            whether or not we have enough inputs for
            a command

        NOTES:
            If no errors were triggered, returns
            a list of words, else False
        """
        # Check if update is getting any arguments
        if arg == '':
            print("** class name missing **")
            return False

        # Begin breaking the string into words
        args = self.parse(arg)

        if arglen == 0 and len(arg) >= 0:
            return args

        # Check if the class name exists
        parsed_class_name = args[0]
        if parsed_class_name not in list(self.classes.keys()):
            print("** class doesn't exist **")
            return False

        if arglen == 1 and len(arg) >= 1:
            return args

        # Check if the ID is missing
        if len(args) < 2:
            print("** instance id missing **")
            return False

        if arglen == 2 and len(arg) >= 2:
            return args

        # Alright, we have the class and UUID, lets pull
        # a copy of all instances
        dict_of_instances = storage.all()
        parsed_uuid = args[1]

        # Check if we have that UUID in our list of instances
        class_uuid_key = parsed_class_name + '.' + parsed_uuid
        if class_uuid_key not in dict_of_instances:
            print("** no instance found **")
            return False

        # Check if attribute's given
        if len(args) < 3 and len(arg) >= 3:
            print("** attribute name missing **")
            return False

        if arglen == 3 and len(arg) >= 3:
            return args, dict_of_instances[class_uuid_key]

        # Check if value for the attribute's given
        if len(args) < 4:
            print("** value missing **")
            return False

        if arglen == 4 and len(arg) >= 4:
            return args, dict_of_instances[class_uuid_key]

        # Passed all the tests, return the list of words
        return args, dict_of_instances[class_uuid_key]

if __name__ == '__main__':
    HBNBCommand().cmdloop()
