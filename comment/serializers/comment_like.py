from rest_framework import serializers
from ..models import CommentLike

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['id','comment_id', 'user_id']