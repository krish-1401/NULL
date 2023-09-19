from django.shortcuts import render,redirect
from .forms import clerkform
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_tobe
# Create your views here.
def registerClerk(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        c_form=clerkform(request.POST)
        if c_form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,password=password)
            user.save()
            clerk=c_form.save(commit=False)
            clerk.user=user
            clerk.save()

    else:
        # form=UserForm()
        c_form=clerkform()
    
    context={
        # 'form':form,
        'c_form':c_form,
    }
    return render(request,'clerk/registerClerk.html',context)

def loginClerk(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        password=password.POST['password']

        user=authenticate(first_name=first_name,password=password)
        if user is not None:
            login_tobe(request,user)
            return redirect('clerk:dashboard')
        else:
            return redirect('clerk:loginClerk')
    return render(request,'clerk/login.html')

def dashboard(request):
    return render(request,'clerk/dashboard.html')
