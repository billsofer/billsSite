from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
import datetime


def post_list(request):
	this_date = timezone.now()
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'post_list.html', {'posts':posts, 'currentdate':this_date})
	
def post_detail(request, pk):
	this_date = timezone.now()
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post':post,'currentdate':this_date})
