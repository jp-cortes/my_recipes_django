from django.views.generic import DateDetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Menu

class MyMenuView(LoginRequiredMixin, DateDetailView):
    model =  Menu
    template_name = "menus/my_menu.html"
    context_object_name = "menu"

    def get_object(self, queryset = None):
        return Menu.objects.filter(is_active=True, user=self.request.user).first()