from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Hello world!를 출력해주는 index 함수를 만든다
def index(request):
    context = {

    }
    # return render(request, 'post/index.html', context=context)
    return HttpResponse('Hello world')

# 모든 포스트 항목을 출력
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'post/post_list.html', context=context)