from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base
from src.models import Base_at


class Owner(Base, Base_at):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dni = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=False)
    photo_url = Column(String, nullable=True)
    birthday = Column(DateTime, nullable=True)

    properties = relationship("Property", back_populates="owner")
