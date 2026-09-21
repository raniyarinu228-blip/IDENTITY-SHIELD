from django.shortcuts import render
from django.http import HttpResponse
def register(request):
    return render(request, 'user/register.html')
def prof(request):
    return render(request, 'user/prof.html')
# Create your views here.
