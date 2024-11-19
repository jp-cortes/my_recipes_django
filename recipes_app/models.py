from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.TextField(max_length=100, verbose_name="category", null=False)
    images = models.ImageField(upload_to="logos", null=True, blank=True)

    #recipes
    def __str__(self):
        return self.title



class Recipe(models.Model):
    name =  models.TextField(max_length=200, verbose_name="name", null=False)
    images = models.ImageField(upload_to="logos", null=True, blank=True)
    ingredients = models.JSONField(null=False)
    preparation = models.TextField(max_length=900, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return self.name



class User(models.Model):
    name = models.TextField(max_length=100, null=False, verbose_name="name")
    lastname = models.TextField(max_length=100, null=False, verbose_name="lastname")
    email = models.TextField(max_length=100, null=False, verbose_name="email")
    password = models.TextField(max_length=100, null=False)

    role = models.TextField(max_length=100, null=False)

    def __str__(self):
        return self.name