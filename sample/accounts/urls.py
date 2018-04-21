from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from django.contrib.auth.views import login


urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^register',views.register,name="register"),
    url(r'^login',views.login,name="login"),
    url(r'^profile',views.profile,name="Profile")

]
