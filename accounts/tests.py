from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser


class SignupTestPage(TestCase):

    def test_page_exist(self):
        response = self.client.get("/accounts/signup")
        self.assertEqual(response.status_code,200)
    
    def test_template_and_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(reverse("signup"),data={
            "username":"mohammad",
            "age":20,
            "email":"abc@abc.com",
            "password1":"Zaq11qaZ",
            "password2":"Zaq11qaZ"
        })

        self.assertEqual(response.status_code,302)
        self.assertEqual(get_user_model().objects.count(),1)
        user = get_user_model().objects.first()
        self.assertEqual(user.username,"mohammad")
        self.assertEqual(user.email,"abc@abc.com")