from test.setup import client
from unittest import TestCase, mock

from src.properties.models import PropertyImage

prefix = "/api/v1/properties"


class TestPropertiesRoutes(TestCase):
    owner = client.post(
        "/api/v1/owners/create",
        json={
            "dni": "1234555",
            "name": "John Doe 2",
            "address": "Av. 123 45 67",
        },
    )
    property = client.post(
        f"{prefix}/create",
        json={
            "name": "My property2",
            "address": "Av. 123 45 678",
            "price": 1000,
            "code_internal": "123456789",
            "year": 2020,
            "owner_id": owner.json()["id"],
        },
    )
    property_image = PropertyImage(
        file_url="https://www.google.com",
        property_id=property.json()["id"],
    )

    @staticmethod
    def get_property_image(db, property_id, file):
        return TestPropertiesRoutes.property_image

    def test_create_property(self):
        self.property = client.post(
            f"{prefix}/create",
            json={
                "name": "My property",
                "address": "Av. 123 45 67",
                "price": 1000,
                "code_internal": "123456",
                "year": 2020,
                "owner_id": self.owner.json()["id"],
            },
        )
        self.assertEqual(self.property.status_code, 201)

    def test_change_price(self):
        _r = client.patch(
            f"{prefix}/{self.property.json()['id']}/change_price",
            json={"price": 2000},
        )
        self.assertEqual(_r.status_code, 200)

    # mock.patch is used to mock the add_property_image function for avoiding
    # the actual upload of the image to the cloud storage.
    @mock.patch("src.properties.routes.add_property_image", get_property_image)
    def test_add_image(self):
        _r = client.post(
            f"{prefix}/{self.property.json()['id']}/add_image",
            files={"file": open("test/properties/images/jarvis.jpg", "rb")},
        )
        print(_r.json(), "<<<")
        self.assertEqual(_r.status_code, 201)
        self.assertEqual(_r.json()["file_url"], self.property_image.file_url)
