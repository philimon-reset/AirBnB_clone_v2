#!/usr/bin/python3
"""
    contains review class to represent reviews
"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey


class Review(BaseModel, Base):
    """
        Review class
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey(Place.id))
    user_id = Column(String(60), ForeignKey(User.id))
    text = Column(String(1024), nullable=False)
