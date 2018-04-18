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
