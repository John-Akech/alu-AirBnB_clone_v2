#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
from models.base_model import BaseModel
import datetime
import json
import os

class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestBaseModel instance"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Common setup code, if needed"""
        pass

    def tearDown(self):
        """Cleanup code after each test"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
        except Exception as e:
            raise e

    def test_default_behavior(self):
        """Test default behavior of BaseModel instantiation"""
        instance = self.value()
        self.assertIsInstance(instance, self.value)

    def test_kwargs(self):
        """Test BaseModel instantiation with kwargs"""
        instance = self.value()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertIsNot(new_instance, instance)

    def test_kwargs_with_int(self):
        """Test BaseModel instantiation with kwargs containing int"""
        instance = self.value()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**copy)

    def test_save_method(self):
        """Test save method of BaseModel"""
        instance = self.value()
        instance.save()
        key = f'{self.name}.{instance.id}'
        with open('file.json', 'r') as f:
            json_data = json.load(f)
            self.assertEqual(json_data[key], instance.to_dict())

    def test_string_representation(self):
        """Test string representation of BaseModel"""
        instance = self.value()
        expected_str = f'[{self.name}] ({instance.id}) {instance.__dict__}'
        self.assertEqual(str(instance), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel"""
        instance = self.value()
        self.assertEqual(instance.to_dict(), instance.to_dict())

    def test_kwargs_with_none(self):
        """Test BaseModel instantiation with kwargs containing None"""
        kwargs = {None: None}
        with self.assertRaises(TypeError):
            new_instance = self.value(**kwargs)

    def test_kwargs_with_one_key(self):
        """Test BaseModel instantiation with kwargs containing one key"""
        with self.assertRaises(ValueError):
            new_instance = BaseModel(Name='test')  # Fixed the instantiation

    def test_id_type(self):
        """Test the type of the id attribute"""
        new_instance = self.value()
        self.assertIsInstance(new_instance.id, str)

    def test_created_at_type(self):
        """Test the type of the created_at attribute"""
        new_instance = self.value()
        self.assertIsInstance(new_instance.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """Test the type of the updated_at attribute"""
        new_instance = self.value()
        self.assertIsInstance(new_instance.updated_at, datetime.datetime)
        serialized_data = new_instance.to_dict()
        new_instance = BaseModel(**serialized_data)
        self.assertAlmostEqual(new_instance.created_at.timestamp(),
                               new_instance.updated_at.timestamp(), delta=1)

if __name__ == '__main__':
    unittest.main()
