from rest_framework import serializers

from .fields import StringArrayField
from .models import CatBreed, CatImage


class CatImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = "__all__"


class CatBreedModelSerializer(serializers.ModelSerializer):
    temperament = StringArrayField()

    class Meta:
        model = CatBreed
        fields = "__all__"
