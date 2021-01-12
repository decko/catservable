from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import CatBreed
from .serializers import CatBreedModelSerializer


class CatBreedAPIView(ListAPIView, RetrieveAPIView):
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedModelSerializer

