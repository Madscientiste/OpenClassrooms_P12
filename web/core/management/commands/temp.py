from django.core.management.base import BaseCommand

from tests.factory import UserFactory, ClientFactory, SalesmanFactory, SupportFactory, EventFactory, ContractFactory

# "users"
from web.auth.models import UserModel


class Command(BaseCommand):
    help = "Temporary command to create users"

    def handle(self, *args, **kwargs):
        SalesmanFactory.create_batch(3)
        ClientFactory.create_batch(3)
        SupportFactory.create_batch(3)
        EventFactory.create_batch(3)
        ContractFactory.create_batch(3)

        print("Users created")
