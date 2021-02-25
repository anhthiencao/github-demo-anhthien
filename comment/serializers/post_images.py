from rest_framework import serializers
from ..models import PostImages

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ['post_id', 'image']