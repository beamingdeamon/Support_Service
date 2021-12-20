from django.shortcuts import render
from .models import Ticket
from .models import TicketMessage
from datetime import date
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
import json
from rest_framework import generics
from . import serializers
# Create your views here.
@permission_classes((permissions.AllowAny,))
class CreateTicket(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        ticket = Ticket(subject = data['subject'], date = date.today())
        ticket.save()
        return Response(request.data)

@permission_classes((permissions.AllowAny,))
class GetTickets(generics.ListAPIView):
        queryset = Ticket.objects.all()
        serializer_class = serializers.TicketSerializer


@permission_classes((permissions.AllowAny,))
class CreateMessage(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        ticket = TicketMessage(ticket_id = Ticket.objects.get(id=data['ticket_id']), user_id = data['user_id'], message = data['message'])
        ticket.save()
        return Response(request.data)


@permission_classes((permissions.AllowAny,))
class GetMessages(generics.ListAPIView):
        queryset = TicketMessage.objects.all()
        serializer_class = serializers.MessageSerializer

