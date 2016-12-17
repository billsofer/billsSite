from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
import datetime
from .models import picture

# Create your views here.

def index(request):
	this_date = timezone.now()
	latest_picture_list = picture.objects.order_by('-date')[:10]
	context = {'latest_picture_list':latest_picture_list, 'currentdate':this_date}
	return render(request, 'latest_picture_list2.html', context)
	
def post_detail(request, pk):
	this_date = timezone.now()
	p = get_object_or_404(picture, pk=pk)
	return render(request, 'detail2.html', {'picture': p, 'currentdate':this_date})