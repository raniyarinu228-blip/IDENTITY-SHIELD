"""
URL configuration for project project.

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('login/',include('login.urls')),
    path('chat/',include('chat.urls')),
    path('comments/',include('comments.urls')),
    path('complaint/',include('complaint.urls')),
    path('reply/',include('reply.urls')),
    path('feedback/',include('feedback.urls')),
    path('main_templates/',include('main_templates.urls')),
<<<<<<< HEAD
    path('admin/',include('main_templates.urls')),
    path('user/',include('main_templates.urls')),
    path('technical/',include('main_templates.urls')),
    path('feed/',include('feedback.urls')),
    path('home/',include('main_templates.urls')),
=======
    path('friend/',include('friend.urls')),
>>>>>>> 887e2eb5634c0ea25f314d1aff681fdb756c807d
]
