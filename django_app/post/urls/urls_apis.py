from django.conf.urls import url

from .. import apis

urlpattern = [
    url(r'^$', apis.PostListView.as_view())
]