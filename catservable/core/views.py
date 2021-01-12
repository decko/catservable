from rest_framework.generics import ListAPIView, RetrieveAPIView

from .filters import ArrayFilter
from .models import CatBreed
from .serializers import CatBreedModelSerializer


class CatBreedListAPIView(ListAPIView):
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedModelSerializer
    filterset_class = ArrayFilter


class CatBreedRetrieveAPIView(RetrieveAPIView):
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedModelSerializer
