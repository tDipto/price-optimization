from django.db.models import Avg, Max, Min
from .serializers import PriceSerializer, PriceSerializer2
from .models import Product, Location, Price, Time
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
import datetime
from rest_framework.response import Response


class PriceUpdateAPI(ListCreateAPIView):
    queryset = Price.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PriceSerializer2
        return PriceSerializer

    def perform_create(self, serializer):
        current_datetime = datetime.datetime.now()

        year = current_datetime.year
        month = current_datetime.month
        day = current_datetime.day
        hour = current_datetime.hour

        try:
            current_time = Time.objects.get(year=year, month=month, day=day, hour=hour)
        except Time.DoesNotExist:
            current_time = Time.objects.create(
                year=year, month=month, day=day, hour=hour
            )

        serializer.save(time_id_foreign=current_time)


class GetSingleProductPriceAPI(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PriceSerializer

    def get(self, request, product_id, location_id):
        location = Location.objects.get(id=location_id)
        product = Product.objects.get(id=product_id)

        year = request.query_params.get("year")
        month = request.query_params.get("month")
        day = request.query_params.get("day")

        if not (year or month or day):
            current_date = datetime.datetime.now()
            year = current_date.year
            month = current_date.month
            day = current_date.day

        queryset = Price.objects.filter(
            product_id_foreign=product_id, location_id_foreign=location_id
        )

        if year:
            queryset = queryset.filter(time_id_foreign__year=year)
        if year and month:
            queryset = queryset.filter(time_id_foreign__month=month)
        if year and month and day:
            queryset = queryset.filter(time_id_foreign__day=day)

        price_stats = queryset.aggregate(
            avg_price=Avg("user_price"),
            max_price=Max("user_price"),
            min_price=Min("user_price"),
        )

        response_data = {
            "place_name": location.district,
            "product_name": product.product_name,
            "average_price": price_stats["avg_price"],
            "max_price": price_stats["max_price"],
            "min_price": price_stats["min_price"],
            "year": int(year) if year else None,
            "month": int(month) if month else None,
            "day": int(day) if day else None,
        }

        return Response(response_data)


class GetAllProductPriceAPI(ListCreateAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        pass

    def get(self, request, location_id):
       
        location = Location.objects.get(id=location_id)
        products = Product.objects.all()

        year = request.query_params.get("year")
        month = request.query_params.get("month")
        day = request.query_params.get("day")

        if not (year or month or day):
            current_date = datetime.datetime.now()
            year = current_date.year
            month = current_date.month
            day = current_date.day

        queryset = Price.objects.filter(location_id_foreign=location_id)

        if year:
            queryset = queryset.filter(time_id_foreign__year=year)
        if month:
            queryset = queryset.filter(time_id_foreign__month=month)
        if day:
            queryset = queryset.filter(time_id_foreign__day=day)

        response_data = {
            "location": location.district,
            "year": int(year) if year else None,
            "month": int(month) if month else None,
            "day": int(day) if day else None,
            "products": [],
        }

        for product in products:
            product_queryset = queryset.filter(product_id_foreign=product.id)

            price_stats = product_queryset.aggregate(
                avg_price=Avg("user_price"),
                max_price=Max("user_price"),
                min_price=Min("user_price"),
            )

            product_data = {
                "product_name": product.product_name,
                "average_price": price_stats["avg_price"],
                "max_price": price_stats["max_price"],
                "min_price": price_stats["min_price"],
            }

            response_data["products"].append(product_data)

        return Response(response_data)
