from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.get_genres),
    path('movies/', views.get_movies),
    path('reviews/', views.get_reviews),
    path('movies/<int:movie_pk>/',views.movie_detail),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/',views.movie_get_review),
]
