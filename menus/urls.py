from django.urls import path

from .views import MyMenuView

urlpatterns = [
    path('my-menu', MyMenuView.as_view(), name="my_menu")    
]
