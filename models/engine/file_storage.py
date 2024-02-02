#!/usr/bin/python3
"""
will correct shortly
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class that manages serialization and deserialization of instances to and 
    from a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves the dictionary of stored objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the stored objects.

        Args:
        obj: instance of a class derived from BaseModel
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes and saves all stored objects to the JSON file.
        """
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            serialized_objects = {key: obj.to_dict() for key,
                                  obj in self.__objects.items()}
            json.dump(serialized_objects,file)

    def reload(self):
        """
        Deserializes and reloads stored objects from the JSON file.
        Ignores if the file is not found (FileNotFoundError).
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                deserialized_objects = json.load(file)
                for key, serialized_object in deserialized_objects.items():
                    class_name = serialized_object['__class__']
                    instance = eval(class_name)(**serialized_object)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
