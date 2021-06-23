
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from .serializers import DataSerializer
from .models import Data


class PostView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class GetView(APIView):
    def get(self,request,pk,*args,**kwargs):
        try:
            t = Data.objects.get(id=pk)
            serializer=DataSerializer(t,many=False)
            return Response(serializer.data)
        except Data.DoesNotExist:
            t = None
            serializer=DataSerializer(t,many=False)
            raise Http404



class DeleteView(APIView):
    def delete(self,request,pk,*args,**kwargs):
            try:
                q = Data.objects.get(id=pk)
                q.delete()
                return Response("Item Deleted Successfully") 
            except:
                raise Http404

class PutView(APIView):
    def put(self,request,pk,*args,**kwargs):
            try:
                t = Data.objects.get(id=pk)
            except Data.DoesNotExist:
                raise Http404
            serializer=DataSerializer(t,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
