from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base
from src.models import Base_at


class Property(Base, Base_at):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    code_internal = Column(String, nullable=False, unique=True)
    year = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id"))

    owner = relationship("Owner", back_populates="properties")
    images = relationship("PropertyImage", back_populates="property")
    traces = relationship("PropertyTrace", back_populates="property")


class PropertyImage(Base, Base_at):
    __tablename__ = "property_images"

    id = Column(Integer, primary_key=True, index=True)
    file_url = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)
    property_id = Column(Integer, ForeignKey("properties.id"))

    property = relationship("Property", back_populates="images")


class PropertyTrace(Base, Base_at):
    __tablename__ = "property_traces"

    id = Column(Integer, primary_key=True, index=True)
    date_sale = Column(DateTime, nullable=False)
    name = Column(String, index=True)
    value = Column(Integer, nullable=False)
    tax = Column(Integer, nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"))

    property = relationship("Property", back_populates="traces")
