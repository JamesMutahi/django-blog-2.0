from django.conf.urls import url
from django.urls import re_path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    # url(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$', views.post_detail,
            name='post_detail'),
    re_path(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]
