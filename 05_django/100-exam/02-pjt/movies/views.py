from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Movie, Cast, Review, Genre
from .serializers import MovieSerializer, GenreSerializer, ReviewSerializer, MovieDetailSerializer, ReviewShortSerializer, CastSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .permmisions import IsAuthorOrReadOnly

# Create your views here.


# F02 전체 장르 목록 조회 api
@api_view(['GET'])
def get_genres(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

# F03 전체 영화 목록 조회 api
@api_view(['GET'])
def get_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

# F04 단일 영화 상세 정보 조회 api
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        # pk에 해당하는 영화 불러오기
        movie = Movie.objects.get(pk = movie_pk)
        movie_casts = movie.cast_set.all()
        movie_reviews = movie.review_set.all()
        # serializer로 변환
        serializer = MovieDetailSerializer(movie)
        data = serializer.data
        data['casts'] = CastSerializer(movie_casts, many=True).data
        data['reviews'] = ReviewShortSerializer(movie_reviews, many=True).data
        
        return Response(data)

# F05 전체 리뷰 목록 조회
@api_view(['GET'])
def get_reviews(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

# F06 단일리뷰 조회/수정/삭제 api
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated,IsAuthorOrReadOnly])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 작성자 권한 체크
    permission = IsAuthorOrReadOnly()
    if not permission.has_object_permission(request, None, review):
        return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method in ['PUT','PATCH']:
        serializer = ReviewSerializer(review, data=request.data, partial=(request.method=='PATCH'))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# F07 특정 영화에 대한 리뷰 생성 api
@api_view(['POST'])
def movie_get_review(request,movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
    
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie, author=request.user)  # author 자동 연결
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
