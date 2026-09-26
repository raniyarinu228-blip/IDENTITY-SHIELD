from django.shortcuts import render
from django.http import HttpResponse
def view(request):
    return render(request, 'reply/view.html')
def reply(request):
    return render(request, 'reply/reply.html')

# Create your views here.
