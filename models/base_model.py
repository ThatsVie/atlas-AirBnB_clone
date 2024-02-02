#!/usr/bin/python3
"""
Base Model Class Module for AirBnB project
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self):
        """
        Constructor method for BaseModel.

        Attributes:
        id (str): Unique identifier generated using uuid.uuid4().
        created_at (datetime): Creation timestamp.
        updated_at (datetime): Last update timestamp.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

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
        Update updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
