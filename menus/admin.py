from django.contrib import admin

from .models import Menu, MenuRecipe


class MenuRecipeInlineAdmin(admin.TabularInline):
    model = MenuRecipe
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    inlines = [MenuRecipeInlineAdmin]


admin.site.register(Menu, MenuAdmin)
