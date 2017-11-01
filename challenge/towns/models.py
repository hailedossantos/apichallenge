# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Town(models.Model):
    region_code = models.IntegerField()
    region_name = models.CharField(max_length=100)
    department_code = models.IntegerField()
    district_code = models.IntegerField()
    town_code = models.IntegerField(primary_key=True)
    town_name = models.CharField(max_length=100)
    population = models.IntegerField()
