from django.urls import re_path, path
from . import views

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

app_name = 'blog'

# urlpatterns = [
#     re_path(r'^$', views.post_list, name='post_list'),
#     re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
#     re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$', views.post_detail,
#             name='post_detail'),
#     re_path(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
# ]


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
