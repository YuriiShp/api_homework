from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import TV, Chair



class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    manufacturer = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)

    def validate(self, attrs):
        if attrs.get('price') > 0:
            return attrs
        else:
            raise ValidationError(detail="invalid price")


class TVSerializer(ArticleSerializer):
    model = serializers.CharField(required=True)
    screen_size = serializers.CharField(required=True)
    power_consumption = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return TV.objects.create(**validated_data)


class ChairSerializer(ArticleSerializer):
    type = serializers.CharField(required=True)
    weight = serializers.FloatField(required=True)

    def validate(self, attrs):
        super().validate(attrs)
        if attrs.get('weight') > 0:
            return attrs
        else:
            raise ValidationError(detail="invalid weight")

    def create(self, validated_data):
        return Chair.objects.create(**validated_data)
