from rest_framework import serializers

from .models import Blog

from accounts.serializer import UserSerializer

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'title', 'article', 'created_at', 'updated_at', 'user')