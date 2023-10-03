from django.contrib import admin
from .models import Product, Location


class ShowProduct(admin.ModelAdmin):
    list_display = ["product_name"]


class ShowDistrict(admin.ModelAdmin):
    list_display = ["district", "thana"]


admin.site.register(Product, ShowProduct)
admin.site.register(Location, ShowDistrict)
