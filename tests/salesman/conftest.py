from rest_framework.test import APIClient
import pytest

from tests.factory import UserFactory, SalesmanFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def admin(api_client: APIClient):
    sales = SalesmanFactory()
    api_client.force_authenticate(user=sales.user)
    return sales
