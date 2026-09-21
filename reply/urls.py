from django.urls import path,include
from reply import views
urlpatterns = [
<<<<<<< Updated upstream
    path('view/', views.view),
=======
    path('reply/', views.reply),
>>>>>>> Stashed changes
]