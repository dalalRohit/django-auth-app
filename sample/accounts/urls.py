from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from django.contrib.auth.views import login

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^accounts/register',views.register,name="register"),

]
