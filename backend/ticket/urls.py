from django.urls import path
from .views import CreateMessage
from .views import GetMessages
from .views import CreateTicket
from .views import UpdateTicket
from .views import DeleteTicket
from .views import GetTickets
from .views import GetMessagebyId
from .views import UpdateMessage
from .views import DeleteMessage
app_name = "Ticket"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('createticket/', CreateTicket.as_view()),
    path('gettickets/', GetTickets.as_view()),
    path('updateticket/<int:pk>/', UpdateTicket.as_view()),
    path('deleteticket/<int:pk>/', DeleteTicket.as_view()),
    path('createmessage/', CreateMessage.as_view()),
    path('getmessages/', GetMessages.as_view()),
    path('getmessages/<int:ticketid>/', GetMessagebyId.as_view()),
    path('updatemessage/<int:pk>/', UpdateMessage.as_view()),
    path('deletemessage/<int:pk>/', DeleteMessage.as_view()),
]