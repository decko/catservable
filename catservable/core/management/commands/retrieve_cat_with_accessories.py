import logging

from django.core.management.base import BaseCommand
from rest_framework.exceptions import ValidationError

from tapioca.exceptions import ClientError, ServerError

from catservable.core.resources import CatAPI
from catservable.core.serializers import CatImageModelSerializer

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Retrieve cats with hats or eyeglasses."
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument(
            '--accessory',
            help="Download images of cats using hats.",
        )

    def handle(self, *args, **kwargs):
        NUMBER_OF_IMAGES = 3

        api = CatAPI()

        logger.debug("Retrieving categories list.")
        self.stdout.write("Retrieving categories list.")
        categories_request = api.categories().get()
        categories = categories_request().data
        selected_category = kwargs["accessory"]

        category_id = ""
        for category in categories:
            if category["name"] == selected_category:
                category_id = category["id"]

        if not category_id:
            msg = f"Category {selected_category} not found."
            logger.info(msg)
            self.stderr.write(self.style.ERROR(msg))
            raise Exception(msg)

        logger.info(f"Looking for cat images with {selected_category}")
        self.stdout.write(f"Looking for cat images with {selected_category}")
        cat_images_request = api.images().get(params={"category_ids": category_id, "limit": NUMBER_OF_IMAGES})

        try:
            logger.info(f"Retrieving image of a cat with {selected_category}")
            cat_images = cat_images_request().data
            logger.info(f"Persisting image of a cat with {selected_category}...")

            cat_serialzier = CatImageModelSerializer(data=cat_images, many=True)
            cat_serialzier.is_valid(raise_exception=True)
            cat_serialzier.save()
            logger.info(f"Retrieved images of cat with {selected_category} with success!")
            self.stdout.write(self.style.SUCCESS(f"Retrieved images of cat with {selected_category} with success!"))
        except (ClientError, ServerError, ValidationError) as exp:
            logger.error(f"Failed to retrieve and persist cat image. error={exp}")
            self.stderr.write(self.style.ERROR("Failed to retrieve and persist cat image."))

