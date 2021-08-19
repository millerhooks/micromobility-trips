from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mapbox_location_field.spatial.models import SpatialLocationField  
from geo.models import WeatherAPI
from django.db import models


class User(AbstractUser):
    """Default user for shipwell."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    location = SpatialLocationField(blank=True, null=True)
    weather_service = models.ForeignKey(
        WeatherAPI, 
        on_delete=models.CASCADE, 
        blank=True, null=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
