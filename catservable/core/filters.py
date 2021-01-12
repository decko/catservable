from django_filters import rest_framework as filters

from .models import CatBreed


class ArrayFilter(filters.FilterSet):
    temperament = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CatBreed
        fields = ("origin", "temperament",)
