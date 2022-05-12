"""Support should:
    - have read-only access to all clients, contracts & events
    - should ONLY be able to edit/read the events they are assigned to
"""

from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, ClientFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_read_all_clients(support: UserModel, api_client: APIClient):
    """Test that a support can read all clients"""
    ClientFactory.create_batch(3)

    response = api_client.get("/api/clients/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_cant_edit_client(support: UserModel, api_client: APIClient):
    """Test that a support can't edit a client"""
    client = ClientFactory()

    data = {
        "company_name": faker.user_name(),
        "mobile": faker.msisdn(),
    }

    response = api_client.put(f"/api/clients/{client.id}/", data)
    assert response.status_code == 403
