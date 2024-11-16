from django.contrib import admin
from django.urls import path
from recipes_app.views import RecipesFormView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', RecipesFormView.as_view(), name="add_recipe")
]