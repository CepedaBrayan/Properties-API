from sqlalchemy.orm import Session

from . import models
from .schemas import CreateOwnerDTO


def get_owner(db: Session, owner_id: int) -> models.Owner:
    return db.query(models.Owner).filter(models.Owner.id == owner_id).first()


def get_owner_by_dni(db: Session, dni: int) -> models.Owner:
    return db.query(models.Owner).filter(models.Owner.dni == dni).first()


def create_owner(db: Session, owner: CreateOwnerDTO) -> models.Owner:
    db_owner = models.Owner(**owner)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner
