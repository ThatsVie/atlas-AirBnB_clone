#!/usr/bin/python3
"""Unittest for City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Class to test City """

    def test_state_id_data_type(self):
        """Test if state_id is of type string"""
        self.assertIsInstance(City().state_id, str)

    def test_state_id_non_empty(self):
        """Test if state_id is not None"""
        self.assertIsNotNone(City().state_id)

    def test_name_data_type(self):
        """Test if name is of type string"""
        self.assertIsInstance(City().name, str)

    def test_name_non_empty(self):
        """Test if name is not None"""
        self.assertIsNotNone(City().name)

if __name__ == "__main__":
    unittest.main()
