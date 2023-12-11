from sqlalchemy.orm import Session

from . import models
from .schemas import CreatePropertyDTO


def get_property_by_internal_code(db: Session, code_internal: str) -> models.Property:
    return (
        db.query(models.Property)
        .filter(models.Property.code_internal == code_internal)
        .first()
    )


def get_property(db: Session, property_id: int) -> models.Property:
    return db.query(models.Property).filter(models.Property.id == property_id).first()


def create_property(db: Session, property: CreatePropertyDTO) -> models.Property:
    property = models.Property(**property)
    db.add(property)
    db.commit()
    db.refresh(property)
    return property


def update_property(db: Session, property_id: int, price: float) -> models.Property:
    property = get_property(db, property_id)
    property.price = price
    db.commit()
    db.refresh(property)
    return property


def create_property_image(
    db: Session, property_id: int, image_url: str
) -> models.PropertyImage:
    property_image = models.PropertyImage(property_id=property_id, file_url=image_url)
    db.add(property_image)
    db.commit()
    db.refresh(property_image)
    return property_image
