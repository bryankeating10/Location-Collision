from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

# Define the base class for our models
Base = declarative_base()

class Quants(Base):
    __tablename__ = 'quants'
    pass

class Testers(Base):
    __tablename__ = 'testers'
    pass

class Casinos(Base):
    __tablename__ = 'casinos'
    pass

class Accounts(Base):
    __tablename__ = 'accounts'
    pass

class Locations(Base):
    __tablename__ = 'locations'
    pass

class Actions(Base):
    __tablename__ = 'actions'
    pass