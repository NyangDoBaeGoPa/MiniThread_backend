from .models import MiniThread
from rest_framework import serializers

class MiniThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniThread
        fields = '__all__' # title과 content 모두 직렬화