from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    phone_number = Column(String, default="")
    notifications_enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    profiles = relationship("SavedProfile", back_populates="owner", cascade="all, delete-orphan")

class SavedProfile(Base):
    __tablename__ = "saved_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    relationship_label = Column(String, default="Self")
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    hour = Column(Integer, nullable=False)
    minute = Column(Integer, nullable=False)
    second = Column(Integer, default=0)
    timezone_offset = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    location_name = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="profiles")
