from rest_framework import serializers
from ..models import PostAttachments

class PostAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachments
        fields = '__all__'

