from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main_templates/index.html')
def admin(request):
    return render(request, 'main_templates/admin.html')
def user(request):
    return render(request, 'main_templates/user.html')
def technical(request):
    return render(request, 'main_templates/technical.html')
def home(request):
    return render(request, 'main_templates/home.html')

# Create your views here.
