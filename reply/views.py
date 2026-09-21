from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< Updated upstream
def view(request):
    return render(request, 'reply/view.html')
=======
def reply(request):
    return render(request, 'reply/reply.html')
>>>>>>> Stashed changes

# Create your views here.
