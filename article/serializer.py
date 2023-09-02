from .models import MiniThread
from rest_framework import serializers
from common.serializers import UserInfoSerializer

class MiniThreadSerializer(serializers.ModelSerializer):
    # 처음 가입할 때, 입력한 account id를 serializer에서 받아와야 함.
    user = serializers.ReadOnlyField(source = 'user.account_id')
    class Meta:
        model = MiniThread
        # 표시되는 항목 직렬화
        fields = ['id', 'title', 'created_at', 'updated_at', 'user', 'content']