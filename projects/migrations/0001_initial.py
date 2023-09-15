# Generated by Django 4.2.3 on 2023-09-15 15:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                limit_value=50
                            )
                        ],
                    ),
                ),
                (
                    "github",
                    models.URLField(
                        validators=[django.core.validators.URLValidator()]
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(
                        validators=[django.core.validators.URLValidator()]
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                limit_value=500
                            )
                        ]
                    ),
                ),
            ],
        ),
    ]
