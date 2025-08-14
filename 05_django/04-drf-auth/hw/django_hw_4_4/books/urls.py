from django.urls import path
from . import views

urlpatterns = [
    path("",views.books_list),
    path("borrow/<int:isbn>",views.borrow_book)
]