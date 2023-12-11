from pydantic import BaseModel


class CreatePropertyDTO(BaseModel):
    name: str
    address: str
    price: float
    code_internal: str
    year: int
    owner_id: int

    def validate(cls, body):
        if "name" not in body:
            raise ValueError("Name is required")
        if len(body["name"]) < 3:
            raise ValueError("Please enter a valid name")
        if "address" not in body:
            raise ValueError("Address is required")
        if len(body["address"]) < 5:
            raise ValueError("Please enter a valid address")
        if "price" not in body:
            raise ValueError("Price is required")
        if body["price"] <= 0:
            raise ValueError("Please enter a valid price")
        if "code_internal" not in body:
            raise ValueError("Code internal is required")
        if len(body["code_internal"]) < 3:
            raise ValueError("Please enter a valid code internal")
        if "year" not in body:
            raise ValueError("Year is required")
        if body["year"] <= 0:
            raise ValueError("Please enter a valid year")
        if "owner_id" not in body:
            raise ValueError("Owner id is required")
        if body["owner_id"] <= 0:
            raise ValueError("Please enter a valid owner id")
        return body


class UpdatePropertyPriceDTO(BaseModel):
    price: float

    def validate(cls, body):
        if "price" not in body:
            raise ValueError("Price is required")
        if body["price"] <= 0:
            raise ValueError("Please enter a valid price")
        return body
