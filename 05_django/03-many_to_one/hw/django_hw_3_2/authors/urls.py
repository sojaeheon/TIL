from django.urls import path
from . import views

urlpatterns=[
    path('<int:author_pk>/',views.author_detail)
]