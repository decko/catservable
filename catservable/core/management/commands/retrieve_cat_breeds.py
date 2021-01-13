from django.core.management.base import BaseCommand

from catservable.core.resources import CatAPI

from catservable.core.serializers import CatBreedModelSerializer


class Command(BaseCommand):
    help = "Retrieve all cat breeds from TheCatAPI."

    def handle(self, *args, **kwargs):
        api = CatAPI()
        breeds_payload = api.breeds().get()
        breeds = breeds_payload().data

        breeds_instances = CatBreedModelSerializer(data=breeds, many=True)
        if breeds_instances.is_valid():
            breeds_instances.save()
