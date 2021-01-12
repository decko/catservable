from django.urls import path

from .views import CatBreedListAPIView, CatBreedRetrieveAPIView

app_name = "core"
urlpatterns = [
    path('breeds/<int:pk>/', CatBreedRetrieveAPIView.as_view(), name="breeds_detail"),
    path('breeds/', CatBreedListAPIView.as_view(), name="breeds_list")
]
