from connect.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GetConnectUserSerializer

# Create your views here.


class UserDetailView(APIView):

    def get(self, request):
        serializer = GetConnectUserSerializer(request.user)
        return Response(serializer.data)