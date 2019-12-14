from rest_framework import serializers

from .models import User, UserManager
from rest_framework_jwt.settings import api_settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'date_of_birth', 'height', 'weight')


class AuthRegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, required=False)

    #sign up時にtokenを発行するためにmodelにはないtoken フィールドを追加している　
    class Meta:
        model = User
        fields = ('token', 'id','email', 'username', 'date_of_birth', 'height', 'weight', 'password')

    #tokenを返す
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
        
    #ユーザー情報を返す
    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)