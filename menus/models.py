from django.db import models

from django.contrib.auth.models import User

from recipes_app.models import Recipe


class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.user}"


class MenuRecipe(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.menu} - {self.recipe}"
