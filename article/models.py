from django.db import models
from django.conf import settings
from common.models import User

# Create your models here.
class MiniThread(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) # 게시글의 id 값    
    title = models.CharField(max_length=50) # 제목 길이: 최대 100자
    created_at = models.DateTimeField(auto_now_add=True) # 작성날짜
    updated_at = models.DateTimeField(auto_now=True) # 수정날짜
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) # 작성자
    content = models.TextField() # 내용 입력