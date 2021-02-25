from rest_framework import serializers
from ..models import Comment
from ..serializers.comment_like import CommentLikeSerializer

print(CommentLikeSerializer)
class CommentSerializer(serializers.ModelSerializer):
    example = CommentLikeSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'message', 'created_at', 'edited_at', 'user_id', 'post_id', 'parent_id','example']

