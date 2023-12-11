import datetime

from pydantic import BaseModel


class CreateOwnerDTO(BaseModel):
    name: str
    dni: str
    address: str
    photo_url: str
    birthday: str

    def validate(cls, body):
        if "name" not in body:
            raise ValueError("Name is required")
        if len(body["name"]) < 3:
            raise ValueError("Please enter a valid name")
        if "dni" not in body:
            raise ValueError("DNI is required")
        if len(body["dni"]) < 5:
            raise ValueError("Please enter a valid dni")
        if "address" not in body:
            raise ValueError("Address is required")
        if len(body["address"]) < 5:
            raise ValueError("Please enter a valid address")
        if "birthday" in body:
            # check if birthday is valid like "mm/dd/yyyy"
            try:
                datetime.datetime.strptime(body["birthday"], "%m/%d/%Y")
            except ValueError:
                raise ValueError("Please enter a valid birthday")
        return body
