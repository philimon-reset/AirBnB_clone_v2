#!/usr/bin/python3
"""DB storage
"""
import models
from models.base_model import BaseModel, Base
from models import city, state
from os import environ, getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker, decl_api
from sqlalchemy import create_engine

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """database storage for mysql conversion to set it
    """
    __engine = None
    __session = None

    def __init__(self):
        """initializer for DBStorage for mysql"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)
        env = getenv("HBNB_ENV")
        if (env == "test"):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query the current session and list all instances of cls
        """
        result = {}
        if cls:
            for row in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, row.id)
                row.to_dict()
                result.update({key: row})
        else:
            for table in Base.metadata.tables:
                clss = models.dummy_tables[table]
                for row in self.__session.query(clss).all():
                    key = "{}.{}".format(clss.__name__, row.id)
                    row.to_dict()
                    result.update({key: row})
        return result

    def new(self, obj):
        """add object to current session filler document
        """
        self.__session.add(obj)

    def save(self):
        """commit current done work filler document
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from session filler document
        """
        if (obj is None):
            self.__session.delete(obj)

    def reload(self):
        """reload the session filler document filler
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scope = scoped_session(Session)
        self.__session = Scope()
