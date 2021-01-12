import pytest
from model_bakery import baker


@pytest.fixture
def catbreed():
    breed = baker.make("core.CatBreed")

    yield breed

    breed.delete()
