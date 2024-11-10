from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RecipesView(TemplateView):
    template_name = "recipes_app/base.html"

    def get_context_data(self):
        recipes = [
            {"title":"Bulgarian salad",
             "ingredients": ["tomato","fresh cheese", "cucumber", "peppers"],
             "preparation":"lorem ipsum"},
             {"title":"Tarator",
             "ingredients": ["plane yogurt","fresh garlic", "cucumber", "walnuts", "dill"],
             "preparation":"lorem ipsum"},
             {"title":"Banitza",
             "ingredients": ["Filo dough","fresh eggs", "fresh cheese", "butter"],
             "preparation":"lorem ipsum"}
                   ]
        context = {
            "recipes": recipes
        }
        return context

