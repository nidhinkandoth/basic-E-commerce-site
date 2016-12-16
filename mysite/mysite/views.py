from .forms import UserForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import RequestContext

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()

    return render(request, 'registration/register.html', {'user_form': user_form,  'registered': registered})
