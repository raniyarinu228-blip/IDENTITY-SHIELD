from django.shortcuts import render
from django.http import HttpResponse
def feedback(request):
    return render(request, 'feedback/feedback.html')
def feed(request):
    return render(request, 'feedback/feed.html')
# Create your views here