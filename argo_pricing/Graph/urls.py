from django.urls import path
from . import views

urlpatterns = [
    path(
        "graph/<int:product_id>/<int:location_id>/",
        views.GetGraphAPI.as_view(),
        name="GetGraphAPI",
    ),
]
