from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^accounts/',include('accounts.urls')),

    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
]
