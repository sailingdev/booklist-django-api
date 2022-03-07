from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email as email_validator
from rest_framework import serializers

from .models import (
    WriterModel,
    GenreModel,
    BookModel
)


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterModel
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):

    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=GenreModel.objects.all())
    class Meta:
        model = BookModel
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['writer'] = WriterSerializer(instance.writer).data
        response['genres'] = GenreSerializer(instance.genres, many=True).data
        return response

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            new_value = value
            old_value = getattr(instance, field)

        return super(BookSerializer, self).update(instance, validated_data)