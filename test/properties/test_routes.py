from test.setup import client
from unittest import TestCase

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
