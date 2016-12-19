from django.shortcuts import render
from django.utils import timezone
import datetime

# Create your views here.
def books_list(request):
	this_date = timezone.now()
	ige = 'Introduction to Genetic Engineering'
	gog = 'Giants of Genetics'
	csc = 'Clones and Stem Cells'
	books_context = {'IGE':ige, 'GOG':gog, 'CSC':csc, 'currentdate':this_date,}
	return render(request, 'books_list.html', books_context)
"""
def courses_detail(request):
	this_date = timezone.now()
	# classes = Class.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'courses_detail.html', {'currentdate':this_date})
	"""