
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from .serializers import DataSerializer
from .models import Data



class TestView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Data.objects.all().last()
        serializer=DataSerializer(qs)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            d=dict()
            d=serializer.data
            out=dict()
            out['Greeting']="Hello "+d['name']  
            out['Message']="How are things at "+d['city']+"?"
            return Response(out)
        return Response(serializer.errors)

