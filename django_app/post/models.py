from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     name = models.CharField(max_length=30)


class Post(models.Model):
    # Django가 제공하는 기본 User와 연결되도록 수정
    author = models.ForeignKey(User)
    photo = models.ImageField(blank=True)
    # pillow 설치 전 유의사항
    # 참고 : http://pillow.readthedocs.io/en/4.1.x/installation.html
    # brew install libtiff libjpeg webp little-cms2
    # : brew는 글로벌에 설치 되는 것이니 어느 위치에서 설치해도 상관없음
    # pip install pillow
    # virtualenv 내에서 설치
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts',
    )
    tags = models.ManyToManyField('Tag')


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
