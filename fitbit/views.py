from django.shortcuts import render

from rest_framework import viewsets, filters

from .models import HourSteps
from .serializer import HourStepsSerializer, HourStepsFilter


class HourStepsViewSet(viewsets.ModelViewSet):
    queryset = HourSteps.objects.all()
    serializer_class = HourStepsSerializer

class HourStepsSearchViewSet(viewsets.ModelViewSet):
    queryset = HourSteps.objects.all()
    serializer_class = HourStepsSerializer
    filter_class = HourStepsFilter
