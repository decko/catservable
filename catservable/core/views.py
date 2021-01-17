from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

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


@api_view(http_method_names=['GET'])
def cat_breed_search_by_temper(request, *args, **kwargs):
    temperament = kwargs.get("temper")
    queryset = CatBreed.objects.filter(temperament__icontains=temperament)

    breeds = CatBreedModelSerializer(queryset, many=True)
    return Response(breeds.data)
