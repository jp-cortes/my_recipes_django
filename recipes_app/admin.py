from django.contrib import admin
from .models import Recipe, Category, User


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ["name", "ingredients", "category", "created_on"]
    search_fields = ["name", "ingredients"]


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["title", "created_on"]
    search_fields = ["title"]


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["name", "lastname", "email", "created_on"]
    search_fields = ["name", "lastname", "email"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(User, UserAdmin)
