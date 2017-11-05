# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

def getTowns(request):
    data = {'name': 'Town1'}
    return JsonResponse(data)
