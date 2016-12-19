from django.conf.urls import url, include
from myphotos.views import index, post_detail

urlpatterns = [
    url(r'/(?P<pk>\d+)/$', post_detail, name='detail2'),
    url(r'$', index, name="index"),
    ]
