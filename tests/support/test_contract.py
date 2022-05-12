"""Support should:
    - have read-only access to all clients, contracts & events
    - should ONLY be able to edit/read the events they are assigned to
"""

from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, ClientFactory, ContractFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_read_all_contracts(support: UserModel, api_client: APIClient):
    """Test that a support can read all contracts"""
    ContractFactory.create_batch(3)

    response = api_client.get("/api/contracts/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_cant_edit_contract(support: UserModel, api_client: APIClient):
    """Test that a support can't edit a contract"""
    contract = ContractFactory()

    response = api_client.put(f"/api/contracts/{contract.id}/", {})
    assert response.status_code == 403
    