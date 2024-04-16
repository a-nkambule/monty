#!/usr/bin/python3
""" Module for testing db_storage """
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """Unit tests for the DBStorage class."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test the all() method of DBStorage."""
        storage = DBStorage()
        storage.reload()
        state = State(name="California")
        city = City(name="San Francisco", state_id=state.id)
        user = User(email="test@example.com", password="password")
        place = Place(name="Cozy Apartment", city_id=city.id, user_id=user.id)
        review = Review(text="Great place!", place_id=place.id, user_id=user.id)
        amenity = Amenity(name="WiFi")
        storage.new(state)
        storage.new(city)
        storage.new(user)
        storage.new(place)
        storage.new(review)
        storage.new(amenity)
        storage.save()

        # Test all() with cls=None
        all_objs = storage.all()
        expected_output = ("State.{}\nCity.{}\nUser.{}\nPlace.{}\nReview.{}\nAmenity.{}\n"
                           .format(state.id, city.id, user.id, place.id, review.id, amenity.id))
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(all_objs["State.{}".format(state.id)], state)
        self.assertEqual(all_objs["City.{}".format(city.id)], city)
        self.assertEqual(all_objs["User.{}".format(user.id)], user)
        self.assertEqual(all_objs["Place.{}".format(place.id)], place)
        self.assertEqual(all_objs["Review.{}".format(review.id)], review)
        self.assertEqual(all_objs["Amenity.{}".format(amenity.id)], amenity)
