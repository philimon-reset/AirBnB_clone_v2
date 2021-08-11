#!/usr/bin/python3
"""test for console to make it start working"""
import unittest
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


class TestConsole(unittest.TestCase):
    """this will test the console"""

    def StartupClass(cls):
        """setup for the test"""
        cls.console = HBNBCommand()


if __name__ == "__main__":
    unittest.main()
