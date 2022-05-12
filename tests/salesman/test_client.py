"""Salesmans should:
    - have read-only access to all clients, contracts & events
    - should ONLY be able to edit/read the clients, contracts & events they are assigned to
"""

from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserFactory, UserModel, ClientFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_create_client(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to create a client"""
    user = UserFactory()

    data = {
        "user": user.id,
        "company_name": faker.user_name(),
        "mobile": faker.msisdn(),
    }

    response = api_client.post("/api/clients/", data)
    assert response.status_code == 201


def test_can_read_clients(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to read all clients"""
    ClientFactory.create_batch(3)

    response = api_client.get("/api/clients/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_can_read_managed_client(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to read managed clients"""
    client = ClientFactory()
    client.sales_contact = salesman

    response = api_client.get(f"/api/clients/{client.id}/")
    assert response.status_code == 200
    assert response.data["id"] == client.id


def test_can_read_unmanaged_client(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to read unmanaged clients"""
    client = ClientFactory()
    client.sales_contact = salesman

    response = api_client.get(f"/api/clients/{client.id}/")
    assert response.status_code == 200
    assert response.data["id"] == client.id


def test_can_update_managed_client(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to update managed clients"""
    client = ClientFactory(sales_contact=salesman)

    data = {
        "company_name": faker.user_name(),
        "mobile": faker.msisdn(),
    }

    response = api_client.patch(f"/api/clients/{client.id}/", data)
    assert response.status_code == 200


def test_cant_update_unmanaged_client(salesman: UserModel, api_client: APIClient):
    """Salesmans should NOT be able to update unmanaged clients"""
    client = ClientFactory()

    data = {
        "company_name": faker.user_name(),
        "mobile": faker.msisdn(),
    }

    response = api_client.patch(f"/api/clients/{client.id}/", data)
    assert response.status_code == 403
