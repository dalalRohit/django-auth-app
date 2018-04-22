from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def index(request):
    return HttpResponse('<h2>From accounts/views </h2>')

# def login(request):
#     if request.method=='POST':
#         return HttpResponse('<h1>Login POST</h1>')

def register(request):
    if request.method=='POST':
        #return HttpResponse('<strong>POSTED</strong>')
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request,user)
            else:
                return HttpResponse('<strong>Problem creating user</strong>')
            return redirect('/accounts/profile')
    else:
        form=SignUpForm()

    return render(request, 'accounts/register.html', {'form': form,'title':"Register page"})

def profile(request):
    args={'name':request.user,'title':"Profile Page"}
    return render(request,'accounts/profile.html',args)

def edit_profile(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)


def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/change_password.html',args)
