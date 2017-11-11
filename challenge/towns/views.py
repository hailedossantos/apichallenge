# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from django.db.models import Avg, Count, Max, Min

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

class AggregationView(GenericAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer

    def get(self, request, *args, **kwargs):
        params = {}
        for param in request.query_params:
            params[param] = request.query_params[param]
        filtered_queryset = self.get_queryset().filter(**params)
        agg_queryset = filtered_queryset.aggregate(Min('population'),
                                                   Avg('population'),
                                                   Max('population'))
        agg_queryset['count'] = filtered_queryset.count()
        return Response(agg_queryset, content_type="application/json")
