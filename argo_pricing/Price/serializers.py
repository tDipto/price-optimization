from rest_framework import serializers
from .models import Price


class PriceSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = [
            "user_price",
            "user_id_foreign",
            "product_id_foreign",
            "location_id_foreign",
            "time_id_foreign"
        ]


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = [
            "user_price",
            "user_id_foreign",
            "product_id_foreign",
            "location_id_foreign",
            "time_id_foreign",
        ]
