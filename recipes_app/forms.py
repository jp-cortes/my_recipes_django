from django import forms 
from .models import Recipe

class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100, label="name")
    images = forms.ImageField(label="images", required=False)
    ingredients = forms.CharField(label="ingredients")
    preparation = forms.CharField(max_length=900, label="preparation")


    def save(self):
        Recipe.objects.create(
            name=self.cleaned_data['name'],
            images=self.cleaned_data['images'],
            ingredients=self.cleaned_data['ingredients'],
            preparation=self.cleaned_data['preparation'],
        )