from django import forms 
from .models import Recipe

class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100, label="name", widget=forms.TextInput(attrs={"placeholder" : "Pizza Margarita"}))
    images = forms.ImageField(label="images", required=False)
    ingredients = forms.CharField(label="ingredients", widget=forms.TextInput(attrs={"placeholder" : "100gr white cheese, 2 eggs, ..."}))
    preparation = forms.CharField(label="preparation", widget=forms.Textarea(attrs={"placeholder" : "Mix all ingredients..."}))


    def save(self):
        Recipe.objects.create(
            name=self.cleaned_data['name'],
            images=self.cleaned_data['images'],
            ingredients=self.cleaned_data['ingredients'],
            preparation=self.cleaned_data['preparation'],
        )