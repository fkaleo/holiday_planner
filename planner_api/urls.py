from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet, TripViewSet, TripStopViewSet

router = DefaultRouter()
router.register(r"destinations", DestinationViewSet)
router.register(r"trips", TripViewSet)
router.register(r"trip-stops", TripStopViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
