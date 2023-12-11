from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db

from .crud import create_owner, get_owner_by_dni
from .schemas import CreateOwnerDTO

router = APIRouter(
    prefix="/owners",
    tags=["owners"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", status_code=201)
def create(property: CreateOwnerDTO, db: Session = Depends(get_db)):
    if get_owner_by_dni(db, property["dni"]) is not None:
        raise HTTPException(status_code=400, detail="Owner already exists")

    return create_owner(db=db, owner=property)
