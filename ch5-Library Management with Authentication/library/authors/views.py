
from django.utils import tree
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from .serializers import DataSerializer,BookSerializer

from .models import authors,books

from rest_framework.permissions import IsAuthenticated


class PostView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        serializer=DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
class GetView(APIView):
    
    def get(self,request,*args,**kwargs):
        qs=authors.objects.all()
        serializer=DataSerializer(qs,many=True)
        return Response(serializer.data)

#---------------------------------------------------

class PostViewBook(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class GetViewBook(APIView):
    def get(self,request,*args,**kwargs):
        qs=books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(serializer.data)

class GetViewBookAuthor(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,pk,*args,**kwargs):
        try:
            t = authors.objects.get(author_id=pk)
            t2=books.objects.filter(author_id=pk)

            serializer=DataSerializer(t,many=False)
            serializer2=BookSerializer(t2,many=True)
            d={}
            d["books"]=serializer2.data
            return Response([serializer.data,d])
        except authors.DoesNotExist:
            t = None
            serializer=DataSerializer(t,many=False)
            raise Http404


class DeleteViewAuthor(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self,request,pk,*args,**kwargs):
        try:
            q = authors.objects.get(author_id=pk)
            q.delete()
            return Response("Author Deleted Successfully") 
        except:
            raise Http404

class DeleteViewBook(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self,request,pk,*args,**kwargs):
            try:
                q = books.objects.get(id=pk)
                q.delete()
                return Response("Book Deleted Successfully") 
            except:
                raise Http404


class PutViewAuthor(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request,pk,*args,**kwargs):
            try:
                t = authors.objects.get(author_id=pk)
            except authors.DoesNotExist:
                raise Http404
            serializer=DataSerializer(t,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class PutViewBook(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request,pk,*args,**kwargs):
            try:
                t = books.objects.get(id=pk)
            except books.DoesNotExist:
                raise Http404
            serializer=BookSerializer(t,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class PatchViewAuthor(APIView):
    permission_classes = (IsAuthenticated,)
    def patch(self, request, pk,*args, **kwargs):
            try:
                t = authors.objects.get(author_id=pk)
                serializer = DataSerializer(t, data=request.data, partial=True) # set partial=True to update a data partially
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
            except authors.DoesNotExist:
                raise Http404
            
class PatchViewBook(APIView):
    permission_classes = (IsAuthenticated,)
    def patch(self, request, pk,*args, **kwargs):
            try:
                t = books.objects.get(id=pk)
                serializer = BookSerializer(t, data=request.data, partial=True) # set partial=True to update a data partially
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
            except books.DoesNotExist:
                raise Http404
            