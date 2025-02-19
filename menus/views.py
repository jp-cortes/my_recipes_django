from django.views.generic import DateDetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Menu, MenuRecipe
from .forms import MenuRecipesForm


class MyMenuView(LoginRequiredMixin, DateDetailView):
    model = Menu
    template_name = "menus/my_menu.html"
    context_object_name = "menu"

    def get_object(self, queryset=None):
        return Menu.objects.filter(is_active=True, user=self.request.user).first()

    # def delete_recipe(self,request, recipe_id):
    #     recipe = Menu.objects.get(pk=recipe_id)
    #     # Menu.objects.exclude(self, recipe)
    #     recipe.delete()
    #     return redirect('my_menu')


class CreateMenuRecipeView(LoginRequiredMixin, CreateView):
    template_name = "menus/create_menu_recipes.html"
    form_class = MenuRecipesForm
    success_url = reverse_lazy("my_menu")

    def form_valid(self, form):
        menu, _ = Menu.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        form.instance.menu = menu
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
