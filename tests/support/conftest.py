from rest_framework.test import APIClient
import pytest

from tests.factory import SupportFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def support(api_client: APIClient):
    support = SupportFactory()
    api_client.force_authenticate(user=support.user)
    return support
