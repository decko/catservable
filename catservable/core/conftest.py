import pytest
from model_bakery import baker

from .models import CatBreed


@pytest.fixture
def catbreed():
    breed = baker.make("core.CatBreed")

    yield breed

    breed.delete()


@pytest.fixture
def energetic_temper_breed():
    breed = baker.make("core.CatBreed", temperament=["Energetic"])
    return breed


@pytest.fixture
def intelligent_temper_breed():
    breed = baker.make("core.CatBreed", temperament=["Intelligent"])
    return breed


@pytest.fixture
def independent_temper_breed():
    breed = baker.make("core.CatBreed", temperament=["Independent"])
    return breed


@pytest.fixture
def super_breed():
    breed = baker.make("core.CatBreed", temperament=["Independent", "Energetic"])
    return breed


@pytest.fixture
def catbreeds(energetic_temper_breed, intelligent_temper_breed, independent_temper_breed, super_breed):

    return CatBreed.objects.all()
