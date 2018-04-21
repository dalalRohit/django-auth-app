from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return HttpResponse('<h2>From accounts/views </h2>')

# def login(request):
#     if request.method=='POST':
#         return HttpResponse('<h1>Login POST</h1>')

def register(request):
    if request.method=='POST':
        #return HttpResponse('<strong>POSTED</strong>')
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request,user)
            else:
                return HttpResponse('<strong>Problem creating user</strong>')
            return redirect('accounts/profile')
    else:
        form=UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    args={'name':'Rohit'}
    return render(request,'accounts/profile.html',args)
