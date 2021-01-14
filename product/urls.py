from django.urls import path

from .views import ProductsList, ProductDetail, CategoriesList


urlpatterns = [
    path('', ProductsList.as_view()),
    path('detail/<str:pk>/', ProductDetail.as_view()),
    path('categories/', CategoriesList.as_view()),
]