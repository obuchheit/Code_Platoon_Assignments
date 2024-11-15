# Generated by Django 5.1.3 on 2024-11-14 16:06

import intro_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro_app', '0002_alter_pokemon_description_alter_pokemon_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=200, validators=[intro_app.validators.validate_pokemon_name]),
        ),
    ]
