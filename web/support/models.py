from django.db import models


class Support(models.Model):
    user = models.OneToOneField("authentification.UserModel", on_delete=models.CASCADE)
