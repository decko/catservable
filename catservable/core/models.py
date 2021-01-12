from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class CatBreed(models.Model):
    origin = models.CharField(_("Breed Origin"), max_length=60)
    temperament = ArrayField(models.CharField(_("Temperament"), max_length=50), blank=True, default=list())
    description = models.TextField(_("Description"))
