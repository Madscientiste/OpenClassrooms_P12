"""Salesmans should:
    - have read-only access to all clients, contracts & events
    - should ONLY be able to edit/read the clients, contracts & events they are assigned to
"""

from rest_framework.test import APIClient
import pytest
import faker


from tests.factory import EventFactory, SupportFactory, UserModel, ClientFactory, ContractFactory

pytestmark = pytest.mark.django_db
faker = faker.Faker()


def test_can_create_event_for_managed_client(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to create an event for a client"""

    support = SupportFactory()
    client = ClientFactory()
    contract = ContractFactory(client=client, salesmans=[salesman])

    data = {
        "support": support.id,
        "client": client.id,
        "contract": contract.id,
        "event_date": faker.date_time_this_year(),
        "attendees": 4000,
        "notes": faker.text(),
    }

    response = api_client.post("/api/events/", data)
    assert response.status_code == 201


def test_can_read_managed_events(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to read all events for their managed clients"""
    client = ClientFactory(sales_contact=salesman)
    contract = ContractFactory(salesmans=[salesman], client=client)
    event = EventFactory.create_batch(3, contract=contract, client=client)

    response = api_client.get("/api/events/")
    assert response.status_code == 200
    assert len(response.data) >= 3


def test_can_update_managed_event(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to update an event for their managed clients"""
    client = ClientFactory(sales_contact=salesman)
    contract = ContractFactory(salesmans=[salesman], client=client)
    event = EventFactory(contract=contract, client=client)

    data = {"notes": faker.text()}

    response = api_client.patch(f"/api/events/{event.id}/", data)
    assert response.status_code == 200


def test_cant_update_unmanaged_event(salesman: UserModel, api_client: APIClient):
    """Salesmans should not be able to update an event for a client they are not assigned to"""
    client = ClientFactory()
    contract = ContractFactory(client=client)
    event = EventFactory(contract=contract, client=client)

    data = {"notes": faker.text()}

    response = api_client.patch(f"/api/events/{event.id}/", data)
    assert response.status_code == 403


def test_can_read_one_event_for_unmanaged_client(salesman: UserModel, api_client: APIClient):
    """Salesmans should be able to read one event"""

    event = EventFactory()

    response = api_client.get(f"/api/events/{event.id}/")
    assert response.status_code == 200
    assert response.data["id"] == event.id
