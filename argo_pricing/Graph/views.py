from django.shortcuts import render
from Price.models import Price
from Price.serializers import PriceSerializer
from django.db.models import Avg, Max, Min
from Product.models import Location, Product
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response


class GetGraphAPI(ListCreateAPIView):
    serializer_class = PriceSerializer

    def get(
        self,
        request,
        product_id,
        location_id,
        Syear=None,
        Eyear=None,
        Smonth=None,
        Emonth=None,
        Sday=None,
        Eday=None,
    ):
        location = Location.objects.get(id=location_id)
        product = Product.objects.get(id=product_id)

        Syear = request.query_params.get("Syear")
        Eyear = request.query_params.get("Eyear")
        Smonth = request.query_params.get("Smonth")
        Emonth = request.query_params.get("Emonth")
        Sday = request.query_params.get("Sday")
        Eday = request.query_params.get("Eday")

        response_data = {
            "product": product.product_name,
            "location": location.district,
            "date_range_stats": {},
        }

        def generate_stats(queryset):
            price_stats = queryset.aggregate(
                avg_price=Avg("user_price"),
                max_price=Max("user_price"),
                min_price=Min("user_price"),
            )

            return {
                "max_price": price_stats["max_price"],
                "min_price": price_stats["min_price"],
                "avg_price": price_stats["avg_price"],
            }

        def process_date_range(queryset, date_range_key):
            if date_range_key not in response_data["date_range_stats"]:
                response_data["date_range_stats"][date_range_key] = generate_stats(
                    queryset
                )

        if not Eyear:
            if not Syear:
                if not Emonth:
                    # Smonth/day - Smonth/day
                    for m in range(int(Smonth), int(Smonth) + 1):
                        for d in range(int(Sday), int(Eday) + 1):
                            queryset = Price.objects.filter(
                                product_id_foreign=product_id,
                                location_id_foreign=location_id,
                                time_id_foreign__month=m,
                                time_id_foreign__day=d,
                            )

                            process_date_range(queryset, f"{m}-{d}")
                else:
                    # Smonth - Emonth
                    for m in range(int(Smonth), int(Emonth) + 1):
                        queryset = Price.objects.filter(
                            product_id_foreign=product_id,
                            location_id_foreign=location_id,
                            time_id_foreign__month=m,
                        )

                        process_date_range(queryset, f"{m}")
            else:
                # Syear/month - Syear/month
                for y in range(int(Syear), int(Syear) + 1):
                    for m in range(int(Smonth), int(Emonth) + 1):
                        queryset = Price.objects.filter(
                            product_id_foreign=product_id,
                            location_id_foreign=location_id,
                            time_id_foreign__year=y,
                            time_id_foreign__month=m,
                        )

                        process_date_range(queryset, f"{y}-{m}")
        else:
            for y in range(int(Syear), int(Eyear) + 1):
                queryset = Price.objects.filter(
                    product_id_foreign=product_id,
                    location_id_foreign=location_id,
                    time_id_foreign__year=y,
                )

                process_date_range(queryset, f"{y}")

        return Response(response_data)
