from django.test import TestCase
from django.template.defaultfilters import slugify
import json
from django.test import Client

class ViewsTestCase(TestCase):
    def test_get_messages(self):
        response = self.client.get('http://localhost:8000/api/getmessages/')
        self.assertEqual(response.status_code, 200)

    def test_get_tickets(self):
        response = self.client.get('http://localhost:8000/api/gettickets/')
        self.assertEqual(response.status_code, 200)


    def test_get_messages_by_date(self):
        response = self.client.get('http://localhost:8000/api/getmessagesbydate/')
        self.assertEqual(response.status_code, 200)

    def test_get_messages_by_id(self):
        response4 = self.client.get('http://localhost:8000/api/getmessages/5/')
        self.assertEqual(response4.status_code, 200)

    def test_create_ticket(self):
        response = self.client.post('http://localhost:8000/api/createticket/', json.loads('{"subject": "value1"}'), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_create_message(self):
        response = self.client.post('http://localhost:8000/api/createmessage/', json.loads('{"ticket_id": "4", "user_id" : "1", "message":"sdada"}'), content_type="application/json")
        self.assertEqual(response.status_code, 200)
