#!/usr/bin/python3
import unittest
import models
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os


# skip these tests if db is not the storage
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not db")
class TestDBStorage(unittest.TestCase):
    """Test DB Storage"""

    def setUp(self):
        """Set up the test environment"""
        self.storage = models.storage

    def tearDown(self):
        """Remove storage file at the end of tests"""
        del self.storage

    def test_user(self):
        """Test User"""
        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        user.save()
        self.assertIn(user.id, self.storage.all())
        self.assertEqual(user.name, "Brian")

    def test_city(self):
        """Test City"""
        state = State(name="Kenya")
        state.save()
        city = City(name="Nairobi")
        city.state_id = state.id
        city.save()
        self.assertIn(city.id, self.storage.all())
        self.assertEqual(city.name, "Nairobi")

    def test_state(self):
        """Test State"""
        state = State(name="Kenya")
        state.save()
        self.assertIn(state.id, self.storage.all())
        self.assertEqual(state.name, "Kenya")

    def test_place(self):
        """Test Place"""
        state = State(name="Kenya")
        state.save()

        city = City(name="Nairobi")
        city.state_id = state.id
        city.save()

        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        user.save()

        place = Place(name="PentHouse", number_rooms=4)
        place.city_id = city.id
        place.user_id = user.id
        place.save()

        self.assertIn(place.id, self.storage.all())
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.name, "PentHouse")

    def test_amenity(self):
        """Test Amenity"""
        amenity = Amenity(name="Spoon")
        amenity.save()
        self.assertIn(amenity.id, self.storage.all())
        self.assertEqual(amenity.name, "Spoon")

    def test_review(self):
        """Test Review"""
        state = State(name="Kenya")
        state.save()

        city = City(name="Nairobi")
        city.state_id = state.id
        city.save()

        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        user.save()

        place = Place(name="PentHouse", number_rooms="4")
        place.city_id = city.id
        place.user_id = user.id
        place.save()

        review = Review(text="work smart", place_id=place.id, user_id=user.id)
        review.save()

        self.assertIn(review.id, self.storage.all())
        self.assertEqual(review.text, "work smart")


if __name__ == '__main__':
    unittest.main()
