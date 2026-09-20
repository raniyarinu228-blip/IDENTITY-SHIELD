from django.urls import path,include
from main_templates import views as mviews
urlpatterns = [
     path('ind/', mviews.index),
     path('admin/', mviews.admin),
     path('user/', mviews.user),
     path('technical/', mviews.technical),
]