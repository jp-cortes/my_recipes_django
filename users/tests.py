from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class LoginViewTest(TestCase):
# test for login view
    def test_should_return_200(self):
        url = reverse("login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_login_view_properties(self):
        url = reverse("login")
        response = self.client.get(url) 

        self.assertIn('view', response.context)

        view = response.context['view']

        self.assertEqual(view.template_name, "users/login.html")  


class LogoutViewTest(TestCase):
    #logout url shouldn't have access, should retun 405
    # should only visible when the user logout
    def test_should_return_405(self):
        url = reverse("logout")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)


class RegisterViewTest(TestCase):
#test for register view
    def test_should_return_200(self):
        url = reverse("register")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_register_view_properties(self):
        url = reverse("register")
        response = self.client.get(url) 

        self.assertIn('view', response.context)

        view = response.context['view']

        self.assertEqual(view.template_name, "users/register.html") 