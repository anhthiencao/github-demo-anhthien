from rest_framework import serializers
from ..models import PostImages

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = '__all__'

