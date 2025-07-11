from django.test import TestCase

import base64

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class TestAuthentication (TestCase):

    def test_basic_authentication(self):
        client = APIClient()
        user = User.objects.create_user(username='testuser', password='testpass')
        credential = base64.b64encode(b'testuser:testpass').decode('ascii')
        header_data = f"Basic {credential}"
        client.credentials(HTTP_AUTHORIZATION=header_data)
        response = client.get(reverse('company_model_viewset-list'))
        print(response, response.data, response.status_code)
        assert response.status_code == status.HTTP_200_OK
        print(response, response.data, response.status_code)


    def test_session_authentication(self):
        client = APIClient()
        user = User.objects.create_user(username='testuser2', password='testpass2')
        client.login(username='testuser2', password='testpass')
        response = client.get(reverse('em-list'))
        print(response, response.data, response.status_code)
        assert response.status_code == status.HTTP_200_OK
        print(response, response.data, response.status_code)

