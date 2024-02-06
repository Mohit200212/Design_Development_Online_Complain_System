"""geekyshows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('login/', views.Login, name='login'),
    path('logout/',views.Logout,name='logout'),
    path('complain/',views.Complain,name='complain'),
    path('cse/',views.Cse,name='cse'),
    path('me/',views.Me,name='me'),
    path('ec/',views.Ec,name='ec'),
    path('ce/',views.Ce,name='ce'),
    path('pharma/',views.Pharma,name='pharma'),
    path('mba/',views.Mba,name='mba'),
    path('bs/',views.Bs,name='bs'),


]
urlpatterns += staticfiles_urlpatterns()