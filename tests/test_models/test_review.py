#!/usr/bin/python3
""" Unittest for Review """
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_place_id_data_type(self):
        self.assertIsInstance(Review().place_id, str)

    def test_user_id_data_type(self):
        self.assertIsInstance(Review().user_id, str)

    def test_text_data_type(self):
        self.assertIsInstance(Review().text, str)

    def test_place_id_not_none(self):
        self.assertIsNotNone(Review().place_id)

    def test_user_id_not_none(self):
        self.assertIsNotNone(Review().user_id)

    def test_text_not_none(self):
        self.assertIsNotNone(Review().text)

if __name__ == "__main__":
    unittest.main()
