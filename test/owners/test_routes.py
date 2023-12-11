from test.setup import client
from unittest import TestCase

prefix = "/api/v1/owners"


class TestOwnerRoutes(TestCase):
    def test_create_owner(self):
        _r = client.post(
            f"{prefix}/create",
            json={
                "dni": "1234567890",
                "name": "John Doe",
                "address": "Av. 123 45 67",
            },
        )
        self.assertEqual(_r.status_code, 201)
