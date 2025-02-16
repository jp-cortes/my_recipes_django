from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class MenuRecipeTest(TestCase):
# test for my my_menu route
    def test_no_logged_user_should_redirect(self):
        url = reverse("my_menu")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,"/users/login/?next=/menus/my-menu")

    def test_logged_user_should_redirect(self):
        url = reverse("my_menu")
        user = get_user_model().objects.create(username="Test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
