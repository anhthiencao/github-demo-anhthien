from rest_framework import serializers
from ..models import Comment
from ..serializers.comment_like import CommentLikeSerializer


class CommentSerializer(serializers.ModelSerializer):
    comment_like = CommentLikeSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'



