from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect

from ..forms import UserEditForm

User = get_user_model()

__all__ = (
    'profile',
    'profile_edit'
)

def profile(request, user_pk=None):
    NUM_POST_PER_PAGE = 3
    # 0. urls.py와 연결

    # 1. user_pk 에 해당하는 User를 cur_user키로 render

    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except Exception as e:
        page = 1
        print(e)

    if user_pk:
        user = get_object_or_404(User, pk=user_pk)
    else:
        user = request.user

    posts = user.post_set.order_by('-created_date')[:page * NUM_POST_PER_PAGE]
    post_count = user.post_set.count()

    next_page = page + 1 if post_count > page * NUM_POST_PER_PAGE else None

    context = {
        'cur_user': user,
        'posts': posts,
        'post_count': post_count,
        'page': page,
        'next_page': next_page,
    }
    return render(request, 'member/profile.html', context=context)

    # 2. member/profile.html작성 해당 user정보 보여주기
    #   2-1. 해당 user의 followers, following목록 보여주기

    # 3. 현재 로그인한 유저가 해당 유저(cur_user)를 팔로우하고 있는지 여부 보여주기
    #   3-1. 팔로우하고 있다면 '팔로우 해제' 버튼, 아니라면  '팔로우' 버튼 띄워주기

    # 4. def follower_toggle(request) 뷰 생성

    ###### 과제
    """
        1. GET parameter로 'page'를 받아 처리
        page가일 경우 Post의 author가 해당 User인
        Post목록을 -created_date 순서로 page*9 만큼의
        QuerySet 을 생성해서 리턴

        만약 실제 Post 개수보다 큰 page가 왔을 경우 최대한의 값을 보여줌
        int로 변환 불가능한 경우 except처리
        1보다 작은 값일 경우 except처리
        'page'키ㅢ 값이 오지 않을 경우 page=1로 처리

        2. def follow_toggle(request, user_pk)
        위 함수 기반 뷰를 구현
    """

def profile_edit(request):
    """
    request.method == 'POST' 일 때
        nickname과 img_profile(필드도 모델에 추가을 수정할 수 있는
        userEditForm을 구성 ( ModelForm상속)
    """
    if request.method == 'POST':
        form = UserEditForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('member:my_profile')
    else:
        form = UserEditForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'member/profile_edit.html', context)