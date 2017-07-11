from rest_framework import serializers

from ..models import Post

__all__ = {
    'PostSerializer',
}


class PostSerializer(serializers.MdelSerializer):
    class Meta:
        model = Post
        fields = {
            'pk',
            'photo',
        }
