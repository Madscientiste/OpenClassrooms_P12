from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, UserFactory, SalesmanFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_create_salesman(api_client: APIClient, admin: UserModel):
    user = UserFactory()

    response = api_client.post("/api/sales/", {"user": user.id})
    assert response.status_code == 201


def test_can_delete_salesman(api_client: APIClient, admin: UserModel):
    salesman = SalesmanFactory()

    response = api_client.delete(f"/api/sales/{salesman.id}/")
    assert response.status_code == 204


def test_can_view_all_salesmen(api_client: APIClient, admin: UserModel):
    SalesmanFactory.create_batch(10)

    response = api_client.get("/api/sales/")
    assert response.status_code == 200
    assert len(response.data) >= 10


def test_can_view_one_salesman(api_client: APIClient, admin: UserModel):
    salesman = SalesmanFactory()

    response = api_client.get(f"/api/sales/{salesman.id}/")
    assert response.status_code == 200
    assert response.data["id"] == salesman.id
