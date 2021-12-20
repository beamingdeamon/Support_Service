from django.urls import path
from .views import CreateMessage
from .views import GetMessages
from .views import CreateTicket
from .views import GetTickets
app_name = "Ticket"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('createticket/', CreateTicket.as_view()),
    path('gettickets/', GetTickets.as_view()),
    path('createmessage/', CreateMessage.as_view()),
    path('getmessages/', GetMessages.as_view())
]