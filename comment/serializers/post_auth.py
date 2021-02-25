from rest_framework import serializers
from ..models import PostAuth

class PostAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAuth
        fields = ['post_id', 'auth_id', 'type']