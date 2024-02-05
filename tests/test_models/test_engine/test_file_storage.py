import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()
        self.storage = FileStorage()
        self.storage.save()

    def tearDown(self):
        del self.model
        del self.storage
        os.remove("file.json")

    def test_new_method(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        stored_objects = self.storage.all()
        self.assertIn(new_model, stored_objects.values())

    def test_all_method(self):
        new_model = BaseModel()
        stored_objects = self.storage.all()
        self.assertIsInstance(stored_objects, dict)
        self.assertIn(new_model, stored_objects.values())

    def test_save_method(self):
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", mode="r", encoding="utf-8") as file:
            file_content = file.read()
        self.assertTrue(len(file_content) > 0)
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
                       file_content)
        
    def test_reload_method(self):
        self.assertEqual(self.storage.all(), {})
        self.assertTrue(len(self.storage.all()) == 0)
        self.storage.reload()
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
                      self.storage.all().keys())
         
if __name__ == '__main__':
    unittest.main()
