from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import login, logout, authenticate


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import exceptions


from .models import MyUser
from .serializers import MyUserSerializerPOST, MyUserSerializerUpdate

# Create your views here.

class Register(APIView):

    def get(self, format = None):

        format = {
            "username":"data(required)",
            "email":"data(required)",
            "password":"data(required)",
            "name":"data(not required)",
            "img_perfil":"data(not required)"
        }

        return Response(format, status=status.HTTP_200_OK)
    
    def post(self, request, format = None):

        user_serializer = MyUserSerializerPOST(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"ERROR":"Los datos ingresados no son validos"}, status=status.HTTP_400_BAD_REQUEST)
        
    
