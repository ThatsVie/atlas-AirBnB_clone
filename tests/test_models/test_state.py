#!/usr/bin/python3
"""Unittest for State Class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_state_name_type(self):
        """Test if the name attribute is a string"""
        state_instance = State()
        self.assertIsInstance(state_instance.name, str)

    def test_state_name_not_none(self):
        """Test if the name attribute is not None"""
        state_instance = State()
        self.assertIsNotNone(state_instance.name)

    def test_state_default_name(self):
        """Test if name attribute is an empty string by default"""
        state_instance = State()
        self.assertEqual(state_instance.name, "")

    def test_state_update_name(self):
        """Test updating the name attribute"""
        state_instance = State()
        state_instance.name = "Oklahoma"
        self.assertEqual(state_instance.name, "Oklahoma")
