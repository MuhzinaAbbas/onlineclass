"""
URL configuration for classproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from classapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register',views.register,name='reg'),
    path('about',views.about,name='about'),
    path('enquiry',views.enquiry,name='enq'),
    path('view/<int:id>',views.view,name='viw'),
    path('delete/<int:id>',views.delete,name='del'),
    path('update/<int:id>',views.update,name='up'),
    path('contact',views.contact,name='cnct'),
    path('login',views.login,name='login'),
    path('course',views.course,name='crs'),
    path('index1',views.index1,name='index1'),
    path('logout',views.logout,name='logout'),
]
