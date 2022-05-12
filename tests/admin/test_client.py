from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, UserFactory, ClientFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_create_client(api_client: APIClient, admin: UserModel):
    user = UserFactory()

    data = {
        "user": user.id,
        "company_name": faker.user_name(),
        "mobile": faker.msisdn(),
    }

    response = api_client.post("/api/clients/", data)
    assert response.status_code == 201


def test_can_delete_client(api_client: APIClient, admin: UserModel):
    client = ClientFactory()

    response = api_client.delete(f"/api/clients/{client.id}/")
    assert response.status_code == 204


def test_can_view_all_clients(api_client: APIClient, admin: UserModel):
    ClientFactory.create_batch(3)

    response = api_client.get("/api/clients/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_can_view_one_client(api_client: APIClient, admin: UserModel):
    client = ClientFactory()

    response = api_client.get(f"/api/clients/{client.id}/")
    assert response.status_code == 200
    assert response.data["id"] == client.id


def test_can_update_client(api_client: APIClient, admin: UserModel):
    client = ClientFactory()

    data = {
        "company_name": faker.user_name(),
        "mobile": faker.msisdn(),
    }

    response = api_client.patch(f"/api/clients/{client.id}/", data)
    assert response.status_code == 200
