#from django.http import response
#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status

from .serializer import PersonSerializer
from .models import Person

# Create your views here.


class ListPersons(APIView):
    
    
    def get(self,request):
        queryset = Person.objects.all()
        serializer_class = PersonSerializer(queryset,many=True)
        return Response(serializer_class.data)

    def post(self,request):
        print(request.META['HTTP_ORIGIN'])
        print(request.body)
        print(request.data)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@get ')
        #print(request.META.keys())
        
        serializer = PersonSerializer(data=request.data)
        print('seriaxgffffffffffffffffffffffffffffffffffffffffffffffffffffffflizer')
        if serializer.is_valid():
            
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
