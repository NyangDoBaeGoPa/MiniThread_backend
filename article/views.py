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
    
    # 새로운 게시글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = MiniThreadSerializer(data=request.data)
        if serializer.is_valid(): # 유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# article의 detail을 보여주는 역할
class ArticleDetail(APIView):
    # 객체 가져오기
    def get_object(self, pk):
        try:
            return MiniThread.objects.get(pk=pk)
        except MiniThread.DoesNotExist:
            raise Http404
