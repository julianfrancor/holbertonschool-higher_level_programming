#!/usr/bin/python3


"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()


class State(Base):
    """class definition of a State and an instance Base = declarative_base()
        inherits from Base Tips
        links to the MySQL table states
        class attribute id that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        class attribute name that represents a column of a string with
        maximum 128 characters and can’t be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City')
