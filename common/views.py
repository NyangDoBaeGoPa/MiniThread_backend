from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserCreateSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404


# 회원가입
@api_view(['POST'])
@permission_classes([AllowAny])  # 인증 필요없다
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()  # DB 저장
        return Response(serializer.data, status=201)


# 로그인
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    return Response({"content": "Hello World!"})
