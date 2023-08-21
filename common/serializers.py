from rest_framework import serializers
from common.models import User


class UserCreateSerializer(serializers.Serializer):
    user_name = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(  # User 생성
            account_id=validated_data['account_id'],
            user_name=validated_data['user_name'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user
