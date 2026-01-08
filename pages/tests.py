from django.test import TestCase,SimpleTestCase
from django.urls import reverse

class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get(reverse("home"))
        # response.status_code==200
        self.assertEqual(response.status_code,200)
    
    def test_template_correct_name(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"pages/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response,"<h1>Home</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)