#!/usr/bin/python3
"""A Wild Class Appears"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """AirBnB Interpreter"""
    prompt = '(hbnb) '

    # ----------------------------------- #
    #       CUSTOM BEHAVOIR METHODS       #
    # ----------------------------------- #
    def emptyline(self):
        """
        ------------------------
        PUBLIC METHOD: EMPTYLINE
        ------------------------
        DESCRIPTION:
            Ensures that when no commands
            are entered, the console re-appears
            overriding the default behavior
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
    Creates a new instance of BaseModel
    saves it to a JSON file, and prints
    the unique ID generated.
NOTES:
    Usage: create [class_name]
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
        elif arg == 'BaseModel':
            instance = BaseModel()
            instance.save()
            print(instance.id)
        elif arg == 'User':
            instance = User()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
----------------
COMMAND: DO_SHOW
----------------
DESCRIPTION:
    Prints out a string representation
    of any instance given that it exists
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

        # args[0] = Classname | args[1] = UUID
        if args[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return

        # Check if we actually have a UUID
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Alright, we have the class and UUID, lets pull
        # a copy of all instances
        dict_of_instances = storage.all()

        class_uuid = args[0] + '.' + args[1]
        # Check if we have that UUID in our list of instances
        if class_uuid not in dict_of_instances:
            print("** no instance found **")
        else:
            print(dict_of_instances[class_uuid])

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

        # args[0] = Classname | args[1] = UUID
        if args[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return

        # Check if we actually have a UUID
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Alright, we have the class and UUID, lets pull
        # a copy of all instances
        dict_of_instances = storage.all()

        class_uuid = args[0] + '.' + args[1]
        # Check if we have that UUID in our list of instances
        if class_uuid not in dict_of_instances:
            print("** no instance found **")
        else:
            del dict_of_instances[class_uuid]

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

        if args[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        else:
            dict_of_instances = storage.all()
            random_list = []

            for keys in dict_of_instances.keys():
                if args[0] in keys:
                    random_list.append(str(dict_of_instances[keys]))
            print(random_list)

    def do_update(self, arg):
        """
------------------
COMMAND: DO_UPDATE
------------------
DESCRIPTION:
    Updates a given instance attribute.
NOTES
    Usage: update [class_name] [uuid] [key] [value]
    Example - "update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        # Check if update is getting any arguments
        if arg == '':
            print("** class name missing **")
            return

        # Args are present, break them down into seperate words
        args = self.parse(arg)

        # Check if the class name exists
        if args[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return

        # Check if the ID is missing
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Check if the UUID exists of that class
        # Alright, we have the class and UUID, lets pull
        # a copy of all instances
        dict_of_instances = storage.all()

        class_uuid = args[0] + '.' + args[1]
        # Check if we have that UUID in our list of instances
        if class_uuid not in dict_of_instances:
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

        # Remove Extra Quotation Marks
        if args[3][0] == '"' and args[3][-1] == '"':
            args[3] = args[3][1:-1]
        # Check if its a float
        elif '.' in args[3]:
            args[3] = float(args[3])
        else:
            args[3] = int(args[3])

        setattr(dict_of_instances[class_uuid], args[2], args[3])

    # ----------------------------------- #
    #       CUSTOM HELPER METHODS         #
    # ----------------------------------- #
    def parse(self, cons_str):
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
        list_of_words = cons_str.split(" ")
        return list_of_words

if __name__ == '__main__':
    HBNBCommand().cmdloop()
