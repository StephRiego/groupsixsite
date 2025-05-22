"""
URL configuration for groupsixsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from crud import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', include('crud.urls')),
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', login_required(views.home), name='home'),
    path('user/edit/<int:userId>/', login_required(views.edit_user), name='edit_user'),
    path('add/user/', login_required(views.add_user), name='add_user'),
    path('gender/list/', login_required(views.gender_list), name='gender_list'),
    path('gender/add/', login_required(views.add_gender), name='add_gender'),
    path('user/list/', login_required(views.user_list), name='user_list'),
    path('user/add/', login_required(views.add_user), name='add_user'),

]
