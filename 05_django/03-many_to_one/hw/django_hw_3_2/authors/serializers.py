from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    
    book_count = serializers.IntegerField(source='book_set.count', read_only=True)
    
    class Meta:
        model = Author
        fields = '__all__'

