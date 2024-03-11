from django.shortcuts import render
from django.contrib.auth.models import User
from .api.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UserView(APIView):
    # def get(self,request):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True,context  ={'request':request})
    #     return Response(serializer.data)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)