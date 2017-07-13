# seems like Shelter.id gives a foreign key to Puppy.shelter_id.

# This documentation exists in order to create new database using sqlalchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    # Shelter table
    # name, address, city, state, zipCode, website, id,
    __tablename__ = 'shelter'
    name = Column(String, nullable = False)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zipCode = Column(Integer)
    website = Column(String)
    id = Column(Integer, primary_key = True)


class Puppy(Base):
    # Puppy tables
    # name, date of birth, gender, weight, shelter_id, picture
    __tablename__ = 'puppy'
    name = Column(String, primary_key = True)
    birthday = Column(Date, nullable = False)
    gender = Column(Integer)
    weight = Column(Integer)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    picture = Column(String)
    shelter = relationship(Shelter)

# engine = create_engine('sqlite:///puppy.db')
Base.metadata.create_all(engine)
