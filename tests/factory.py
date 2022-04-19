import factory
import faker

from web.auth.models import UserModel
from web.client.models import Client
from web.support.models import Support
from web.sales.models import Salesman

from web.event.models import Event
from web.contract.models import Contract


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    is_staff = False
    is_superuser = False
    is_active = False


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    user = factory.SubFactory(UserFactory)

    company_name = factory.Faker("company")
    mobile = factory.Faker("phone_number")


class SalesmanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Salesman

    user = factory.SubFactory(UserFactory)
