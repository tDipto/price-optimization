from django.urls import path
from . import views

urlpatterns = [
    path("price/", views.PriceUpdateAPI.as_view(), name="PriceUpdateAPI"),
    path(
        "price/<int:product_id>/<int:location_id>/",
        views.GetSingleProductPriceAPI.as_view(),
        name="GetSingleProductPriceAPI",
    ),
    path(
        "price/<int:location_id>/",
        views.GetAllProductPriceAPI.as_view(),
        name="GetAllProductPriceAPI",
    ),
]
