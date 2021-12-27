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

### Requests for Ticket

POST Create Ticket
>http://localhost:8000/api/createticket/
>>when you creating ticket you must send only one value in the body. It's 'subject'

Response: 
```json
{
    "subject": "test"
}
```

GET All Tickets
>http://localhost:8000/api/gettickets/

Response: 
```json
{
    "id": 1,
    "subject": "dsadsdasdasdada",
    "date": "2021-12-22"
}
```

PUT Ticket
>http://localhost:8000/api/updateticket/{id}/
>>there you must enter id of the ticket in the url and send json file with 'subject'

Response: 
```json
{
    "id": 1,
    "subject": "dsadsdasdasdada",
    "date": "2021-12-22"
}
```

DELETE Ticket
>http://localhost:8000/api/deleteticket/{id}/
>>to delete message you must only enter id in url

Response: 
```json
"Delete succesfull"
```

___

### Requests for Message

POST Create Message
>http://localhost:8000/api/createmessage/
>>when you creating message you must send some values in the vody. it's 'ticket_id', 'user_id' and 'message'

Response: 
```json
{
    "ticket_id": "4",
    "user_id": "1",
    "message": "21wqeqdsa3123qweq"
}
```

GET All Messages
>http://localhost:8000/api/getmessages/

Response: 
```json
{
    "id": 10,
    "ticket_id": 3,
    "user_id": 1,
    "message": "Sa2131231lam",
    "created_date": "2021-12-23",
    "updated_date": "2021-12-23"
}
```


GET Messages by Tickets id
>http://localhost:8000/api/getmessages/{id}/

Response: 
```json
{
    {
        "id": 10,
        "ticket_id": 3,
        "user_id": 1,
        "message": "Sa2131231lam",
        "created_date": "2021-12-23",
        "updated_date": "2021-12-23"
    },
    {
        "id": 11,
        "ticket_id": 3,
        "user_id": 1,
        "message": "42131",
        "created_date": "2021-12-23",
        "updated_date": "2021-12-23"
    }
}
```

GET Sorted Messages By Date
>http://localhost:8000/api/getmessagesbydate/

Response: 
```json
{
    {
        "id": 10,
        "ticket_id": 3,
        "user_id": 1,
        "message": "Sa2131231lam",
        "created_date": "2021-12-23",
        "updated_date": "2021-12-23"
    },
    {
        "id": 12,
        "ticket_id": 3,
        "user_id": 1,
        "message": "Sa2131231lam",
        "created_date": "2021-12-27",
        "updated_date": "2021-12-27"
    }
}
```

PUT Message
>http://localhost:8000/api/updatemessage/{id}/
>>there you must enter id of the message in the url and send json file with 'message'

Response: 
```json
{
    "id": 10,
    "ticket_id": 3,
    "user_id": 1,
    "message": "dsadsadada",
    "created_date": "2021-12-27",
    "updated_date": "2021-12-27"
}
```

DELETE Message
>http://localhost:8000/api/deletemessage/{id}/
>>to delete message you must only enter id in url

Response: 
```json
"Delete succesfull"
```
