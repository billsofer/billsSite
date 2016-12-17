from django.shortcuts import render
from django.utils import timezone
import datetime



# Create your views here.

def intro(request):
	this_date = timezone.now()
	context = {'currentdate':this_date}
	return render(request, 'intro_more.html', context)
