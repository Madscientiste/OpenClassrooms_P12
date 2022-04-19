from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import ClientFactory, UserModel, SalesmanFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_admin_can_create_contract(api_client: APIClient, admin: UserModel):
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
