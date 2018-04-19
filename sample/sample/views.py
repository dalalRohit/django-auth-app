from django.shortcuts import render
from django.template import loader
from . import views

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1>Home page of Auth-App </h1>')

    return  render(request,'index.html',context={
        'title':"Home page"
    })


def login(request):
    #return HttpResponse('<h3>Login page</h3>')
    return  render(request,'login.html',context={
        'title':"Login page"
    })

def register(request):
    #return HttpResponse('<h2>Register page</h2>')
    return  render(request,'register.html',context={
        'title':"Register page"
    })