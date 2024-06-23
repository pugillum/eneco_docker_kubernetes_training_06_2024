from sqlalchemy import Column, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class BikeRides(Base):
    __tablename__ = "bike_rides"

    uuid = Column(String, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    created = Column(DateTime)
