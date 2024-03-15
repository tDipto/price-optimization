from .serializers import ProductSerializer, LocationSerializer
from django.http import HttpResponse
from .models import Product, Location
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


def index(request):
    return HttpResponse("Hello, world. You're at the Product and Location.")


class ProductAPI(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPI(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class LocationAPI(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = "id"
