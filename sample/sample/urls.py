from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'',include('auth.urls')),
    path('', views.index , name="index"),
    path('login', views.login, name="Login"),
    path('register', views.register, name="Register")

]
