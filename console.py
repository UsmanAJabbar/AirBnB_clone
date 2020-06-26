#!/usr/bin/python3
""" slkjdhbflkdsaf """
import cmd

class HBNBCommand(cmd.Cmd):
    """ ksjbhflksb nf;l """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """  skjuhfdlksd """
        exit()

    def do_EOF(self, arg):
        exit()

if __name__ == '__main__':
    com = HBNBCommand()
    com.cmdloop()
