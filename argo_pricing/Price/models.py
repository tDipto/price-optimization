from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from Product.models import Location, Product


class Time(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    hour = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"year: {self.year}, month: {self.month}, day: {self.day}, hour: {self.hour}"


class Price(models.Model):
    user_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    user_id_foreign = models.ForeignKey(User, on_delete=models.CASCADE)
    time_id_foreign = models.ForeignKey(Time, on_delete=models.CASCADE)
    product_id_foreign = models.ForeignKey(Product, on_delete=models.CASCADE)
    location_id_foreign = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product: {self.product_id_foreign},Price: {self.user_price}, Location: {self.location_id_foreign}, Time: {self.time_id_foreign}"
