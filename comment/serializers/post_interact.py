from rest_framework import serializers
from ..models import PostInteract

class PostInteractSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostInteract
        fields = ['post_id', 'user_id', 'type']