from django.test import TestCase
from django.urls import reverse

from .models import Recipe, Category


class RecipeListViewTest(TestCase):
    # test for route all recipes
    def test_should_return_200(self):
        url = reverse("all_recipes")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["recipes"].count(), 0)

    def test_should_return_200_with_recipes(self):
        url = reverse("all_recipes")
        category_instace = Category.objects.create(
            title="test category",
            images="test category image",
            created_on="test category date",
        )
        Recipe.objects.create(
            name="test",
            images="test-image",
            ingredients="test ingredients",
            preparation="test preparation",
            category=category_instace,
            created_on="test date",
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["recipes"].count(), 1)
