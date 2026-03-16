from sqlalchemy import Column, Integer, \
    String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

# Define the base class for our models
Base = declarative_base()

class Quants(Base):
    __tablename__ = 'quants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)

class Testers(Base):
    __tablename__ = 'testers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    assigned_quant = Column(Integer, ForeignKey('quants.id'))
    created_at = Column(DateTime, nullable=False)

class Casinos(Base):
    __tablename__ = 'casinos'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    network = Column(String(50), nullable=True)
    signup_rest = Column(Boolean, nullable=False) 
    deposit_rest = Column(Boolean, nullable=False)
    play_rest = Column(Boolean, nullable=False)
    withdrawal_rest = Column(Boolean, nullable=False)
    network_rest = Column(Boolean, nullable=False)
    active = Column(Boolean, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False)

class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    tester_id = Column(Integer, ForeignKey('testers.id'))
    casino_id = Column(Integer, ForeignKey('casinos.id'))
    username = Column(String(50), nullable=True)
    created_at = Column(DateTime, nullable=False)

class Locations(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=True)
    longitude= Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)

class Actions(Base):
    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True)
    category = Column(String(50), nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))
    timestamp = Column(DateTime, nullable=False)