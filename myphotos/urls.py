from django.conf.urls import url, include
from myphotos.views import index, post_detail

urlpatterns = [
	# url(r'^$', index, name="index"),
    url(r'pics/$', index, name="index"),
    url(r'pics/(?P<pk>\d+)/$', post_detail, name='detail2'),
    ]
