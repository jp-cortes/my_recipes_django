from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.TextField(max_length=100, verbose_name="category", null=False)

    #recipes



class Recipe(models.Model):
    name =  models.TextField(max_length=200, verbose_name="name", null=False)
    images = models.JSONField(null=True)
    images = models.JSONField(null=False)
    preparation = models.TextField(max_length=900, null=False)
    #category_id



class User(models.Model):
    name = models.TextField(max_length=100, null=False)
    email = models.TextField(max_length=100, null=False)
    password = models.TextField(max_length=100, null=False)

    role = models.TextField(max_length=100, null=False)