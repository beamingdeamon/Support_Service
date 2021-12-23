from django.db import models

class Ticket( models.Model):
    subject = models.CharField(max_length=30)
    date = models.DateField(blank=True)