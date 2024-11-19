# Generated by Django 5.1.3 on 2024-11-19 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='logos'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes_app.category'),
        ),
    ]
