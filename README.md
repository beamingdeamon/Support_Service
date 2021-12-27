Support service
===============
It's my project work by puthon django curse.

In this project I was developed the support service
____
Requests for backend
--------------------
In the files have a 'Ticket.postman_collection.json'

It's json by the postman for look every requests
___

POST Create Ticket
>localhost:8000/api/createticket/
>>when you creating ticket you must send only one value in the body. It's 'subject'

GET All Tickets
>http://localhost:8000/api/gettickets/

PUT Ticket
>http://localhost:8000/api/updateticket/1/
>>there you must enter id of the ticket in the url and send json file with 'subject'

DELETE Ticket
>http://localhost:8000/api/deleteticket/2/
>>to delete message you must only enter id in url

___

POST Create Message
>localhost:8000/api/createmessage/
>>when you creating message you must send some values in the vody. it's 'ticket_id', 'user_id' and 'message'

GET All Messages
>http://localhost:8000/api/getmessages/

GET Messages by Tickets id
>http://localhost:8000/api/getmessages/2/

GET Sorted Messages By Date
>http://localhost:8000/api/getmessagesbydate/

PUT Message
>http://localhost:8000/api/updatemessage/5/
>>there you must enter id of the message in the url and send json file with 'message'

DELETE Message
>http://localhost:8000/api/deletemessage/1/
>>to delete message you must only enter id in url
