from django.shortcuts import render
from django.http import Http404

from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import (MyUser, MyUserSerializerDELETE,
                        MyUserSerializerGET, MyUserSerializerPOST,
                        MyUserSerializerPUT)

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
        
class GetUserView(generics.RetrieveAPIView):
    serializer_class = MyUserSerializerGET
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class PutUserView(generics.UpdateAPIView):
    serializer_class = MyUserSerializerPUT
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        return self.request.user
    
class DeleteUserView(generics.DestroyAPIView):
    serializer_class = MyUserSerializerDELETE
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
