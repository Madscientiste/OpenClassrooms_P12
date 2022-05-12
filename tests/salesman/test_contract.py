"""Salesmans should:
    - have read-only access to all clients, contracts & events
    - should ONLY be able to edit/read the clients, contracts & events they are assigned to
"""

from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, ClientFactory, ContractFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_create_contract_for_managed_client(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to create a contract for a managed client"""
    client = ClientFactory(sales_contact=salesman)

    data = {
        "date_created": faker.date_time(),
        "date_updated": faker.date_time(),
        "status": True,
        "amount": faker.random_number(),
        "payment_due": faker.date_time(),
        "client": client.id,
    }

    response = api_client.post("/api/contracts/", data)
    assert response.status_code == 201


def test_can_read_managed_contracts(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to read all contracts for their managed clients"""
    contracts = ContractFactory.create_batch(3)
    for contract in contracts:
        contract.salesmans.set([salesman])

    response = api_client.get("/api/contracts/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_can_validate_managed_contract(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to validate a contract for their managed clients"""
    contract = ContractFactory(status=False)
    contract.salesmans.set([salesman])

    data = {"status": True}

    response = api_client.patch(f"/api/contracts/{contract.id}/", data)
    assert response.status_code == 200


def test_cant_validate_unmanaged_contract(salesman: UserModel, api_client: APIClient):
    """Salesmans should not be able to validate a contract for a client they are not assigned to"""
    contract = ContractFactory(status=False)

    data = {"status": True}

    response = api_client.patch(f"/api/contracts/{contract.id}/", data)
    assert response.status_code == 403
