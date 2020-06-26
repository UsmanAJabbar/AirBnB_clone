#!/usr/bin/python3
"""A Wild Class Appears"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """AirBnB Interpreter"""
    prompt = '(hbnb) '

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

    def do_quit(self, arg):
        """
-------------
HELP: DO QUIT
-------------
DESCRIPTION:
    Allows you to exit the console.
NOTES:
    Also see, EOF.
        """
        exit()

    def do_EOF(self, arg):
        """
------------
HELP: DO EOF
------------
DESCRIPTION:
    Allows you to exit the console.
NOTES:
    Also see, quit.
        """
        exit()

    def do_create(self, arg):
        """
-------------------
FUNCTION: DO_CREATE
-------------------
DESCRIPTION:
    Creates a new instance of BaseModel
    saves it to a JSON file, and prints
    the unique ID generated.
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
        elif arg == 'BaseModel':
            instance = BaseModel()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
-----------------
FUNCTION: DO_SHOW
-----------------
DESCRIPTION:
    Prints out a string representation
    of any instance given that it exists
        """
        if arg == '':
            print("** class name missing **")
            return

        args = self.parse(arg)
        if args[0] != 'BaseModel':
            print("** class doesn't exist **")
            return
        print(args)
        if len(args) < 2:
            print("** instance id missing **")
            return
        dict_of_instances = storage.all()

        if args[0] + '.' + args[1] not in dict_of_instances:
            print("** no instance found **")
        else:
            print(dict_of_instances[args[0] + '.' + args[1]])

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
        buffer = ""
        list_of_words = []

        for i in range(len(cons_str)):
            if cons_str[i] != " ":
                buffer += cons_str[i]
            if cons_str[i] == " " or (i + 1) == len(cons_str):
                if buffer != "":
                    list_of_words.append(buffer)
                    buffer = ""
        return list_of_words

if __name__ == '__main__':
    com = HBNBCommand()
    com.cmdloop()
