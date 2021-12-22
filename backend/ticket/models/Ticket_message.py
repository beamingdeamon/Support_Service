from django.db import models

class TicketMessage(models.Model):
    ticket_id = models.ForeignKey('Ticket',on_delete=models.CASCADE,blank=True)
    user_id = models.IntegerField(blank=True)
    message = models.CharField(max_length=1000)