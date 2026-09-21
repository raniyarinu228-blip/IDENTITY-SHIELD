from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
def user(request):
    return render(request, 'user/user.html')
<<<<<<< Updated upstream
def photo(request):
    return render(request, 'user/photo.html')
def chat(request):
    return render(request, 'user/chat.html')
def like(request):
    return render(request, 'user/like.html')
=======
def authent(request):
    return render(request, 'user/authent.html')
>>>>>>> Stashed changes

=======
def register(request):
    return render(request, 'user/register.html')
def prof(request):
    return render(request, 'user/prof.html')
>>>>>>> 887e2eb5634c0ea25f314d1aff681fdb756c807d
# Create your views here.
