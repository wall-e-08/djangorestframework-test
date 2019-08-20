from rest_framework import serializers
from .models import Newspaper


class NewspaperSerializerOne(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    page = serializers.IntegerField()
    genre = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Newspaper.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.page = validated_data.get('page', instance.page)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance

