from django.urls import path
from . import views

urlpatterns = [
    path(
        "getGraph/<int:product_id>/<int:location_id>/",
        views.GetGraphAPI.as_view(),
        name="GetGraphAPI",
    ),
]
