from django.shortcuts import render
from django.utils import timezone
from .models import PostsSubmit
from .forms import PostsSubmitForm

def add_product(request):
	form = PostsSubmitForm()
	context = {'form':form}
	return render(request, 'blog/add_product.html', context)	

	
def save_product(request):
	if request.method == "POST":	
		form = PostsSubmitForm(request.POST, request.FILES)
		print("outside if saveproduct")
		print(form.errors)
       		if form.is_valid():
			print('save_productviewsample')
       			form.save
       			context = {'form':form}
       			print form.errors
	       		return render(request, 'blog/add_product', context)
	else:
       		form = PostsSubmitForm()
		print(form.errors)
  		return render(request, 'blog/save_product', {'form': form}) 
