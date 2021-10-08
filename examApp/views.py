from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from loginApp.models import User


# Create your views here.
def examIndex(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=request.session['user']),
    }
    return render(request, 'exam.html', context)