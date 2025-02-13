from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import RecipeForm
from .models import Recipe, Category
from .serializers import RecipeSerializer

# Create your views here.
class HomeView(TemplateView):
    template_name = "recipes_app/home.html"

    # def get_context_data(self):
    #     categories = [
    #         {"title":"Vegetarian"},
    #         {"title":"Vegan"},
    #         {"title":"Seafood"},
    #         {"title":"Keto"},
    #         {"title":"Low calories"},
    #         {"title":"High calories"},
    #                ]
    #     # categories = Category.objects.all()
    #     context = {
    #         "categories": categories
    #     }
    #     return context
    

class RecipesView(TemplateView):
    template_name = "recipes_app/all_recipes.html"

    def get_context_data(self):
        recipes_example = [
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
        recipes = Recipe.objects.all()
        context = {
            "recipes": recipes
        }
        return context


class RecipesFormView(generic.FormView):
    template_name="recipes_app/add_recipe.html"
    form_class=RecipeForm
    success_url=reverse_lazy("all_recipes")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class RecipeListApi(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer =  RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def get_recipe(self, request, pk=None, format=None):
        pk = id
        recipe = Recipe.objects.get(id=id)
        serializer =  RecipeSerializer(recipe)
        return Response(serializer.data)