#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Test class for the BaseModel model.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up any necessary resources for the test cases."""
        pass

    def tearDown(self):
        """Clean up any resources created during the test cases."""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test case to check if an instance of \
                BaseModel is created properly."""
        j = self.value()
        self.assertEqual(type(j), self.value)

    def test_kwargs(self):
        """
        Test case to check if an instance of BaseModel\
                can be created with keyword arguments.
        """
        j = self.value()
        copy = j.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is j)

    def test_kwargs_int(self):
        """
        Test case to check if TypeError is raised when\
                creating BaseModel instance with integer keys.
        """
        j = self.value()
        copy = j.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test case to check if the 'save' method saves \
                the BaseModel instance properly."""
        j = self.value()
        j.save()
        key = self.name + "." + j.id
        with open('file.json', 'r') as f:
            i = json.load(f)
            self.assertEqual(i[key], j.to_dict())

    def test_str(self):
        """Test case to check if the 'str' method returns\
                the expected string representation."""
        j = self.value()
        self.assertEqual(str(j), '[{}] ({}) {}'.format(self.name, j.id, i.__dict__))

    def test_todict(self):
        """Test case to check if the 'to_dict' method \
                returns a dictionary representation of the BaseModel instance."""
        j = self.value()
        n = j.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test case to check if TypeError is raised\
                when creating BaseModel instance with None keys."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test case to check if KeyError is raised\
                when creating BaseModel instance with invalid keys."""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test case to check the data type of the 'id' attribute."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test case to check the data\
                type of the 'created_at' attribute."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test case to check the data type of the\
                'updated_at' attribute and their initial values."""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
