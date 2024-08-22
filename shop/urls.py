from django.urls import path, include
from rest_framework import routers

from .views import (
    EmbroideryViewSet,
    BookViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("embroideries", EmbroideryViewSet)
router.register("books", BookViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "shop"
