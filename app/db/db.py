from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import Base

# Database connection URL
DATABASE_URL = 'postgresql+psycopg2://sunbird:sunbird@db:5432/sunbird_db'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Function to create the tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Dependency to get a session
def get_session():
    return SessionLocal()