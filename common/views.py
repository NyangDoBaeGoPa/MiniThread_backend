from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404


# 회원가입
@api_view(['POST'])
@permission_classes([AllowAny])  # 인증 필요없다
def signup(request):
    print('request', request)
    print('request.data', request.data['_content'])
    serializer = UserCreateSerializer(data=request.data['_content'])
    if serializer.is_valid(raise_exception=True):
        serializer.save()  # DB 저장
        return Response(serializer.data, status=201)


# 로그인"
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        # account_id required
        if serializer.validated_data['account_id'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': True,
            'token': serializer.data['token']  # 시리얼라이저에서 받은 토큰 전달
        }
        return Response(response, status=status.HTTP_200_OK)
