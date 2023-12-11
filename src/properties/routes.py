from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from src.database import get_db
from src.owners.crud import get_owner

from .crud import (
    create_property,
    get_property,
    get_property_by_internal_code,
    update_property,
)
from .schemas import CreatePropertyDTO, UpdatePropertyPriceDTO
from .services import add_property_image

router = APIRouter(
    prefix="/properties",
    tags=["properties"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", status_code=201)
def create(property: CreatePropertyDTO, db: Session = Depends(get_db)):
    if get_property_by_internal_code(db, property["code_internal"]):
        raise HTTPException(
            status_code=400, detail="Property with this internal code already exists"
        )
    if not get_owner(db, property["owner_id"]):
        raise HTTPException(status_code=404, detail="Owner not found")

    return create_property(db=db, property=property)


@router.post("/{id}/add_image", status_code=201)
def add_image(id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not get_property(db, id):
        raise HTTPException(status_code=404, detail="Property not found")
    try:
        return add_property_image(db=db, property_id=id, file=file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{id}/change_price", status_code=200)
def change_price(id: int, price: UpdatePropertyPriceDTO, db: Session = Depends(get_db)):
    if not get_property(db, id):
        raise HTTPException(status_code=404, detail="Property not found")

    return update_property(db=db, property_id=id, price=price["price"])
