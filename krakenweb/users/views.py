from users.models import UserRegistrationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.

#Registration view
def registration(request):
     form=UserRegistrationForm
     context={
         'form':form
     }
     if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if(form.is_valid()):
            user=form.save()
            messages.success(request=request,message="Registration successful")
            login(request=request,user=user)
            return redirect('shop:home')
        else:
            for msg in form.error_messages:
                messages.error(request,f'Error: {msg}')
                return render(request,template_name='registration.html',context=context)
     return render(request,template_name='registration.html',context=context);

