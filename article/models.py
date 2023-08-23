from django.db import models
from django.conf import settings

# Create your models here.
class MiniThread(models.Model):
    title = models.CharField(max_length=50) # 제목 길이: 최대 50자
    content = models.TextField() # 내용 입력
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)