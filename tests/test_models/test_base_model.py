#!/usr/bin/python3
"""
Unittest for BaseModel Class
"""
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Setup a BaseModel instance for testing
        self.base_model = BaseModel()

    def test_to_dict_contains_id(self):
        # Test that to_dict() returns a dictionary containing id attribute
        instance_dict = self.base_model.to_dict()
        self.assertIn('id', instance_dict)

    def test_to_dict_contains_created_at(self):
        # Test that to_dict() returns a dict containing created_at attribute
        instance_dict = self.base_model.to_dict()
        self.assertIn('created_at', instance_dict)

    def test_to_dict_contains_updated_at(self):
        # Test that to_dict() returns a dict containing updated_at attribute
        instance_dict = self.base_model.to_dict()
        self.assertIn('updated_at', instance_dict)

    def test_to_dict_contains_class_attribute(self):
        # Test that to_dict() returns a dict containing __class__ attribute
        instance_dict = self.base_model.to_dict()
        self.assertIn('__class__', instance_dict)

    def test_id_is_string(self):
        # Test that the id attribute is of type string
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        # Test that the created_at attribute is of type datetime
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_str_representation(self):
        # Test the string representation (__str__) of the BaseModel instance
        str_representation = str(self.base_model)
        self.assertIn(self.base_model.__class__.__name__, str_representation)
        self.assertIn(self.base_model.id, str_representation)

    def test_save_updates_updated_at(self):
        # Test that calling save() updates the updated_at attribute
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertTrue(os.path.exists("file.json"))
        updated_at_after_save = self.base_model.updated_at
        self.assertNotEqual(initial_updated_at, updated_at_after_save)

if __name__ == '__main__':
    unittest.main()
