from django.contrib import admin
from .models import Recipe, Category, User

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ["name", "ingredients", "category"]
    search_fields = ["name", "ingredients", "category"]

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["title"]
    search_fields = ["title"]

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["name", "lastname", "email"]
    search_fields = ["name", "lastname", "email"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(User, UserAdmin)
