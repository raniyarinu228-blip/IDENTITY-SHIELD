from django.urls import path,include
from user import views
urlpatterns = [
<<<<<<< HEAD
     path('user/',views.user),
     path('photo/',views.photo),
     path('chat/',views.chat),
     path('like/',views.like),
=======
     path('register/',views.register),
     path('prof/',views.prof),
>>>>>>> 887e2eb5634c0ea25f314d1aff681fdb756c807d
]