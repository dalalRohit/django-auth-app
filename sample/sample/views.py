from django.shortcuts import render
from django.template import loader
from . import views
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def index(request):
    #return HttpResponse('<h1>Home page of Auth-App </h1>')

    return  render(request,'accounts/index.html',context={
        'title':"Home page"
    })


def login(request):
    #return HttpResponse('<h3>Login page</h3>')

    return  render(request,'accounts/login.html',context={
        'title':"Login page"
    })

def register(request):
    # return HttpResponse('<h2>Register page</h2>')
    return  render(request,'accounts/register.html',context={
        'title':"Register page"
    })
    # form=UserCreationForm()
    # args={'form':form}
    # return render(request,'accounts/register.html',args)
