from rest_framework import serializers

from .models import HourSteps
from django_filters import rest_framework as filters

class HourStepsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HourSteps
        fields = ('id', 'hour_steps', 'time', 'string_date')

class HourStepsFilter(filters.FilterSet):
    string_date = filters.CharFilter( lookup_expr='contains')
    class Meta:
        model = HourSteps
        fields = ('id', 'hour_steps', 'time', 'string_date')