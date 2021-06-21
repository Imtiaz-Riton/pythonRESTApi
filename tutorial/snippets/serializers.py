from rest_framework import serializers
from .models import Snippet, ModelToDelete, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style','name']


class ModelToDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelToDelete
        fields = ['id','class_name','name']