from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
import datetime


def post_list(request):
	this_date = timezone.now()
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'post_list.html', {'posts':posts, 'currentdate':this_date})
	
def post_detail(request, pk):
	# assert False, "I'm in postdetail"
	this_date = timezone.now()
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post':post,'currentdate':this_date})
	
def post_edit(request, pk):
	# assert False, "I'm in postedit"
	this_date = timezone.now()
	post=get_object_or_404(Post, pk=pk)
	
	if request.method == "POST":
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			# stays the same: post.published_date = timezone.now() 
			post.save()
			
			return redirect('detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form': form, 'currentdate':this_date})
	
def post_new(request):
	this_date = timezone.now()
	if request.method == "POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'post_new.html', {'form': form, 'currentdate':this_date})
	
