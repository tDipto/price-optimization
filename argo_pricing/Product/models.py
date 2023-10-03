from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    quantity = models.IntegerField(default=0)
    product_image = models.ImageField(
        upload_to="productImage/", max_length=250, null=True, default=None
    )

    def __str__(self):
        return self.product_name


class Location(models.Model):
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=200)

    def __str__(self):
        return f"district: {self.district}, thana: {self.thana}"
