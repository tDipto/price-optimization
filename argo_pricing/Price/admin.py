from django.contrib import admin
from .models import Price,Time


class ShowPrice(admin.ModelAdmin):
    list_display = [
        "product_id_foreign",
        "user_price",
        "location_id_foreign",
        "time_id_foreign",
    ]
    class Meta:
        model = Price

class ShowTime(admin.ModelAdmin):
    list_display = [
        "year" ,
        "month",
        "day" ,
        "hour"
    ]
    class Meta:
        model = Time


admin.site.register(Price, ShowPrice)
admin.site.register(Time,ShowTime)
