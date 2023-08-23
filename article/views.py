from django.shortcuts import render

# 데이터 처리
from .models import MiniThread
from .serializer import MiniThreadSerializer

# APIView를 사용하기 위한 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
# article 목록을 보여주는 역할
class ArticleList(APIView):
    # Article list를 보여줄 때
    def get(self, request):
        articles = MiniThread.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many = True로 설정
        serializer = MiniThreadSerializer(articles, many=True)
        return Response(serializer.data)