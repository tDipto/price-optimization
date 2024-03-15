from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("location/", views.LocationAPI.as_view(), name="LocationAPI"),
    path(
        "location/<int:id>/",
        views.LocationDetailAPI.as_view(),
        name="LocationDetailAPI",
    ),
    path("product/", views.ProductAPI.as_view(), name="ProductAPI"),
    path(
        "product/<int:id>/", views.ProductDetailAPI.as_view(), name="ProductDetailAPI"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
