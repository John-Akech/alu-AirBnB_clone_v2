#!/usr/bin/python3
import unittest
from models import storage
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os
from datetime import datetime


# skip these tests if db is not the storage
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not db")
class TestDBStorage(unittest.TestCase):
    """Test DB Storage"""

    def setUp(self):
        """Set up the test environment"""
        self.storage = storage
        self.session = storage._DBStorage__session

    def tearDown(self):
        """Remove storage file at the end of tests"""
        self.session.rollback()
        self.session.close()
        del self.storage

    def test_user(self):
        """Test User"""
        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        self.session.add(user)
        self.session.commit()
        self.assertIn(user.id, self.storage.all(User))
        self.assertEqual(user.name, "Brian")

    def test_city(self):
        """Test City"""
        state = State(name="Kenya")
        self.session.add(state)
        self.session.commit()

        city = City(name="Nairobi")
        city.state_id = state.id
        self.session.add(city)
        self.session.commit()

        self.assertIn(city.id, self.storage.all(City))
        self.assertEqual(city.name, "Nairobi")

    def test_state(self):
        """Test State"""
        state = State(name="Kenya")
        self.session.add(state)
        self.session.commit()

        self.assertIn(state.id, self.storage.all(State))
        self.assertEqual(state.name, "Kenya")

    def test_place(self):
        """Test Place"""
        state = State(name="Kenya")
        self.session.add(state)
        self.session.commit()

        city = City(name="Nairobi")
        city.state_id = state.id
        self.session.add(city)
        self.session.commit()

        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        self.session.add(user)
        self.session.commit()

        place = Place(name="PentHouse", number_rooms=4)
        place.city_id = city.id
        place.user_id = user.id
        self.session.add(place)
        self.session.commit()

        self.assertIn(place.id, self.storage.all(Place))
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.name, "PentHouse")

    def test_amenity(self):
        """Test Amenity"""
        amenity = Amenity(name="Spoon")
        self.session.add(amenity)
        self.session.commit()

        self.assertIn(amenity.id, self.storage.all(Amenity))
        self.assertEqual(amenity.name, "Spoon")

    def test_review(self):
        """Test Review"""
        state = State(name="Kenya")
        self.session.add(state)
        self.session.commit()

        city = City(name="Nairobi")
        city.state_id = state.id
        self.session.add(city)
        self.session.commit()

        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        self.session.add(user)
        self.session.commit()

        place = Place(name="PentHouse", number_rooms="4")
        place.city_id = city.id
        place.user_id = user.id
        self.session.add(place)
        self.session.commit()

        review = Review(text="work smart", place_id=place.id, user_id=user.id)
        self.session.add(review)
        self.session.commit()

        self.assertIn(review.id, self.storage.all(Review))
        self.assertEqual(review.text, "work smart")


if __name__ == '__main__':
    unittest.main()
