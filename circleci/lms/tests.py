from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from lms.fixtures.lms_fixture import AuthorFixture

from faker import Faker


class AuthorTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        self.author_fixture = AuthorFixture()
        
    def test_create_author(self):
        
        data = self.author_fixture.generate_data()

        response = self.client.post(
            reverse('author-list'),
            data,
            format="json")
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_multiple_author(self):
        
        total_authors = 4

        data = self.author_fixture.generate_data()
        
        response = []
        
        for count in range(0,total_authors):
            author = self.client.post(
                reverse('author-list'),
                data,
                format="json")

            response.append(author.data['id'])
        
        return response
