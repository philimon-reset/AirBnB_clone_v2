#!/usr/bin/python3
"""
    module containing place
"""
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """
        Place class
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    storage_engine = environ.get("HBNB_TYPE_STORAGE")
    reviews = relationship("Review", backref="place")

    @property
    def review(self):
        """getter attribute"""
        result = []
        for review in self.reviews:
            if review.place_id == self.id:
                result.append(review)
        return result
