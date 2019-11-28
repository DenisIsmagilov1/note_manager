from rest_framework import serializers
from ..models import Note, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class NoteSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'category', 'elect', 'created']
