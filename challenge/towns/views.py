# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Town
from .serializers import TownSerializer

class TownsView(ListAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer

    def get(self, request, *args, **kwargs):
        town1 = Town(region_code = 53,
                     region_name = "Bretagne",
                     department_code = 22,
                     district_code = 2,
                     town_code = 137,
                     town_name = "Maël-Carhaix",
                     population = 1580)
        town1.save()
        town2 = Town(region_code = 11,
                     region_name = "Île-de-France",
                     department_code = 93,
                     district_code = 3,
                     town_code = 66,
                     town_name = "Saint-Denis",
                     population = 111752)
        town2.save()
        town3 = Town(region_code = 11,
                     region_name = "Île-de-France",
                     department_code = 75,
                     district_code = 1,
                     town_code = 108,
                     town_name = "Paris 8e  Arrondissement",
                     population = 38902)
        town3.save()
        
        return self.list(request, *args, **kwargs)

    def getTowns(request):
        towns = Town.objects.values()
        paginator = Paginator(towns, 1)
        page = request.GET.get('page')
        try:
            towns = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            towns = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            towns = paginator.page(paginator.num_pages)
        return JsonResponse(dict(towns_list = list(towns)))
    
