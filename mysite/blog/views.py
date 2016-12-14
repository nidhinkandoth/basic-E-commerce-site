from django.shortcuts import render
from django.utils import timezone
from .models import PostsSubmit
from blog.forms import PostsSubmitForm

def add_product(request):
	form = PostsSubmitForm()
	context_variable = {'form':form}
	return render(request, 'blog/add_product.html', context_variable)	

