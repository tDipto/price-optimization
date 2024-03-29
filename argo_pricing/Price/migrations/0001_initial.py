# Generated by Django 4.2.5 on 2023-10-03 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Product", "0003_alter_product_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Time",
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
                ("year", models.PositiveIntegerField()),
                ("month", models.PositiveSmallIntegerField()),
                ("day", models.PositiveSmallIntegerField()),
                ("hour", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Price",
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
                    "user_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "location_id_foreign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Product.location",
                    ),
                ),
                (
                    "product_id_foreign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Product.product",
                    ),
                ),
                (
                    "time_id_foreign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Price.time"
                    ),
                ),
                (
                    "user_id_foreign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
