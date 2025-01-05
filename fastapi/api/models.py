from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

workout_routine_association = Table(
    'workout_routine', Base.metadata,
)