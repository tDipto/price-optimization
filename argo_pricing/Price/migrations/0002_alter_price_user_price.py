# Generated by Django 4.2.5 on 2023-10-04 09:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Price", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="user_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
