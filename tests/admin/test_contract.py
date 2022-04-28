from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, ClientFactory, SalesmanFactory, ContractFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_create_contract(api_client: APIClient, admin: UserModel):
    salesmans = SalesmanFactory.create_batch(3)
    client = ClientFactory()

    data = {
        "date_created": faker.date_time(),
        "date_updated": faker.date_time(),
        "status": True,
        "amount": faker.random_number(),
        "payment_due": faker.date_time(),
        "client": client.id,
        "salesmans": [salesman.id for salesman in salesmans],
    }

    response = api_client.post("/api/contracts/", data)
    assert response.status_code == 201


def test_can_delete_contract(api_client: APIClient, admin: UserModel):
    contract = ContractFactory()
    salesmans = SalesmanFactory.create_batch(3)
    contract.salesmans.set(salesmans)

    response = api_client.delete(f"/api/contracts/{contract.id}/")
    assert response.status_code == 204


def test_can_view_all_contracts(api_client: APIClient, admin: UserModel):
    contracts = ContractFactory.create_batch(3)
    salesmans = SalesmanFactory.create_batch(3)
    for contract in contracts:
        contract.salesmans.set(salesmans)

    response = api_client.get("/api/contracts/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_can_view_one_contract(api_client: APIClient, admin: UserModel):
    contract = ContractFactory()
    salesmans = SalesmanFactory.create_batch(3)
    contract.salesmans.set(salesmans)

    response = api_client.get(f"/api/contracts/{contract.id}/")
    assert response.status_code == 200
    assert response.data["id"] == contract.id
