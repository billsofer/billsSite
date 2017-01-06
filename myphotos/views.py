from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from .models import picture

# Create your views here.

def index(request):
	this_date = timezone.now()
	latest_picture_list = picture.objects.order_by('-date')[:]
	# new Paginator code starts here ...
	page = request.GET.get('page', 1)
	paginator = Paginator(latest_picture_list, 2)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	context = {'users':users, 'currentdate':this_date}  
	# context = {'latest_picture_list':latest_picture_list, 'currentdate':this_date}
	# return render(request, 'latest_picture_list2.html', context)
	return render(request, 'latest_picture_list.html', context)
	
def post_detail(request, pk):
	this_date = timezone.now()
	p = get_object_or_404(picture, pk=pk)
	return render(request, 'detail2.html', {'picture': p, 'currentdate':this_date})