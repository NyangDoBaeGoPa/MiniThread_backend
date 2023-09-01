from .models import MiniThread
from rest_framework import serializers

class MiniThreadSerializer(serializers.ModelSerializer):
    # 처음 가입할 때, 입력한 user name을 serializer에서 받아와야 함.
    user = serializers.ReadOnlyField(source = 'user.account_id')
    class Meta:
        model = MiniThread
        # 표시되는 항목 직렬화
        fields = ['id', 'title', 'created_at', 'updated_at', 'user', 'content']