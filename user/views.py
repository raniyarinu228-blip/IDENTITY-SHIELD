from django.shortcuts import render
from django.http import HttpResponse
def user(request):
    return render(request, 'user/user.html')
def photo(request):
    return render(request, 'user/photo.html')
def chat(request):
    return render(request, 'user/chat.html')
def like(request):
    return render(request, 'user/like.html')

# Create your views here.
