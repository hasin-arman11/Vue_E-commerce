from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import CustomUsers
from .serializer import User_Serializer
from .import permissions
# Create your views here.
class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwargs):
        serializer=User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data={'Message':'error occured'})
    

class LoginView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,*args,**kwargs):
        username=self.request.GET['username']
        passwprd=self.request.GET['password']
        queryset=CustomUsers.objects.filter(username=username,password=passwprd).first()
        serializer=User_Serializer(queryset)
        return Response(serializer.data)
        