from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model 
# from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_tobe
from django.contrib.auth import logout as logout_tobe
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import User
from .forms import UserForm

User=get_user_model()
# Create your views here.
def main(request):
    return render(request,'investor/investor.html',{})


def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            # user=form.save(commit=False)
            form.save()
            # username=form.cleaned_data.get('username')
            # messages.success(request,f'Welcome {username}, your account is created')
            return redirect('investor:login')
    else:
        form=UserForm()
    return render(request,'investor/register.html',{'form':form})


def login(request):
    if request.method=="POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password') 
        user = authenticate(request, phone_number=phone_number, password=password) 
        if user is not None:
            login_tobe(request,user)
            return redirect('investor:main')
        else:
            return redirect('investor:login')
    else:
        return render(request,'investor/login.html',{})
    