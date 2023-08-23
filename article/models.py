from django.db import models
from django.conf import settings

# Create your models here.
class MiniThread(models.Model):
    title = models.CharField(max_length=50) # 제목 길이: 최대 50자
    content = models.TextField() # 내용 입력
    
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    ## created_at 부분에서 python manage.py makemigrations 할 때, 에러 발생
    ## 해결책: 뜨는 옵션창에서 1번 선택 후 created_at의 auto_now_add=True, default=timezone.now()로 수정하면 된다고 인터넷에서는 말함.
    ## 이렇게 수정하는 것이 전체 세팅에서 문제가 없는지 의문이 들어 보류해놓은 상태태