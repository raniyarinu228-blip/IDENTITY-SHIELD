from django.shortcuts import render
from django.http import HttpResponse
def friend(request):
    return render(request, 'friend/friend.html')
def manage(request):
    return render(request, 'friend/manage.html')
# Create your views here.
