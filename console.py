#!/usr/bin/python3
"""This is a definition of the HBnB console."""
import re
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User
from models.state import State
from models.city import City


def parsing(arg):
    curly_brace = re.search(r"\{(.*?)\}", arg)
    sq_bracket = re.search(r"\[(.*?)\]", arg)
    if curly_brace is None:
        if sq_bracket is None:
            return [p.strip(",") for p in split(arg)]
        else:
            lexer = split(arg[:sq_bracket.span()[0]])
            pars_tok = [p.strip(",") for p in lexer]
            pars_tok.append(sq_bracket.group())
            return (pars_tok)
    else:
        lexer = split(arg[:curly_brace.span()[0]])
        pars_tok = [p.strip(",") for p in lexer]
        pars_tok.append(curly_brace.group())
        return (pars.tok)

class HBNBCommand(cmd.Cmd):
    """this is the command line for hbnb
    Attributes:
        prompt : this is the command prompt.
    """

    prompt = "(hbnb) "
    __classes = classes

    def emptyline(self):
        """nothing to be done"""
        pass
     def default(self, arg):
        """this is shown with invalid input in it"""
        dictArg = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arglen = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arglen[1])
            if match is not None:
                command = [arglen[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in dictArg.keys():
                    call = "{} {}".format(arglen[0], command[1])
                    return dictArg[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """command used to exit console."""
        return True

    def do_EOF(self, arg):
        """used to exit program."""
        print("")
        return True

    def do_create(self, arg):
        """a new class instance is created and
        id printed
        """
        arglen = parse(arg)
        if len(argl) == 0:
             print("** class name missing **")
        elif arglen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """used to show the string rep of a class instance
        """
        arglen = parse(arg)
        objdict = storage.all()
        if len(arglen) == 0:
            print("** class name missing **")
        elif arglen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglen) == 1:
            print("** instance of id missing **")
        elif "{}.{}".format(arglen[0], arglen[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arglen[0], arglen[1])])

    def do_destroy(self, arg):
        """deleting an instance of a class"""
        arglen = parse(arg)
        objdict = storage.all()
        if len(arglen) == 0:
            print("** class name missing **")
        elif arglen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglen) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arglen[0], arglen[1]) not in objdict.keys():
             print("** no instance found **")
        else:
            del objdict["{}.{}".format(arglen[0], arglen[1])]
            storage.save()

    def do_all(self, arg):
        """this is used to show all the string rep of class instances
        if no class then objects instantiated"""

        arglen = parse(arg)
        if len(arglen) > 0 and arglen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objectl = []
            for obj in storage.all().values():
                if len(arglen) > 0 and arglen[0] == obj.__class__.__name__:
                    objectl.append(obj.__str__())
                elif len(arglen) == 0:
                    objectl.append(obj.__str__())
            print(objectl)

    def do_count(self, arg):
        """this gets the number of instances of a class"""
        arglen = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arglen[0] == obj.__class__.__name__:
                count = count + 1
        print(count)

    def do_update(self, arg):
        """used in updating a specific class or attribute"""
        arglen = parse(arg)
        jdict = storage.all()

        if len(arglen) == 0:
            print("** class name missing **")
            return False
        if arglen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arglen) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arglen[0], arglen[1]) not in jdict.keys():
            print("** no instance found **")
            return False
        if len(arglen) == 2:
            print("** attribute name missing **")
            return False
        if len(arglen) == 3:
            try:
                type(eval(arglen[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arglen) == 4:
            obj = jdict["{}.{}".format(arglen[0], arglen[1])]
            if arglen[2] in obj.__class__.__dict__.keys():
                vtype = type(obj.__class__.__dict__[arglen[2]])
                obj.__dict__[arglen[2]] = vtype(arglen[3])
            else:
                obj.__dict__[arglen[2]] = arglen[3]
        elif type(eval(arglen[2])) == dict:
            obj = jdict["{}.{}".format(arglen[0], arglen[1])]
            for k, val in eval(arglen[2]).items():
                 if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    vtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = vtype(val)
                else:
                    obj.__dict__[k] = val
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
