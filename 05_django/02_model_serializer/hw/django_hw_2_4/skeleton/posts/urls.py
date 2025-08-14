from django.urls import path
from . import views
urlpatterns = [
    path('',views.post_list),
    path('<int:post_pk>',views.post_details)
]