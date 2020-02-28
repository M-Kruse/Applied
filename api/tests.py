from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from jobs.models import Job

class JobTests(APITestCase):
    def test_create_job(self):
        """
        Ensure we can create a new account object.
        """
        test_source_site = "indeed"
        test_title = "Fooperator"
        test_company = "Bar Corp"
        test_location = "Barsville"
        test_post_date = "2 days ago"
        test_description = "Come join us as a Fooperator at Bar Corp where you will help make Foo resilient, performant and highly available to the world."
        test_apply_url = "https://example.com/apply"
        url = reverse('jobs')
        data = {
	        "source_site":test_source_site,
	        "title":test_title,
	        "company":test_company,
	        "location":test_location,
	        "date_posted":test_post_date,
	        "url":test_apply_url,
	        "description":{"text":test_description}
	    }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 1)
        self.assertEqual(Job.objects.get().source_site, test_source_site)
        self.assertEqual(Job.objects.get().title, test_title)
        self.assertEqual(Job.objects.get().company, test_company)
        self.assertEqual(Job.objects.get().location, test_location)
        self.assertEqual(Job.objects.get().date_posted, test_post_date)
        self.assertEqual(Job.objects.get().url, test_apply_url)
        self.assertEqual(Job.objects.get().description.text, test_description)