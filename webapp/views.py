from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import Serializer 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from .models import todo 
from .serializer import *
# Create your views here.

class todoList(APIView):

        def get(self,request):
            todos = todo.objects.all() 
            serializer = todoSerializer(todos,many=True)
            return Response(serializer.data) 

        def post(self):
            pass