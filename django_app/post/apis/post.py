from rest_framework.response import Response
from rest_framework.views import APIView
from post.serializers.post import PostSerializer
from ..models import Post

__all__ = (
    'PostListView',
)


class PostListView(APIView):
    # gett요청이 왔을 때, Post.ovjets.all()을
    # PostSerializer를 통해 Response로 반환
    # DRF API Guide
    #  - API View
    #  - Serializers

    def get(self, response, *args, **kwargs):
        posts = Post.objects.all()
        # serializer 처리를 할 객체가 복수이기 때문에 many=True 옵션을 준다.
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
