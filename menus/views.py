from django.views.generic import DateDetailView
from .models import Menu

class MyMenuView(DateDetailView):
    model =  Menu
    template_name = "menus/my_menu.html"
    context_object_name = "menu"

    def get_object(self, queryset = None):
        return Menu.objects.filter(is_active=True).first()