# Generated by Django 4.2.5 on 2023-10-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(
                default=None, max_length=250, null=True, upload_to="productImage/"
            ),
        ),
    ]
