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
    classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity',
               'Review']

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
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        # Create a list of instance calls that we're going
        # to use in the loop below
        f_classes = [BaseModel(), User(), Place(), State(),
                     City(), Amenity(), Review()]

        # Since self.classes and f_classes and are in the
        # same order, we call f_classes while we compare
        # the string versions of f_classes(aka self.classes)
        for index in range(len(f_classes)):
            if self.classes[index] == arg:
                instance = f_classes[index]
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
        # Checks if create is being passed args
        if arg == '':
            print("** class name missing **")
            return

        # At least one arg has been passed, break
        # the input up into a list of words
        args = self.parse(arg)

        parsed_class_name = args[0]
        if parsed_class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # Check if we actually have a UUID
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Alright, we have the class and UUID, lets pull
        # a copy of all instances
        dict_of_instances = storage.all()
        parsed_uuid = args[1]

        # Check if we have that UUID in our list of instances
        class_uuid_key = parsed_class_name + '.' + parsed_uuid
        if class_uuid_key not in dict_of_instances:
            print("** no instance found **")
        else:
            print(dict_of_instances[class_uuid_key])

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

        # Checks if create is being passed args
        if arg == '':
            print("** class name missing **")
            return

        # At least one arg has been passed, break
        # the input up into a list of words
        args = self.parse(arg)

        parsed_class_name = args[0]
        if parsed_class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # Check if we actually have a UUID
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Alright, we have the class and UUID, lets pull
        # a copy of all instances, and rename args[1]
        dict_of_instances = storage.all()
        parsed_uuid = args[1]

        # Check if we have that UUID in our list of instances
        class_uuid_key = parsed_class_name + '.' + parsed_uuid
        if class_uuid_key not in dict_of_instances:
            print("** no instance found **")
        else:
            del dict_of_instances[class_uuid_key]

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
        # If we don't have an arg, print everything
        if arg == '':
            print(storage.all())
            return

        # We do have an arg, pull everything out of console in
        args = self.parse(arg)

        parsed_class_name = args[0]
        if parsed_class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            dict_of_instances = storage.all()
            instances = []

            for keys in dict_of_instances.keys():
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
        # Check if update is getting any arguments
        if arg == '':
            print("** class name missing **")
            return

        # Args are present, break them down into seperate words
        args = self.parse(arg)

        # Check if the class name exists
        parsed_class_name = args[0]
        if parsed_class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # Check if the ID is missing
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Alright, we have the class and UUID, lets pull
        # a copy of all instances
        dict_of_instances = storage.all()
        parsed_uuid = args[1]

        # Check if we have that UUID in our list of instances
        class_uuid_key = parsed_class_name + '.' + parsed_uuid
        if class_uuid_key not in dict_of_instances:
            print("** no instance found **")
            return

        # Check if attribute's given
        if len(args) < 3:
            print("** attribute name missing **")
            return

        # Check if value for the attribute's given
        if len(args) < 4:
            print("** value missing **")
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

        setattr(dict_of_instances[class_uuid_key], key, value)
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
