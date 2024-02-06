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
        # Check if the file exists before attempting to remove it
    if os.path.exists("file.json"):
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
        
    def test_reload(self):
        initial_keys = list(self.storage.all().keys())
        self.storage.reload()
        reloaded_keys = list(self.storage.all().keys())
        self.assertEqual(reloaded_keys, initial_keys)

    def test_file_path_attribute(self):
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_objects_attribute(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_reload_method_with_existing_file(self):
        initial_keys = list(self.storage.all().keys())
        # Remove the existing file to simulate a fresh start
        os.remove("file.json")
        self.storage.reload()
        reloaded_keys = list(self.storage.all().keys())
        self.assertEqual(reloaded_keys, initial_keys)

if __name__ == '__main__':
    unittest.main()
