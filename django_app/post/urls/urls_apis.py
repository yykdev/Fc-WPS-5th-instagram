from django.conf.urls import url

from .. import apis

urlpatterns = [
    url(r'^$', apis.PostListCreateView.as_view()),
    url(r'^toggle/(?P<post_pk>\d+)$', apis.PostLikeToggleView.as_view()),
]
