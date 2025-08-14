from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from rest_framework.decorators import api_view
from .models import Author
from rest_framework.response import Response
from .serializers import AuthorSerializer

# Create your views here.
@api_view(['GET'])
def author_detail(request,author_pk):
    author = get_object_or_404(Author,pk=author_pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)