from django.contrib import admin
from django.urls import path
from recipes_app.views import RecipesFormView, RecipesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', RecipesFormView.as_view(), name="add_recipe"),
    path('all/', RecipesView.as_view(), name="all_recipes")
]