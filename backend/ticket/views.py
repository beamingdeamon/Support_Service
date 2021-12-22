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
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
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
class DeleteTicket(APIView):
        def delete(self, request, pk):
                ticket = Ticket.objects.get(pk=pk)
                ticket.delete()
                return Response('Delete succesfull')

           
@permission_classes((permissions.AllowAny,))     
class UpdateTicket(APIView):
        def put(self, request,pk):
                ticket = Ticket.objects.get(pk=pk)
                serializer = serializers.TicketSerializer(ticket, data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                
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

@permission_classes((permissions.AllowAny,))
class GetMessagebyId(APIView):
        def get(self, request, ticketid):   
                queryset = TicketMessage.objects.filter(ticket_id = ticketid)
                serializer = serializers.MessageSerializer(queryset, many = True)
                return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class DeleteMessage(APIView):
        def delete(self, request, pk):
                ticket_message = TicketMessage.objects.get(pk=pk)
                ticket_message.delete()
                return Response('Delete succesfull')

@permission_classes((permissions.AllowAny,))     
class UpdateMessage(APIView):
        def put(self, request,pk):
                ticket_message = TicketMessage.objects.get(pk=pk)
                serializer = serializers.MessageSerializer(ticket_message, data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)