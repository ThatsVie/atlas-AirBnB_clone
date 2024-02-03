#!/usr/bin/python3
"""Unittest for Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test cases for the Amenity class """

    def test_name_data_type(self):
        """ Test if name is of type string """
        self.assertIsInstance(Amenity().name, str)

    def test_name_non_empty(self):
        """ Test if name is not None """
        self.assertIsNotNone(Amenity().name)

if __name__ == "__main__":
    unittest.main()
