from rest_framework import serializers
from .models import Book, ExternalPost

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class ExternalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalPost
        fields = "__all__"
