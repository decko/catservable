import pytest
from model_bakery import baker


@pytest.fixture
def catbreed():
    breed = baker.make("core.CatBreed")

    return catbreed
