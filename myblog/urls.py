from django.conf.urls import url
from myblog.views import post_list, post_detail, post_new, post_edit

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'/edit/(?P<pk>\d+)/$', post_edit, name='post_edit'),
    url(r'/(?P<pk>\d+)/$', post_detail, name='detail'),
    url(r'/new/', post_new, name='post_new'),
]