from django.shortcuts import render
from django.http import HttpResponse
def complaint(request):
    return render(request, 'complaint/complaint.html')
def comp(request):
    return render(request,'complaint/comp.html')
# Create your views here.
