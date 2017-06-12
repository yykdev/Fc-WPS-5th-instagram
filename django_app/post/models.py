from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
# comfig/settings.py 파일 import


# class User(models.Model):
#     name = models.CharField(max_length=30)


class Post(models.Model):
    # Django가 제공하는 기본 User와 연결되도록 수정
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
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
        settings.AUTH_USER_MODEL,
        related_name='like_posts',
        through='PostLike',

    )
    tags = models.ManyToManyField('Tag')

    def add_comment(self, user, content):
        # 자신을 post로 갖고 전달받은 user를 author로 가지며
        # constent를 content필드 내용으로 넣는 Comment 객체 생성
        return self.comment_set.create(author=user, content=content)

    def add_tag(self, tag_name):
        # tags에 tag_name매개변수로 전달 된 값(str)을
        # name으로 갖는 Tag 객체를 (이미 존재하면) 가져오고 없으면 생성하여
        # 자신의 tags에 추가
        tag, tag_created = Tag.objects.get_or_create(name=tag_name)
        # 튜플로 받을 경우 (태그값, get과 create여부) 리턴 get False, create True
        if not self.tags.filter(name=tag_name).exists():
            # 현재 포스트가 특정 태그를 가지고 있지 않을 경우
            # 현재 포스트의 태그 리스트에 tag를 추가 한다.
            self.tags.add(tag)

    def like_count(self):
        # 자신을 like하고 있는 user 수 리턴
        return self.like_users.count()


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    create_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'post_post_like_users'
    #     # 테이블 참조 시 migrate 에서 already exists 오류 발생할 경우
    #     # ./manage.py migrate --fake 해준다.


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='CommentLike',
        related_name='like_comments',
    )


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    create_date = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
