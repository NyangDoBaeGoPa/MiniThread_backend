from rest_framework import serializers
from common.models import User


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(  # User 생성
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user
