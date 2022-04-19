from rest_framework.test import APIClient
import pytest

from web.auth.models import UserModel
from web.client.models import Client
from web.support.models import Support

from web.event.models import Event
from web.contract.models import Contract


@pytest.fixture
def api_client():
    return APIClient(format="json")
