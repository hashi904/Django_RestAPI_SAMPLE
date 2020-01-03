from django.shortcuts import render

from rest_framework import viewsets, filters

from .models import HourSteps
from .serializer import HourStepsSerializer, HourStepsFilter


class HourStepsViewSet(viewsets.ModelViewSet):
    queryset = HourSteps.objects.all()
    serializer_class = HourStepsSerializer
    def get_queryset(self):
        queryset = HourSteps.objects.all()
        string_date = self.request.query_params.get('string_date', None)
        if string_date is not None:
            queryset = queryset.filter(string_date=string_date)
        return queryset

class HourStepsSearchViewSet(viewsets.ModelViewSet):
    queryset = HourSteps.objects.all()
    serializer_class = HourStepsSerializer
    filter_class = HourStepsFilter
