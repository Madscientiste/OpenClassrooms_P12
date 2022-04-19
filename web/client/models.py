from django.db import models

from web.contract.models import Contract


class Client(models.Model):
    user = models.OneToOneField("authentification.UserModel", on_delete=models.CASCADE)

    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def is_validated(self):
        return Contract.objects.filter(client=self).count() > 0

    