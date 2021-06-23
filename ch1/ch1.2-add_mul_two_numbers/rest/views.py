
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from .serializers import DataSerializer




class TestView(APIView):
    

    def post(self,request,*args,**kwargs):
        serializer=DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            d=dict()
            d=serializer.data
            out=dict()
            out['sum']=d['number1']+d['number2']
            out['product']=d['number1']*d['number2']
            
            return Response(out)
        return Response(serializer.errors)
