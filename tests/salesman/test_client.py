"""Salesmans should:
    - have read-only access to all clients, contracts & events
    - should ONLY be able to edit/read the clients, contracts & events they are assigned to
"""

from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import SalesmanFactory, UserFactory, UserModel, ClientFactory, ContractFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_create_client(salesman: UserModel, api_client: APIClient):
    user = UserFactory()

    data = {
        "user": user.id,
        "company_name": faker.company(),
        "mobile": faker.phone_number(),
    }

    response = api_client.post("/api/clients/", data)
    assert response.status_code == 201


def test_can_read_clients(salesman: UserModel, api_client: APIClient):
    ClientFactory.create_batch(3)

    response = api_client.get("/api/clients/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_can_update_client(salesman: UserModel, api_client: APIClient):
    client = ClientFactory()

    data = {
        "company_name": faker.company(),
        "mobile": faker.phone_number(),
    }

    response = api_client.patch(f"/api/clients/{client.id}/", data)
    assert response.status_code == 200
