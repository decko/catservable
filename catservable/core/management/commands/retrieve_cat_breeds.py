import logging
import time

from django.core.management.base import BaseCommand

from catservable.core.resources import CatAPI
from catservable.core.serializers import CatBreedModelSerializer

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Retrieve all cat breeds from TheCatAPI."

    def handle(self, *args, **kwargs):
        api = CatAPI()

        logger.info("Retrieving cat breeds")
        self.stdout.write("Retrieving cat breeds")
        t1 = time.time()
        breeds_payload = api.breeds().get()
        elapsed = time.time() - t1
        logger.info(f"Finished cat breeds retrieval in {elapsed}")
        self.stdout.write(self.style.SUCCESS(f"Finished cat breeds retrieval in {elapsed:.2f}"))
        breeds = breeds_payload().data

        logger.debug(f"Serializing cat breeds")
        self.stdout.write("Serializing cat breeds...")
        breeds_instances = CatBreedModelSerializer(data=breeds, many=True)
        if breeds_instances.is_valid():
            number_of_breeds = len(breeds_instances.data)
            logger.debug(f"Persisting {number_of_breeds} cat breeds")
            self.stdout.write(f"Persisting {number_of_breeds} cat breeds...")
            breeds_instances.save()
            logger.debug(f"Persisted {number_of_breeds} cat breeds")
            self.stdout.write(self.style.SUCCESS(f"Persisted {number_of_breeds} cat breeds"))
        else:
            logger.error(f"Error persisting cat breeds. error={breeds_instances.errors}")
            self.stderr.write(self.style.ERROR(f"Error persisting cat breeds. error={breeds_instances.errors}"))

        logger.info("Finished cat breeds retrieval and persistence.")
        self.stdout.write(self.style.SUCCESS("Finished cat breeds retrieval and persistence."))
