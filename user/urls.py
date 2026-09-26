from django.urls import path,include
from user import views
urlpatterns = [

     path('user/',views.user),

     path('photo/',views.photo),
     path('chat/',views.chat),
     path('like/',views.like),

     path('register/',views.register),
     path('prof/',views.prof),

     path('authent/',views.authent),

]