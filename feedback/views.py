from django.shortcuts import render
from django.http import HttpResponse
def feedback(request):
    return render(request, 'feedback/feedback.html')
# Create your views here.
