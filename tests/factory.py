import datetime

from django.utils import timezone
import factory
import faker

from web.auth.models import UserModel
from web.client.models import Client
from web.support.models import Support
from web.sales.models import Salesman

from web.event.models import Event
from web.contract.models import Contract

faker = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    first_name = factory.Faker("user_name")
    last_name = factory.Faker("user_name")

    is_staff = False
    is_superuser = False
    is_active = False


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    user = factory.SubFactory(UserFactory)

    company_name = factory.Faker("user_name")
    mobile = factory.Faker("msisdn")


class SalesmanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Salesman

    user = factory.SubFactory(UserFactory)


class SupportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Support

    user = factory.SubFactory(UserFactory)


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    client = factory.SubFactory(ClientFactory)
    status = True
    amount = factory.Faker("random_number")
    payment_due = factory.Faker("date_time_this_year", tzinfo=timezone.get_current_timezone())

    @factory.post_generation
    def salesmans(self, create, extracted, **kwargs):
        if create and type(extracted) is list:
            self.salesmans.set(extracted)
        elif create and type(extracted) is tuple:
            self.salesmans.set(SalesmanFactory.create_batch(extracted[0]))


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    client = factory.SubFactory(ClientFactory)
    contract = factory.SubFactory(ContractFactory)
    support = factory.SubFactory(SupportFactory)

    attendees = factory.Faker("random_number")
    event_date = factory.Faker("date_time")
    notes = factory.Faker("text")
