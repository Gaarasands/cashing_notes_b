from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view



@api_view(['POST'])
def add(request):
    user = UserSerializer(data=request.data, context={'request': request})
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})
    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
