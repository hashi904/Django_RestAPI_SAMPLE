from django.shortcuts import render

from rest_framework import viewsets, filters

from .models import HourSteps
from .serializer import HourStepsSerializer


class HourStepsViewSet(viewsets.ModelViewSet):
    queryset = HourSteps.objects.all()
    serializer_class = HourStepsSerializer