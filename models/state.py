#!/usr/bin/python3
"""
    contains state class to represent a state
"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class: class to represent states of cities"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """cities list
        """
        result = []
        for j, i in models.storage.all(models.city.City).items():
            if (i.state_id == self.id):
                result.append(i)
        return result
