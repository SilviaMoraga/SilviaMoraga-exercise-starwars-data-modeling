import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    userName = Column(String(25), unique=True)
    email = Column(String(20), nullable=False)
    password = Column(String(10), nullable=False)
    firstName = Column(String(20), nullable=False)
    lastName = Column(String(20), nullable=True)
    subscriptionDate = Column(Date, nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    population = Column(Integer, nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(15), unique=True)
    model = Column(String(10), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    height = Column(Integer, nullable=False)
    planet = Column(Integer, ForeignKey('planets.id'))
    planets_idRelationship = relationship(Planets)
    starship = Column(Integer, ForeignKey('starships.id'), unique=True)
    starships_idRelationship = relationship(Starships)

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user_idRelationship = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters_idRelationship = relationship(Characters)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user_idRelationship = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets_idRelationship = relationship(Planets)

class FavoriteStarships(Base):
    __tablename__ = 'favorite_starships'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.user_id'))
    user_idRelationship = relationship(User)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships_idRelationship = relationship(Starships)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
