from django.db import models


class Salesman(models.Model):
    user = models.OneToOneField("web.User", on_delete=models.CASCADE)
