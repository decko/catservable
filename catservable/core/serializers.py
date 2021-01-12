from rest_framework.serializers import ModelSerializer

from .models import CatBreed


class CatBreedModelSerializer(ModelSerializer):
    class Meta:
        model = CatBreed
        fields = "__all__"
