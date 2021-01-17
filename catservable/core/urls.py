from django.urls import path

from .views import cat_breed_search_by_origin, cat_breed_search_by_temper, CatBreedListAPIView, CatBreedRetrieveAPIView

app_name = "core"
urlpatterns = [
    path('breeds/search/temper/<str:temper>/', cat_breed_search_by_temper, name="breeds_temper_search"),
    path('breeds/search/origin/<str:origin>/', cat_breed_search_by_origin, name="breeds_origin_search"),
    path('breeds/<str:pk>/', CatBreedRetrieveAPIView.as_view(), name="breeds_detail"),
    path('breeds/', CatBreedListAPIView.as_view(), name="breeds_list")
]
