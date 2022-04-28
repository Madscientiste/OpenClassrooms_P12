from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, UserFactory, SupportFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_create_support(api_client: APIClient, admin: UserModel):
    user = UserFactory()

    response = api_client.post("/api/supports/", {"user": user.id})
    assert response.status_code == 201


def test_can_delete_support(api_client: APIClient, admin: UserModel):
    support = SupportFactory()

    response = api_client.delete(f"/api/supports/{support.id}/")
    assert response.status_code == 204


def test_can_view_all_supports(api_client: APIClient, admin: UserModel):
    SupportFactory.create_batch(10)

    response = api_client.get("/api/supports/")
    assert response.status_code == 200
    assert len(response.data) >= 10


def test_can_view_one_support(api_client: APIClient, admin: UserModel):
    support = SupportFactory()

    response = api_client.get(f"/api/supports/{support.id}/")
    assert response.status_code == 200
    assert response.data["id"] == support.id
