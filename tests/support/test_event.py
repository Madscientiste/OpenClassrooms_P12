"""Support should:
    - have read-only access to all clients, contracts & events
    - should ONLY be able to edit/read the events they are assigned to
"""

from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import UserModel, EventFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_read_all_events(support: UserModel, api_client: APIClient):
    """Test that a support can read all events"""
    EventFactory.create_batch(3)

    response = api_client.get("/api/events/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_can_update_managed_event(support: UserModel, api_client: APIClient):
    """Test that a support can update an event"""
    event = EventFactory(support=support)

    data = {
        "notes": faker.sentence(),
    }

    response = api_client.patch(f"/api/events/{event.id}/", data)
    assert response.status_code == 200


def test_cant_update_unmanaged_event(support: UserModel, api_client: APIClient):
    """Test that a support can't update an event"""
    event = EventFactory()

    response = api_client.patch(f"/api/events/{event.id}/", {})
    assert response.status_code == 403
