"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from core.views import home, about, contact, skill_create, skill_delete, skill_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('skills/add/', skill_create, name = 'skill_create'),
    path('skills/<int:pk>/delete/', skill_delete, name='skill_delete'),
    path('skills/<int:pk>/edit/', skill_edit, name='skill_edit'),

]
