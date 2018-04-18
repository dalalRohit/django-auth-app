from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1>Auth page </h1>')

    temp=loader.get_template('auth/index.html')
    return render(request,temp)
