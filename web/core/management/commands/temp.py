from django.core.management.base import BaseCommand

from tests.factory import ClientFactory, SalesmanFactory, SupportFactory, EventFactory, ContractFactory


class Command(BaseCommand):
    help = "Temporary command to create users"

    def handle(self, *args, **kwargs):
        # Related
        salesman = SalesmanFactory(user__username="salesman")
        support = SupportFactory(user__username="support")

        client = ClientFactory(sales_contact=salesman)
        contract = ContractFactory(client=client, salesmans=[salesman])
        EventFactory(client=client, contract=contract, support=support)

        # Unrelated
        ClientFactory.create_batch(3)
        ContractFactory.create_batch(3)
        EventFactory.create_batch(3)

        print("Users created")
