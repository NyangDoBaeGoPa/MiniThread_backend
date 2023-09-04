# 데이터 처리
from .models import MiniThread
from .serializer import MiniThreadSerializer

# APIView를 사용하기 위한 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# 인증관련
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrReadOnly

# Create your views here.
# article 목록을 보여주는 역할
class ArticleList(APIView):
    # authentication 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    # permission 추가
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Article list를 보여줄 때
    def get(self, request):
        articles = MiniThread.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many = True로 설정
        serializer = MiniThreadSerializer(articles, many=True)
        return Response(serializer.data)
    
# 새로운 게시글을 작성할 때
class ArticleCreate(APIView):
    # authentication 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    # permission 추가
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = MiniThreadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 유효성 검사
            serializer.save(user = request.user) # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
# article의 detail을 보여주는 역할
class ArticleDetail(APIView):
    # authentication 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    # permission 추가
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # 객체 가져오기
    def get_object(self, pk):
        try:
            return MiniThread.objects.get(pk=pk)
        except MiniThread.DoesNotExist:
            raise Http404

    # detail 보기
    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = MiniThreadSerializer(article)
        return Response(serializer.data)
    
    # article 수정하기
    def put(self, request, pk, format=None):        
        article = self.get_object(pk)
        serializer = MiniThreadSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            # return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # article 삭제하기
    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)