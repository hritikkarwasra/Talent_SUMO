
from dataclasses import fields
from rest_framework import serializers

from Talent_SUMO.databse.models import *

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
            model = Candidates
            fields= {'id'}