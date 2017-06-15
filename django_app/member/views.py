from django.contrib.auth import authenticate, login, logout as django_logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from member.models import User


def login_check(request):
    # memberlogin.html 생성
    #   username, password, button이 있는 HTML 생성
    #   POST요청이 올 경우 좌측 코드를 기반으로 로그인 완료 후 post_list로 이동
    #   실패할 경우 HttpResponse로 'Login invalid' 띄워주기

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post:post_list')
        else:
            HttpResponse('Login invalid')

    else:
        if request.user.is_authenticated:
            return redirect('post:post_list')
        return render(request, 'member/login.html')


def logout(request):
    django_logout(request)
    return redirect('post:post_list')


def signup(request):
    # member/signup.html을 사용
    # username, passworld1, password2를 받아 회원가입
    # 이미 유저가 존재 하는지 검사
    # password1, password2가 일치 하는지 검사
    # 각각의 경우를 검사해서 틀릴경우 오류메시지 리턴
    # 가입에 성공시 로그인 시키고 post_list로 리다이렉트

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = authenticate(request, username=username, password=password1)

        if user is None:
            user = User.objects.create_user(
                username=username,
                password=password1,
            )
            login(request, user)
            return redirect('post:post_list')
        else:
            return HttpResponse('Username already exists.')
    else:
        return render(request, 'member/signup.html')
