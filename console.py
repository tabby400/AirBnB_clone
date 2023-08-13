#!/usr/bin/python3
"""definition of the console"""


import models
import cmd
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }
the_cmds = ['all', 'count', 'show', 'destroy', 'update']


class HBNBCommand(cmd.Cmd):
    """ the hbnb  interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """exit the program using quit.\n"""

        return True

    def do_EOF(self, line):
        """exit the program."""

        print()
        return True

    def emptyline(self):
        """ Nothing to be done"""
        pass

    def do_help(self, line):
        """ help is shown"""
        cmd.Cmd.do_help(self, line)

    def do_create(self, args):
        "Usage: create <class>\n        "
        "creating and printing new class id."
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_inst = classes[class_name]()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, args):
        "Usage: show <class> <id> or <class>.show(<id>)\n        "
        "string rep of a class instance of"
        " a given id."

        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_id = args[1]
        all_inst = models.storage.all()
        found = False
        for key, instance in all_inst.items():
            if class_name in key and class_id in key:
                found = True
                print(instance)
                break
        if not found:
            print("** no instance found **")

    def do_destroy(self, args):
        "Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
        "Deletion of class instance."
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id is missing **")
            return

        found = False
        inst_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_inst = models.storage.all()
        instance = all_inst.pop(key)
        if instance:
            del (instance)
            models.storage.save()
            found = True
        if not found:
            print("** no instance found **")

    def do_all(self, args):
        "Usage: all or all <class> or <class>.all()\n        "
        "String representations of all instances of a given class"
        ".\n        If no class is specified, displays all instantiated "
        "objects."

        args = args.split(" ")
        class_name = args[0]
        if class_name:
            if class_name not in classes:
                print("** class doesn't exist **")
                return
        else:
            all_inst = models.storage.all()
            for key, instances in all_inst.items():
                print([str(instances)])
        if class_name in classes:
            all_inst = models.storage.all()
            for key, instance in all_inst.items():
                if class_name in key:
                    print([str(instance)])

    def do_update(self, args):
        "Usage: update <class> <id> <attribute_name> <attribute_value> or"
        "\n  <class>.update(<id>, <attribute_name>, <attribute_value"
        ">) or\n       <class>.update(<id>, <dictionary>)\n        "
        "Updatating a class instance o id through adding or updating\n   "
        "     a given att key/value pair or dictionary."
        args = args.split()
        class_name = args[0]

        if len(args) < 1:
            print("** class name missing **")
            return
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        inst_id = args[1]
        found = False
        key = "{}.{}".format(class_name, inst_id)
        all_inst = models.storage.all()
        if len(args) < 3:
            print("** atribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]

        for key, instance in all_inst.items():
            if inst_id in key:
                found = True
                if len(args) < 5:
                    setattr(instance,
                            attr_name,
                            attr_value.strip('"'))
                    models.storage.save()

        if not found:
            print("** no instance found **")
            return

    def precmd(self, args):
        """Reformating cmd line for advanced command syntax.
        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''

        if not ('.' in args and '(' in args and ')' in args):
            return args

        try:
            prline = args[:]

            _cls = prline[:prline.find('.')]

            _cmd = prline[prline.find('.') + 1:prline.find('(')]
            if _cmd not in the_cmds:
                raise Exception

            # if parantheses has arguments, parse them
            prline = prline[prline.find('(') + 1:prline.find(')')]
            if prline:
                prline = prline.partition(', ')

                _id = prline[0].replace('\"', '')
                prline = prline[2].strip()
                if prline:

                    if prline[0] == '{' and prline[-1] == '}' \
                            and type(eval(prline)) is dict:
                        _args = prline
                    else:
                        _args = prline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def do_count(self, args):
        "Usage: count <class> or <class>.count()\n        "
        "getthe number of instances of a class."
        count = 0
        all_inst = models.storage.all()
        for key, value in all_inst.items():
            if args[0] in key:
                count = count + 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
