from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client, Support, Salesman, Contract, Event

admin.site.register(Client)
admin.site.register(Support)
admin.site.register(Salesman)
admin.site.register(Contract)
admin.site.register(Event)
