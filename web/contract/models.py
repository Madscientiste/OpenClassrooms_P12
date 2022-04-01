from django.db import models


class Contract(models.Model):
    client = models.ForeignKey("client.Client", on_delete=models.CASCADE)
    sales_contact = models.ManyToManyField("sales.Salesman")
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    status = models.BooleanField(default=True)
    amount = models.FloatField()
    payment_due = models.DateTimeField()
