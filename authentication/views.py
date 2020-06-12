from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import reverse

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    
    context = {
        "user":request.user
    }
    return render(request, "users/user.html", context)