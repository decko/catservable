from django.urls import path

from .views import CatBreedAPIView

app_name = "core"
urlpatterns = [
    path('breeds/', CatBreedAPIView.as_view(), name="breeds_list")
]
