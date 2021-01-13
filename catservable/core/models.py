from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class CatBreed(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(_("Breed Name"), max_length=40, default="")
    origin = models.CharField(_("Breed Origin"), max_length=60)
    temperament = ArrayField(models.CharField(_("Temperament"), max_length=50), blank=True, default=list)
    description = models.TextField(_("Description"))

    def __str__(self):
        return f"{self.name} - origin: {self.origin}"
