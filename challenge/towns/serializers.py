from rest_framework import serializers
from .models import Town

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ('region_code',
                  'region_name',
                  'department_code',
                  'district_code',
                  'town_code',
                  'town_name',
                  'population')
