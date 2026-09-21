from django.urls import path,include
from friend import views
urlpatterns = [
     path('friend/', views.friend),
     path('manage/', views.manage), 
]