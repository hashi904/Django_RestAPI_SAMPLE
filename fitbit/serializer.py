from rest_framework import serializers

from .models import HourSteps

class HourStepsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HourSteps
        fields = ('id', 'hour_steps', 'time', 'string_date')