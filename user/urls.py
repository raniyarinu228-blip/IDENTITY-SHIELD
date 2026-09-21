from django.urls import path,include
from user import views
urlpatterns = [
     path('user/',views.user),
     path('photo/',views.photo),
     path('chat/',views.chat),
     path('like/',views.like),
]