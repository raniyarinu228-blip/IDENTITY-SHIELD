from django.urls import path,include
from complaint import views
urlpatterns = [
     path('complaint/', views.complaint),
     path('comp/',views.comp),
]