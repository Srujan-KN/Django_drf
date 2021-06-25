from rest_framework import serializers
from .models import authors,books



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=authors
        fields="__all__"
class BookSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=books
        fields="__all__"



