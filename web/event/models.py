from django.db import models


class Event(models.Model):
    client = models.ForeignKey("client.Client", on_delete=models.CASCADE)
    contract = models.ForeignKey("contract.Contract", on_delete=models.CASCADE)
    support = models.ForeignKey("support.Support", on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()
