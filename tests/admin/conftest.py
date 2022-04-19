from rest_framework.test import APIClient
import pytest

from tests.factory import UserFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def admin(api_client: APIClient):
    user = UserFactory(is_staff=True, is_superuser=True, is_active=True)
    api_client.force_authenticate(user=user)

    return user
