from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
    # 직렬화를 한다.
        # 모델에 대한 정보를 토대로
        model = Article
        fields = ('id','title',)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'