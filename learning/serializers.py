from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Newspaper

User = get_user_model()


# normal serializer
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


# model serializer
class NewspaperSerializerTwo(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ['id', 'title', 'page', 'genre']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']
