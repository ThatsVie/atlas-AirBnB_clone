#!/usr/bin/python3
"""Unittest for Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test cases for the Place class """

    def test_city_id_data_type(self):
        self.assertIsInstance(Place().city_id, str)

    def test_user_id_data_type(self):
        self.assertIsInstance(Place().user_id, str)

    def test_name_data_type(self):
        self.assertIsInstance(Place().name, str)

    def test_description_data_type(self):
        self.assertIsInstance(Place().description, str)

    def test_number_rooms_data_type(self):
        self.assertIsInstance(Place().number_rooms, int)

    def test_number_bathrooms_data_type(self):
        self.assertIsInstance(Place().number_bathrooms, int)

    def test_max_guest_data_type(self):
        self.assertIsInstance(Place().max_guest, int)

    def test_price_by_night_data_type(self):
        self.assertIsInstance(Place().price_by_night, int)

    def test_latitude_data_type(self):
        self.assertIsInstance(Place().latitude, float)

    def test_longitude_data_type(self):
        self.assertIsInstance(Place().longitude, float)

    def test_amenity_ids_data_type(self):
        self.assertIsInstance(Place().amenity_ids, list)

    def test_city_id_not_none(self):
        self.assertIsNotNone(Place().city_id)

    def test_user_id_not_none(self):
        self.assertIsNotNone(Place().user_id)

    def test_name_not_none(self):
        self.assertIsNotNone(Place().name)

    def test_description_not_none(self):
        self.assertIsNotNone(Place().description)

    def test_number_rooms_not_none(self):
        self.assertIsNotNone(Place().number_rooms)

    def test_number_bathrooms_not_none(self):
        self.assertIsNotNone(Place().number_bathrooms)

    def test_max_guest_not_none(self):
        self.assertIsNotNone(Place().max_guest)

    def test_price_by_night_not_none(self):
        self.assertIsNotNone(Place().price_by_night)

    def test_latitude_not_none(self):
        self.assertIsNotNone(Place().latitude)

    def test_longitude_not_none(self):
        self.assertIsNotNone(Place().longitude)

    def test_amenity_ids_not_none(self):
        self.assertIsNotNone(Place().amenity_ids)

if __name__ == "__main__":
    unittest.main()
