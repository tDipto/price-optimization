# Generated by Django 4.2.5 on 2023-10-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Product", "0003_alter_product_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
