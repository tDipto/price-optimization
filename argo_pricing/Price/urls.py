from django.urls import path
from . import views

urlpatterns = [
    path("priceupdate/", views.PriceUpdateAPI.as_view(), name="PriceUpdateAPI"),
    path(
        "getsingleproductprice/<int:product_id>/<int:location_id>/",
        views.GetSingleProductPriceAPI.as_view(),
        name="GetSingleProductPriceAPI",
    ),
    path(
        "getallproductprice/<int:location_id>/",
        views.GetAllProductPriceAPI.as_view(),
        name="GetAllProductPriceAPI",
    ),
]
