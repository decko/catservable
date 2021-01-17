import logging
from django.apps import apps
from django.core.management.base import BaseCommand

from rest_framework.exceptions import ValidationError

from tapioca.exceptions import ClientError, ServerError

from catservable.core.resources import CatAPI
from catservable.core.serializers import CatImageModelSerializer

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Retrieve 3 images for each cat breed from TheCatAPI."
    requires_migrations_checks = True

    def handle(self, *args, **kwargs):
        NUMBER_OF_IMAGES = 3
        api = CatAPI()
        CatBreed = apps.get_model("core", "CatBreed")

        breeds = CatBreed.objects.all()

        logger.info(f"Retrieving images for {CatBreed.objects.count()} cat breeds...")
        self.stdout.write(f"Retrieving images for {CatBreed.objects.count()} cat breeds...")

        for breed in breeds:
            for _ in range(NUMBER_OF_IMAGES):
                try:
                    request = api.images().get(params={"breed_id": breed.id})
                    payload = request().data[0]
                    image = CatImageModelSerializer(data=payload)
                    image.is_valid(raise_exception=True)
                    image.save(breed=breed)
                    logger.info(f"Retrievied image {_} of {NUMBER_OF_IMAGES} for {breed.id} breed")
                except (ClientError, ServerError, ValidationError) as exp:
                    logger.error(f"Failed retrieving image {_} of {NUMBER_OF_IMAGES} for {breed.id} breed. error={exp}")
                    self.stderr.write(self.style.ERROR("Failed retrieving image..."))
            self.stdout.write(self.style.SUCCESS(f"Retrieved images for {breed.id} breed"))
