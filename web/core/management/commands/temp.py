from django.core.management.base import BaseCommand

# "users"
from web.auth.models import UserModel
from web.client.models import Client
from web.support.models import Support
from web.sales.models import Salesman

# objects
from web.contract.models import Contract
from web.event.models import Event


class Command(BaseCommand):
    help = "Temporary command to create users"

    def handle(self, *args, **kwargs):
        # 10 clients
        # 4 supports
        # 4 salesmans
        # 2 admin
        # 2 staff

        default_password = "default"

        for i in range(1, 10):
            user = UserModel.objects.create_user(username=f"client{i}", password=default_password)
            user.save()

            client = Client.objects.create(user=user)
            client.save()

        for i in range(1, 4):
            user = UserModel.objects.create_user(username=f"support{i}", password=default_password)
            user.save()

            support = Support.objects.create(user=user)
            support.save()

        for i in range(1, 4):
            user = UserModel.objects.create_user(username=f"salesman{i}", password=default_password)
            user.save()

            salesman = Salesman.objects.create(user=user)
            salesman.save()

        for i in range(1, 2):
            user = UserModel.objects.create_user(username=f"admin{i}", password=default_password, is_staff=True)
            user.is_superuser = True
            user.save()

        print("Users created")
