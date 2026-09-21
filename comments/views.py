from django.shortcuts import render
from django.http import HttpResponse
def comment(request):
    return render(request, 'comments/comment.html')
# Create your views here.
