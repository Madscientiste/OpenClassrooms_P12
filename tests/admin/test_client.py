from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, UserFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_admin_can_create_client(api_client: APIClient, admin: UserModel):
    user = UserFactory()

    data = {
        "user": user.id,
        "company_name": faker.company(),
        "mobile": faker.phone_number(),
    }

    response = api_client.post("/api/clients/", data)
    assert response.status_code == 201
