from django.urls import path,include
from comments import views
urlpatterns = [
     path('comment/', views.comment),
]