import pytest
from django.urls import reverse

from .models import CatBreed

pytestmark = pytest.mark.django_db


def test_url_to_list_cat_breeds():

    viewname = "core:breeds_list"

    url = reverse(viewname)

    assert url == "/breeds/"


def test_attributes_for_cat_breed_model():

    attributes = {"origin", "temperament", "description"}

    for attribute in attributes:
        assert hasattr(CatBreed, attribute)


def test_return_attributes_on_a_GET_request(client, catbreed):

    attributes = {"origin", "temperament", "description"}

    viewname = "core:breeds_list"
    url = reverse(viewname)

    request = client.get(url)
    breed_data = request.data[0]

    assert attributes < set(breed_data.keys())
