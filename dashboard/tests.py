from django.test import TestCase
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.test import client, TestCase
import json


# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'root',
            'password': '123456'}
        User.objects.create_user(**self.credentials)

    def test_check_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    def test_bus_stations(self):
        # login first
        response = self.client.post('/login/', self.credentials, follow=True)
        response = self.client.get('/api/bus_stations/')
        # print(response.content)
        if response.status_code == 200:
            self.assertTrue(isinstance(json.loads(response.content), list))

    def test_bike_realtime(self):
        # login first
        response = self.client.post('/login/', self.credentials, follow=True)
        response = self.client.get('/api/bike_realtime/')
        if response.status_code == 200:
            self.assertTrue(isinstance(json.loads(response.content), list))

    def test_bus_realtime(self):
        # login first
        response = self.client.post('/login/', self.credentials, follow=True)
        response = self.client.get('/api/bus_realtime/')
        if response.status_code == 200:
            self.assertTrue(isinstance(json.loads(response.content), dict))
