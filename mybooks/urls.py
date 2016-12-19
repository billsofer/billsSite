from django.conf.urls import url
from mybooks.views import books_list

urlpatterns = [
    url(r'^$', books_list, name='books'),
]