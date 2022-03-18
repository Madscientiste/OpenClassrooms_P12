from django.db import models


class Salesman(models.Model):
    user = models.OneToOneField("authentification.UserModel", on_delete=models.CASCADE)
