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
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review}

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

    def precmd(self, arg):
        """
        ---------------------------
        CUSTOM BEHAVOR FUNC: PRECMD
        ---------------------------
        DESCRIPTION:
            Takes in a command, finds out whether
            or not the command is a function call
            and processes it accordingly.
        NOTES:
            If the command input in not detected
            as a emulated function call, then the
            precmd part's skipped.
        """
        print("entered precmd")
        # Check if the input's empty
        if arg is not '':
            print("Input detected")
            func_chars = ['.', '(', ')', ',']

            for chars in func_chars:
                if chars in arg:
                    # If func_chars found in str, replace with ' '
                    cleanup = ''
                    for letters in arg:
                        if letters in func_chars:
                            cleanup += ' '
                        else:
                            cleanup += letters

                    cleanup = cleanup.replace('  ', ' ').strip()

                    # Breakup the string into a list of strings
                    l_of_str = self.parse(cleanup)

                    # Cleanup the quotes
                    for i in range(len(l_of_str)):
                        if l_of_str[i][0] == '"' and l_of_str[i][-1] == '"':
                            if len(l_of_str) == 5 and i == 4:
                                continue
                            l_of_str[i] = l_of_str[i].replace('"', ' ').strip()

                    # Generate Output String
                    if len(l_of_str) == 1:
                        final_str = l_of_str[0]

                    elif len(l_of_str) >= 2:
                        final_str = l_of_str[1] + ' ' + l_of_str[0]

                    if len(l_of_str) >= 3:
                        for strings in l_of_str[2:]:
                            final_str += ' ' + strings

                    print("Returning final_str as ", final_str)
                    return final_str
            return arg

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
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return
        if arg not in self.classes.keys():
            print("** class doesn't exist **")
            return

        for key in self.classes.keys():
            if key == arg:
                instance = self.classes[key]()
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

        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return

        # Check if we actually have a UUID
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Alright, we have the class and UUID, lets pull
        # a copy of all instances
        dict_of_instances = storage.all()

        # Check if we have that UUID in our list of instances
        class_uuid_key = args[0] + '.' + args[1]
        if class_uuid_key not in dict_of_instances.keys():
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

        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return

        # Check if we actually have a UUID
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Alright, we have the class and UUID, lets pull
        # a copy of all instances
        dict_of_instances = storage.all()

        # Check if we have that UUID in our list of instances
        class_uuid_key = args[0] + '.' + args[1]
        if class_uuid_key not in dict_of_instances.keys():
            print("** no instance found **")
        else:
            del dict_of_instances[class_uuid_key]
            storage.save()

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

        parsed_cls_name = args[0]
        if parsed_cls_name not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            dict_of_inst = storage.all()
            instances = []

            for keys in dict_of_inst.keys():
                if parsed_cls_name == dict_of_inst[keys].__class__.__name__:
                    instances.append(str(dict_of_inst[keys]))
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
        if parsed_class_name not in self.classes.keys():
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
        if class_uuid_key not in dict_of_instances.keys():
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
        dict_of_instances[class_uuid_key].save()

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
        return console_in.split(" ")

if __name__ == '__main__':
    HBNBCommand().cmdloop()


# INPUT
# User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})

# OUTPUT TO UPDATE
# Detect whether we have a '{' and '}'
# If we have those, then divide them by the the comma and save them into a list_of_str_dict
# If the first command was update, then we are going to take in

# for loop running through list_of_str_dict
# static + list_of_str_dict[i]

# update User 38f22813-2753-4d42-b37c-57a17f1e4f88 first_name "John"
# update User 38f22813-2753-4d42-b37c-57a17f1e4f88 age 89
