from django import forms
from .models import Post
from django.forms import ModelForm, Textarea

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)
		widgets = {'text': Textarea(attrs={'cols':50, 'rows':10}), 
		'title': Textarea(attrs={'cols':50, 'rows':1})}
