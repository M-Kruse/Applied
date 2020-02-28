#from django.urls import reverse
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from jobs.models import Job

class JobTests(APITestCase):
    def setUp(self):
        # Include an appropriate `Authorization:` header on all requests.
        self.user = User(email="rusty@rustyshack.null")
        password = 'foopy'
        self.user.set_password(password)
        self.user.save()
        Token.objects.create(user=self.user)
        token = Token.objects.get(user__username=self.user.username)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.client.force_login(user=self.user)

    def test_create_job(self):
        test_source_site = "indeed"
        test_title = "Fooperator"
        test_company = "Bar Corp"
        test_location = "Barsville"
        test_post_date = "2 days ago"
        test_description = "Come join us as a Fooperator at Bar Corp where you will help make Foo resilient, performant and highly available to the world."
        test_apply_url = "https://example.com/apply"
        data = {
            "job_site":test_source_site,
            "title":test_title,
            "company":test_company,
            "location":test_location,
            "date_posted":test_post_date,
            "url":test_apply_url,
            "description":{"text":test_description}
        }
        

        # Authenticate client with user
        response = self.client.post('http://127.0.0.1:8000/api/jobs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 1)
        self.assertEqual(Job.objects.get().job_site, test_source_site)
        self.assertEqual(Job.objects.get().title, test_title)
        self.assertEqual(Job.objects.get().company, test_company)
        self.assertEqual(Job.objects.get().location, test_location)
        self.assertEqual(Job.objects.get().date_posted, test_post_date)
        self.assertEqual(Job.objects.get().url, test_apply_url)
        self.assertEqual(Job.objects.get().description.text, test_description)