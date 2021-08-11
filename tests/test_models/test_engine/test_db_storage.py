#!/usr/bin/python3
"""
    tests for FileStorage
"""
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


class test_DBStorage(unittest.TestCase):
    """
        Base test class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy = DBStorage()

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy

    def test_attrs(self):
        """
            attribute tests
        """
        self.assertTrue(hasattr(self.dummy, "_DBStorage__objects"))
        self.assertTrue(isinstance(self.dummy._DBStorage__engine, sqlalchemy.engine.base.Engine))
        self.assertTrue(hasattr(self.dummy, "_DBStorage__file_path"))
        self.assertTrue(isinstance(self.dummy._DBStorage__session, NoneType))

if __name__ == "__main__":
    unittest.main()
