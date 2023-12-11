from sqlalchemy import Column, DateTime, func

"""
Base class to add created_at, updated_at and deleted_at columns to all tables
"""


class Base_at:
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
