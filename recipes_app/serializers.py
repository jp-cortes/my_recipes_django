from rest_framework.serializers import ModelSerializer
from .models import Recipe


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "images",
            "ingredients",
            "preparation",
            "category",
            "created_on",
        ]
