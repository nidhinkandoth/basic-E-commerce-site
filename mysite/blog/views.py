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
		#print("outside if saveproduct")
		print(form.errors)
       		if form.is_valid():
			#print('save_productviewsample')
       			form.save()
       			context = {'form':form}
       			print form.errors
	       		return render(request, 'blog/save_product.html', context)
	else:
       		form = PostsSubmitForm()
		print(form.errors)
  		return render(request, 'blog/add_product.html', {'form': form})


 
def product_display(request):
	List = PostsSubmit.objects.all()
	context = {'List':List}
        return render(request, 'blog/product_display.html',context)
def click_product(request, product_id):
	#print List
	#print product_id
	obj = PostsSubmit.objects.get(id=product_id)
	#print key
	#obj = PostsSubmit.objects.get(id = key)
	print obj
	return  render(request,'click_product.html', {'obj':obj})
