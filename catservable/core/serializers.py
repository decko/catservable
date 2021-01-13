from rest_framework import serializers

from .fields import StringArrayField
from .models import CatBreed


class CatBreedModelSerializer(serializers.ModelSerializer):
    temperament = StringArrayField()

    class Meta:
        model = CatBreed
        fields = "__all__"
