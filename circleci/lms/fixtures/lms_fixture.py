from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from faker import Faker


class AuthorFixture():

    def generate_data(self):
        
        fake = Faker()
        return {
            'name': fake.first_name()
            }
