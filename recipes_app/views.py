from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import generic
from .forms import RecipeForm

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


class RecipesFormView(generic.FormView):
    template_name="recipes_app/add_recipe.html"
    form_class=RecipeForm
    success_url=reverse_lazy("add_recipe")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
