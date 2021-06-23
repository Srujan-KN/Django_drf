from rest_framework import serializers
from .models import Data

from django import forms

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields="__all__"



