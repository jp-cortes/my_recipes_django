# Generated by Django 5.1.3 on 2024-11-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(max_length=100, verbose_name="category")),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=200, verbose_name="name")),
                ("images", models.ImageField(blank=True, null=True, upload_to="logos")),
                ("ingredients", models.JSONField()),
                ("preparation", models.TextField(max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=100, verbose_name="name")),
                ("lastname", models.TextField(max_length=100, verbose_name="lastname")),
                ("email", models.TextField(max_length=100, verbose_name="email")),
                ("password", models.TextField(max_length=100)),
                ("role", models.TextField(max_length=100)),
            ],
        ),
    ]
