from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h2>From accounts/views </h2>')

def register(request):
    if request.method=='POST':
        return HttpResponse('<h1>Data POSTED </h1>')
