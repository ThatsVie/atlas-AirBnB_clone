#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    # Look for the text enclosed in curly braces {}
    curly_braces_match = re.search(r"\{(.*?)\}", arg)
    
    # Look for text enclosed in square brackets []
    square_brackets_match = re.search(r"\[(.*?)\]", arg)

    if curly_braces_match is None:
        # No curly braces found, check for square brackets
        if square_brackets_match is None:
            # No brackets found, split the argument using shlex
            return [token.strip(",") for token in split(arg)]
        else:
            # Brackets found, split the argument up to opening bracket
            lexer_tokens = split(arg[:square_brackets_match.span()[0]])
            result_tokens = [token.strip(",") for token in lexer_tokens]
            result_tokens.append(square_brackets_match.group())
            return result_tokens
    else:
        # Curly braces found, split the argument up to opening curly brace
        lexer_tokens = split(arg[:curly_braces_match.span()[0]])
        result_tokens = [token.strip(",") for token in lexer_tokens]
        result_tokens.append(curly_braces_match.group())
        return result_tokens


class HBNBCommand(cmd.Cmd):
    """
    Defines the command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        supported_commands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        # Check if the input argument contains a dot (indicating a method call)
        match_dot = re.search(r"\.", arg)
        if match_dot is not None:
            # Split the argument into two parts before and after the dot
            parts = [arg[:match_dot.span()[0]], arg[match_dot.span()[1]:]]
            # Check if the second part contains parentheses
            match_parentheses = re.search(r"\((.*?)\)", parts[1])
            if match_parentheses is not None:
                # Extract the command and its parameters
                command = [
                    parts[1][:match_parentheses.span()[0]],
                    match_parentheses.group()[1:-1]
                ]
                if command[0] in supported_commands:
                    # Construct full method call, execute corresponding method
                    full_call = "{} {}".format(parts[0], command[1])
                    return supported_commands[command[0]](full_call)

        # Print an error message for unknown syntax and return False
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """

        # Parse the argument into a list of tokens
        tokens = parse(arg)

        # Access the dictionary containing all instances

        obj_dict = storage.all()

        if len(tokens) == 0:
            # No class name provided
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.__classes:
            # Invalid class name
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            # No instance id provided
            print("** instance id missing **")
        elif "{}.{}".format(tokens[0], tokens[1]) not in obj_dict:
            # No instance found with the given id
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(tokens[0], tokens[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """

        # Parse the argument into a list of tokens
        tokens = parse(arg)

        # Access the dictionary containing all instances
        obj_dict = storage.all()
        if len(tokens) == 0:
            # No class name provided
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.__classes:
            # Invalid class name
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            # No instance id provided
            print("** instance id missing **")
        elif "{}.{}".format(tokens[0], tokens[1]) not in obj_dict.keys():
            # No instance found with the given id
            print("** no instance found **")
        else:
            # Delete the instance from the dictionary
            del obj_dict["{}.{}".format(tokens[0], tokens[1])]
            # Save the changes to storage
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        # Parse the argument into a list of tokens
        tokens = parse(arg)

        if len(tokens) > 0 and tokens[0] not in HBNBCommand.__classes:
            # Check if the specified class exists
            print("** class doesn't exist **")
        else:
            # List to store string representations of instances
            instance_str_list = []

            # Iterate through all instances in storage
            for obj in storage.all().values():
                if len(tokens) > 0 and tokens[0] == obj.__class__.__name__:
                    # Check if the instance belongs to the specified class
                    instance_str_list.append(obj.__str__())
                elif len(tokens) == 0:
                    # If no class is specified, include all instances
                    instance_str_list.append(obj.__str__())
            # Print the list of string representations
            print(instance_str_list)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        # Parse the argument into a list of tokens
        tokens = parse(arg)

        # Initialize a counter for the number of instances
        count = 0

        # Iterate through all instances in storage
        for obj in storage.all().values():
            # Check if the instance belongs to the specified class
            if tokens[0] == obj.__class__.__name__:
                count += 1
        # Print the count of instances
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        # Parse the argument into a list of tokens
        tokens = parse(arg)

        # Access the dictionary containing all instances
        instances_dict = storage.all()

        # Check for missing class name
        if len(tokens) == 0:
            print("** class name missing **")
            return False

        # Check if the specified class exists
        if tokens[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        # Check for missing instance id
        if len(tokens) == 1:
            print("** instance id missing **")
            return False

        # Check if the instance with the specified id exists
        if "{}.{}".format(tokens[0], tokens[1]) not in instances_dict.keys():
            print("** no instance found **")
            return False

        # Check for missing attribute name
        if len(tokens) == 2:
            print("** attribute name missing **")
            return False

        # Check for missing attribute value (dictionary)
        if len(tokens) == 3:
            try:
                type(eval(tokens[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        # Update the instance based on the arguments
        if len(tokens) == 4:
            obj = instances_dict["{}.{}".format(tokens[0], tokens[1])]

            # Check if the attribute exists in the class definition
            if tokens[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[tokens[2]])
                obj.__dict__[tokens[2]] = val_type(tokens[3])
            else:
                obj.__dict__[tokens[2]] = tokens[3]
        elif type(eval(tokens[2])) == dict:
            obj = instances_dict["{}.{}".format(tokens[0], tokens[1])]

            # Iterate through key-value pairs in the provided dictionary
            for k, v in eval(tokens[2]).items():
                # Check if key exists in class definition and has a valid type
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(v)
                else:
                    obj.__dict__[k] = v
        # Save the changes to storage
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
