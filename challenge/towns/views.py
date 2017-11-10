# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Town
from .serializers import TownSerializer

import json

class TownsView(ListAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer

    def get(self, request, *args, **kwargs):        
        return self.list(request, *args, **kwargs)    
