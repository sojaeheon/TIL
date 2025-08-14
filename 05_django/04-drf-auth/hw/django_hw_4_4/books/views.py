from django.shortcuts import render
from rest_framework.decorators import api_view



# Create your views here.
@api_view(['GET'])
def books_list(request):
    pass


@api_view(['POST'])
def borrow_book(request, isgn):
    pass