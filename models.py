from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

# No foreign keys because using planetscale.
# I enforce referential integrity at the application level instead of at the database level

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String(50), unique=True)

class ScoreType(Base):
    __tablename__ = 'scoreTypes'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), unique=True)

class Score(Base):
    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, nullable=False)
    scoreDate = Column(DateTime, nullable=False)
    score = Column(Integer, nullable=False)
