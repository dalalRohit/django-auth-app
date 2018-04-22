from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from django.contrib.auth.views import logout
from django.contrib.auth.views import login


urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^register',views.register,name="register"),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^profile/$',views.profile,name="Profile"),
    url(r'^profile/edit/$',views.edit_profile,name="edit profile"),
    url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),
    url(r'^change-password$',views.change_password,name="edit profile")

]
