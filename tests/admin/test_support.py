from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, UserFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_admin_can_create_support(api_client: APIClient, admin: UserModel):
    user = UserFactory()

    response = api_client.post("/api/supports/", {"user": user.id})
    assert response.status_code == 201
