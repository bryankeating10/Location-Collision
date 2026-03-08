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
    assigned_quant = Column(Integer, ForeignKey='quants.id')
    created_at = Column(DateTime, nullable=False)

class Casinos(Base):
    __tablename__ = 'casinos'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    network = Column(String(50), nullable=True)
    signup_rest = Column(Boolean, nullable=False) # True if the casino has a signup restriction, False otherwise
    deposit_rest = Column(Boolean, nullable=False) # True if the casino has a deposit restriction, False otherwise
    play_rest = Column(Boolean, nullable=False)
    withdrawal_rest = Column(Boolean, nullable=False)
    network_rest = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)