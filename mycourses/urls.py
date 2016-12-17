from django.conf.urls import url
from mycourses.views import courses_list, courses_detail

urlpatterns = [
    url(r'^$', courses_list, name='courses'),
    url(r'(?P<pk>\d+)/$', courses_detail, name='course'),
]