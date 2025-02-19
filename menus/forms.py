from django.forms import ModelForm
from .models import MenuRecipe


class MenuRecipesForm(ModelForm):
    class Meta:
        model = MenuRecipe
        fields = ["recipe"]
