from datetime import datetime
from sqlalchemy import Column, Integer, REAL, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Minutely(Base):
    __tablename__ = "minutely"
    id = Column(Integer, primary_key=True)
    last = Column(REAL)
    bid = Column(REAL)
    ask = Column(REAL)
    timestamp = Column(DateTime, nullable=False)

class Hourly(Base):
    __tablename__ = "hourly"
    id = Column(Integer, primary_key=True)
    last = Column(REAL)
    bid = Column(REAL)
    ask = Column(REAL)
    timestamp = Column(DateTime, nullable=False)

class Daily(Base):
    __tablename__ = "daily"
    id = Column(Integer, primary_key=True)
    last = Column(REAL)
    bid = Column(REAL)
    ask = Column(REAL)
    timestamp = Column(DateTime, nullable=False)
