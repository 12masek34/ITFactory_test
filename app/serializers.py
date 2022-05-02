from rest_framework import serializers
from . import models


class SalePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SalePoint
        fields = ('id', 'name')


class RequestVisitSerializer(serializers.Serializer):
    sale_point = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    class Meta:
        models = models.Visiting
        fields = ('sale_point', 'sale_point', 'longitude')


class ResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    visit_date = serializers.DateTimeField()

    class Meta:
        model = models.Visiting
        fields = ('id', 'visit_date')
