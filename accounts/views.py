from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import login, logout, authenticate


from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import exceptions


from .models import MyUser
from .serializers import MyUserSerializerPOST, MyUserSerializerUpdate, MyUserSerializer

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
        
    
class MyUserGETPOSTView(APIView):
    permission_classes = [permissions.IsAdminUser,
                          permissions.IsAuthenticated]

    def get(self, request, format = None):

        users = MyUser.objects.all()

        user_serializer = MyUserSerializer(users, many = True)

        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format = None):
        
        user_serializer = MyUserSerializerPOST(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message":"Usuario registrado exitosamente!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"Los datos ingresados no son validos. Por favor revisalos."})
    


class MyUserPUTView(APIView):


    def get_user(self, pk):
        try:
            user = MyUser.objects.get(pk=pk)
            return user
        except MyUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        user = self.get_user(pk=pk)
        user_serializer = MyUserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk, format = None):
        user = self.get_user(pk=pk)
        user_serializer = MyUserSerializerUpdate(user, data=request.data, partial = True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message":"Usuario actualizado correctamente"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Los datos ingresadon no son validos."}, status=status.HTTP_400_BAD_REQUEST)

get_user_with_pk = MyUserPUTView()

class MyUserDELETEView(APIView):
    permission_classes = [
        permissions.IsAdminUser, permissions.IsAuthenticated,
    ]

    def get(self, request, pk):
        user = get_user_with_pk.get_user(pk)
        user_serializer = MyUserSerializer(user)
        try:
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return Response({"Usuario no existe"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format = None):
        user = get_user_with_pk.get_user(pk)
        user.delete()
        return Response({"message":"Usuario eliminado correctamente"}, status=status.HTTP_200_OK)
        