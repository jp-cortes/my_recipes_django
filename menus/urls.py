from django.urls import path

from .views import MyMenuView, CreateMenuRecipeView

urlpatterns = [
    path("my-menu", MyMenuView.as_view(), name="my_menu"),
    path("create-menu", CreateMenuRecipeView.as_view(), name="create_menu"),
]
