from rest_framework import serializers

from .models import User, UserManager


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'date_of_birth', 'height', 'weight')


class AuthRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id','email', 'username', 'date_of_birth', 'height', 'weight', 'password')

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)