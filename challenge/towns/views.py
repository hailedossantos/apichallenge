# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

from .models import Town

def getTowns(request):
    town1 = Town(region_code = 53,
                region_name = "Bretagne",
                department_code = 22,
                district_code = 2,
                town_code = 137,
                town_name = "Maël-Carhaix",
                population = 1.580)
    town1.save()
    town2 = Town(region_code = 11,
                region_name = "Île-de-France",
                department_code = 93,
                district_code = 3,
                town_code = 66,
                town_name = "Saint-Denis",
                population = 111.752)
    town2.save()
    town3 = Town(region_code = 11,
                region_name = "Île-de-France",
                department_code = 75,
                district_code = 1,
                town_code = 108,
                town_name = "Paris 8e  Arrondissement",
                population = 38.902)
    town3.save()
    towns = Town.objects.values()
    return JsonResponse(dict(towns_list = list(towns)))
