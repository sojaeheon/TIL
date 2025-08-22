from rest_framework import serializers
from .models import Movie, Cast, Review, Genre
from django.contrib.auth import get_user_model
User = get_user_model()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

        
class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
        
    class Meta:
        model = Movie
        fields = '__all__'
        
        
class MovieDetailSerializer(serializers.ModelSerializer):
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
            
    genres = GenreNameSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        exclude = ('id',)

class ReviewSerializer(serializers.ModelSerializer):
    class MovieShortSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')
            
    movie = MovieShortSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        exclude = ('id', 'movie')
        
class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ReviewShortSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(read_only=True)  # 읽을 때 사용자 정보 제공

    class Meta:
        model = Review
        exclude = ('id', 'movie')
        
