#!/usr/bin/python3
"""
Base Model Class Module for AirBnB project
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method for BaseModel.

        Attributes:
        id (str): Unique identifier generated using uuid.uuid4().
        created_at (datetime): Creation timestamp.
        updated_at (datetime): Last update timestamp.

        Parameters:
        * args: variable-length list of arguments
        **kwargs: variable-length dictionary of keyword arguments.
        """
        # If instance is being created from a dictionary representation
        if kwargs:
            # If kwargs is not empty, update instance attributes
            for key, value in kwargs.items():
                # Convert string representation of datetime to datetime object
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                # Exclude __class__ from setting as an attribute
                if key != "__class__":
                    setattr(self, key, value)

            # If id is not provided in kwargs, generate a new unique identifier
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()
        else:
            # If instance is being created without a dictionary representation
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            # Register the new instance with the storage system
            storage.new(self)

    def __str__(self):
        """
        String representation of BaseModel.

        Returns:
        str: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """
        Saves instance and updates updated_at attribute to current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
