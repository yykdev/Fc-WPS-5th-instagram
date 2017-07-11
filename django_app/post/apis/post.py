from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Post, Comment
from ..serializers import PostSerializer

__all__ = (
    'PostListCreateView',
)


class PostListCreateView(APIView):
    # get요청이 왔을 때, Post.objects.all()을
    # PostSerailizer를 통해 Response로 반환
    # DRF API Guide
    #   - API View
    #   - Serializers
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(author=request.user)
            comment_content = request.data.get('comment')
            if comment_content:
                instance.my_comment = Comment.objects.create(
                    post=instance,
                    author=instance.author,
                    content=comment_content,
                )
                instance.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

