# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from django_filters import rest_framework as filters

from .models import Town
from .serializers import TownSerializer

class TownFilter(filters.FilterSet):
    class Meta:
        model = Town
        fields = {
            'population': ['lt', 'gt'],
            'department_code': ['exact', 'lt', 'gt'],
            'town_name': ['icontains'],
        }

class TownsView(ListAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = TownFilter

    def get(self, request, *args, **kwargs):        
        return self.list(request, *args, **kwargs)    
