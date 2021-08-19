from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from shipwell.users.api.views import UserViewSet
from geo.api.views import AustinHexList, TrafficIncidentList, StateList, WeatherAPIList

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register("hexes", AustinHexList)
router.register("trafficincidents", TrafficIncidentList)
router.register("states", StateList)
router.register("weather", WeatherAPIList)

app_name = "api"
urlpatterns = router.urls

