from django.db import models


class Support(models.Model):
    user = models.OneToOneField("web.User", on_delete=models.CASCADE)
