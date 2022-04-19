from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, UserFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_admin_can_create_one_user(api_client: APIClient, admin: UserModel):
    password = faker.password()

    data = {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": password,
        "password2": password,
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
    }

    response = api_client.post("/api/users/", data)
    assert response.status_code == 201


# TODO: remove username & password from validation on patch
# def test_admin_can_edit_user(api_client: APIClient, admin: UserModel):
#     user = UserFactory()
#     new_first_name = faker.first_name()

#     response = api_client.patch(f"/api/users/{user.id}/", {"first_name": new_first_name})
#     assert response.status_code == 200
#     assert response.data["first_name"] == new_first_name


def test_admin_can_view_all_users(api_client: APIClient, admin: UserModel):
    UserFactory.create_batch(10)

    response = api_client.get("/api/users/")
    assert response.status_code == 200
    assert len(response.data) >= 10


def test_admin_can_view_one_user(api_client: APIClient, admin: UserModel):
    user = UserFactory()

    response = api_client.get(f"/api/users/{user.id}/")
    assert response.status_code == 200
    assert response.data["id"] == user.id
