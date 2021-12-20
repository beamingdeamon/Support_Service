from .models import TicketMessage
from .models import Ticket
from rest_framework import serializers

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'subject', 'date']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketMessage
        fields = ['id','ticket_id', 'user_id', 'message']